import os
import json
import inspect
import ast
import concurrent.futures
import importlib.util
import sys
import random
import glob

from pathlib import Path
from func_timeout import func_timeout, FunctionTimedOut
from collections import namedtuple
from timeit import default_timer as timer

# namedtuple: A factory function from the collections module that creates tuple subclasses with named fields.
# It enables access to elements by attribute (dot notation) as well as by index, improving code readability.
# Syntax: from collections import namedtuple
#          Point = namedtuple('Point', ['x', 'y'])
#          p = Point(1, 2); print(p.x, p[1])
# 
# Main operations:
# - _replace(**kwargs): Return a new instance with specified fields replaced.
# - _asdict(): Return a dict mapping field names to their values.
# - index(value): Return the index of the first occurrence of the value.
# - _fields: Tuple of field names.
# - _make(iterable): Create a new instance from an iterable.


import solvers_pre
import solvers_evo

Solver = namedtuple('Solver', ['name', 'path', 'source', 'o_score', 't_score'])
Differ = namedtuple('Differ', ['name', 'path', 'source', 'score_type', 's_score', 't_score'])

Mutation = namedtuple('Mutation', ['present', 'old', 'new'])

Path('solvers_lnk.py').touch()
import solvers_lnk
Path('solvers_dir.py').touch()
import solvers_dir

# Flags for training and evaluation modes
# train: true for train task
#        false for test task
# eval: false if we have correct result
#       true if we don't
Flags = namedtuple('Flags', ['train', 'eval'])

OKT = namedtuple('OKT', ['ok', 't'])

BAD_SOLVERS = {
    '27a28665', # Broken in solvers_ref.py
    '29623171', # Broken in solvers_ref.py
    '39a8645d', # Broken in solvers_ref.py
    '50846271', # Broken in solvers_ref.py
    '6455b5f5', # Broken in solvers_ref.py
    '6855a6e4', # Broken in solvers_ref.py
    '88a62173', # Broken in solvers_ref.py
    '9af7a82c', # Broken in solvers_ref.py
    '9f236235', # Broken in solvers_ref.py
    'a3325580', # Broken in solvers_ref.py
    'a64e4611', # Broken in solvers_ref.py
    'a87f7484', # Broken in solvers_ref.py
    'b230c067', # Broken in solvers_ref.py
    'ba97ae07', # Broken in solvers_ref.py
    'c8cbb738', # Broken in solvers_ref.py
    'd6ad076f', # Broken in solvers_ref.py
    'e40b9e2f', # Broken in solvers_ref.py
    # 'a65b410d', # Gets closer, but no solve
    # '6773b310', # Gets closer, but no solve
    # 'ef135b50', # Gets closer, but no solve
    # '6a1e5592', # Gets closer, but no solve
    # 'a8d7556c', # Gets closer, but no solve
    # 'd06dbe63', # Gets closer, but no solve
    # '484b58aa', # Gets closer, but no solve
    # 'e26a3af2', # Seems to hang
} 


class VariableInliner(ast.NodeTransformer):
    def __init__(self):
        self.assignments = {}
        self.safe_to_inline = set()  # Track which variables are safe to inline
        self.processing = set()      # Track variables being processed to avoid recursion loops


    def visit_Assign(self, node):
        # Only handle simple assignments to variable names
        if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            # For other kinds of assignments (tuple unpacking, etc.), visit children
            return self.generic_visit(node)
        
        var_name = node.targets[0].id

        # Store the original value before processing
        original_value = ast.unparse(node.value)

        # First, recursively visit all child nodes to inline variables and substitute constants
        node.value = self.visit(node.value)
            
        # Store the expression for later substitution
        self.assignments[var_name] = node.value
        self.safe_to_inline.add(var_name)

        # Remove assignments from the output
        return None


    def visit_Name(self, node):
        # Replace variable reference with its assigned value, if available and safe
        if isinstance(node.ctx, ast.Load) and node.id in self.safe_to_inline:
            # Avoid infinite recursion
            if node.id in self.processing:
                return node
                
            # Track that we're processing this variable
            self.processing.add(node.id)

            # Get a deep copy of the expression to substitute
            expr = ast.parse(ast.unparse(self.assignments[node.id])).body[0].value
            
            # Recursively process the expression to inline any variables inside it
            result = self.visit(expr)
            
            # Done processing this variable
            self.processing.remove(node.id)
            return result
            
        return node


def inline_variables(source_code):
    start_total = timer()
    parse_t0 = timer()
    tree = ast.parse(source_code)
    parse_dt = timer() - parse_t0

    visit_t0 = timer()
    inliner = VariableInliner()
    # Process tree and collect assignments
    tree = inliner.visit(tree)
    visit_dt = timer() - visit_t0

    fix_t0 = timer()
    # Convert back to source code
    ast.fix_missing_locations(tree)
    unparse_source = ast.unparse(tree)
    fix_dt = timer() - fix_t0

    total_dt = timer() - start_total
    # Record timings if profiler is set
    if _prof is not None:
        _prof['utils.inline_variables.parse'] += parse_dt
        _prof['utils.inline_variables.visit'] += visit_dt
        _prof['utils.inline_variables.unparse'] += fix_dt
        _prof['utils.inline_variables.total'] += total_dt

    return unparse_source

# Lightweight module-level profiler wiring
_prof = None
def set_profiler(prof):
    """Register a defaultdict(float) profiler to accumulate timings."""
    global _prof
    _prof = prof




def get_data(train=True, sort_by_size=False, task_id=None):
    """
    Load ARC task data with options for sorting and filtering.
    
    Args:
        train: Whether to load training data (True) or evaluation data (False)
        sort_by_size: Whether to sort tasks by file size
        task_id: Optional task_id to filter for a specific task
        
    Returns:
        Dictionary containing task data organized by train/test sets
    """
    path = f'../data/{"training" if train else "evaluation"}'
    data = {}
    
    if sort_by_size:
        # Get entries sorted by file size
        entries = [(entry.name, entry.stat().st_size) 
                  for entry in os.scandir(path) if entry.is_file()]
        sorted_entries = sorted(entries, key=lambda x: x[1])
        files_to_process = [fn for fn, _ in sorted_entries]
    else:
        # Get entries in default order
        files_to_process = os.listdir(path)
    
    # Process each file (or just the specified task_id)
    for fn in files_to_process:
        task_key = fn.rstrip('.json')
        if task_id is None or task_key == task_id:
            with open(f'{path}/{fn}') as f:
                data[task_key] = json.load(f)
    
    # Convert to tuples for immutability
    ast = lambda g: tuple(tuple(r) for r in g)
    return {
        'train': {k: [{
            'input': ast(e['input']),
            'output': ast(e['output']),
        } for e in v['train']] for k, v in data.items()},
        'test': {k: [{
            'input': ast(e['input']),
            'output': ast(e['output']),
        } for e in v['test']] for k, v in data.items()}
    }


def get_solver_source(task_id, imports=None, best_only=False):    
    # if imports is None:
    #     imports = [solvers_dir]

    solve_header = 'from dsl import *\nfrom constants import *\n\n'
    solve_identity = f'{solve_header}def solve(S, I, C):\n    O = identity(I)\n    return O\n'
    best_solver = Solver('solve', 'solve_identity.py', solve_identity, 0, 999)

    for imp in imports:
        if imp == solvers_pre and task_id in BAD_SOLVERS:
            # Skip bad solvers from solvers_pre
            continue

        if imp == solvers_dir:
            solver_list = []
            weights = []
            best_o_score = -1
            best_item = None
            file_paths = glob.glob(f'solver_dir/solve_{task_id}/[0-9]*/[0-9]*/[0-9a-f]*.py')
            if not file_paths:
                # print_l(f'No solver found for {task_id}, using identity')
                return Solver('solve', None, solve_identity, 0, 999)
            random.shuffle(file_paths)
            for file_path in file_paths:
                sections = file_path.split('/')
                o_score = int(sections[2])
                t_score = int(sections[3])

                curr_solver = Solver('solve', file_path, None, o_score, t_score)

                if curr_solver.o_score > best_o_score:
                    best_o_score = curr_solver.o_score
                    best_solver = curr_solver

                solver_list.append(curr_solver)
                weights.append(curr_solver.o_score)

            if not best_only and sum(weights) > 0:
                select_solver = random.choices(solver_list, weights=weights, k=1)[0]
            else:
                select_solver = best_solver

            if not select_solver:
                continue

            if select_solver.path is None:
                continue

            solver_module = load_path(select_solver.path)
            if solver_module is None:
                continue

            func_name = select_solver.name
            # print_l(f'Found {func_name} in {solver_module.__name__}')
            solver = getattr(solver_module, func_name)
            select_solver = select_solver._replace(source=f'{solve_header}{inspect.getsource(solver)}')
            return select_solver

        else:
            func_name = f'solve_{task_id}'
            # print_l(f'Looking for {func_name} in {imp.__name__}', end=' ')
            if hasattr(imp, func_name):
                # print_l(f'Found {func_name} in {imp.__name__}')
                solver = getattr(imp, func_name)
                return Solver(func_name, imp.__name__, f'{solve_header}{inspect.getsource(solver)}', 
                        0, 999)

    # print_l(f'No solver found for {task_id}, using None')
    return Solver('solve', None, None, 0, 999)


def get_differs(import_names, best_only=False):
    differs = {}
    for imp_name in import_names:
        if imp_name == 'differs':
            differ_module = importlib.import_module(imp_name)
            for name in dir(differ_module):
                if name.startswith('differ_'):
                    differ = getattr(differ_module, name)
                    differs[name] = Differ(name, imp_name, inspect.getsource(differ), None, 0, 999)
        else:
            # new_imp_name = f'differ_md5.{imp_name}'
            # differ_module = importlib.import_module(new_imp_name)
            # differ = getattr(differ_module, 'differ')
            # name = f'differ_{imp_name}'
            # differs[name] = Differ(name, imp_name, inspect.getsource(differ), None, 0, 999)

            sections = imp_name.split('/')
            score_type = sections[1]  # 'iz' or 'zo'
            s_score = int(sections[3])
            t_score = int(sections[4])
            # solver_md5 = sections[5]
            # differ_md5 = sections[6]
            differ_md5 = sections[5]

            differ_module = importlib.import_module(f'differ_md5.{differ_md5}')
            differ = getattr(differ_module, 'differ')
            name = f'differ_{differ_md5}'
            differs[name] = Differ(name, differ_md5, inspect.getsource(differ), None, 0, 999)

    return differs


def get_solvers(imports, best_only=False):
    # Get both train and test tasks
    train_data = get_data(train=True)
    # eval_data = get_data(train=False)

    # total_data = {k: {**train_data[k], **eval_data[k]} for k in ['train', 'test']}
    total_data = {k: {**train_data[k]} for k in ['train', 'test']}
    task_list = list(total_data['train'].keys())

    # Exclude known bad solvers
    # bad_solvers = BAD_SOLVERS
    # task_list = [task_id for task_id in task_list if task_id not in bad_solvers]

    solvers = {}
    for task_id in task_list:
        solver = get_solver_source(task_id, imports, best_only=best_only)
        if solver.source is not None:
            solvers[task_id] = solver

    return solvers


def load_path(file_path):
    """
    Dynamically load a Python module from a file path
    Args: module_name: Path to the Python file to load
    Returns: Loaded module object
    """
    symlink_path = Path(file_path)
    if symlink_path.is_symlink() and not symlink_path.exists():
        # Just remove the broken symlink
        symlink_path.unlink()
        return None
        
    module_name = file_path[:-3].replace('/', '.')
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def load_module(module_name):
    """
    Dynamically load a Python module from a file path
    Args: module_name: Path to the Python file to load
    Returns: Loaded module object
    """
    file_path = f'{module_name}.py'
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Module file not found: {file_path}")
        
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def run_with_timeout(func, args, timeout=5):
    try:
        return False, func_timeout(timeout, func, args)
    except FunctionTimedOut:
        return True, None


def print_l(msg, sep=' ', end='\n', flush=False):
    """Print line number and message"""
    frame = inspect.currentframe()
    caller_frame = frame.f_back
    file_path = caller_frame.f_code.co_filename
    file_name = os.path.basename(file_path)
    line_number = caller_frame.f_lineno
    print(f"{file_name}:{line_number}: {msg}", sep=sep, end=end, flush=flush)


def show_exception(msg, e=None):
    frame = inspect.currentframe()
    caller_frame = frame.f_back
    file_path = caller_frame.f_code.co_filename
    file_name = os.path.basename(file_path)
    function_name = caller_frame.f_code.co_name
    line_number = caller_frame.f_lineno
    if e is not None:
        print(f"!!! EXCEPTION !!! {type(e).__name__}: {e}")
    print(f"!!! ========= !!! {file_name}:{line_number} {function_name}: {msg}")


def got_id_str_in(code, id_str):
    """Checks if a specific identifier string exists in the given Python code.

    This function parses the provided code into an AST (Abstract Syntax Tree) and
    searches for any Name nodes that match the specified identifier string.

    Args:
        code (str): The Python code to search through as a string
        id_str (str): The identifier string to search for

    Returns:
        bool: True if the identifier string is found in the code, False otherwise

    Example:
        >>> got_id_str_in("x = 5", "x")
        True
        >>> got_id_str_in("y = 5", "x") 
        False
    """
    tree = ast.parse(code)
    return any(
        isinstance(node, ast.Name) and node.id == id_str
        for node in ast.walk(tree)
    )


pat_s = r'\s*'
# pat_n = r'[^\d\W]\w*' # name
pat_n = r'[_a-zA-Z][_a-zA-Z0-9]*(\[\d*(:\d*)?(:\d*)?\])?' # name

# Just to make pat_list more compact
s = pat_s
n = pat_n

# NOTE First pattern isn't selective enough, as it also matches functions
#      If/when fixing, make sure that processing for matches work properly
# pat_list = [
#     # rf'{s}(?P<n1>{n}) = (?P<n2>{n})', 
#     rf'{s}(?P<n1>{n}) = (?P<n2>{n})\((?P<n3>{n})\)', 
#     rf'{s}(?P<n1>{n}) = (?P<n2>{n})\((?P<n3>{n}), (?P<n4>{n})\)', 
#     rf'{s}(?P<n1>{n}) = (?P<n2>{n})\((?P<n3>{n}), (?P<n4>{n}), (?P<n5>{n})\)', 
#     rf'{s}(?P<n1>{n}) = (?P<n2>{n})\((?P<n3>{n}), (?P<n4>{n}), (?P<n5>{n}), (?P<n6>{n})\)',]

call_pat_list = [
    # rf'{s}(?P<n1>{n}) = (?P<n2>{n})', 
    rf'{s}(?P<n1>{n}) = (?P<n2>{n})\((?P<n3>{n})\)', 
    rf'{s}(?P<n1>{n}) = (?P<n2>{n})\((?P<n3>{n}), (?P<n4>{n})\)', 
    rf'{s}(?P<n1>{n}) = (?P<n2>{n})\((?P<n3>{n}), (?P<n4>{n}), (?P<n5>{n})\)', 
    rf'{s}(?P<n1>{n}) = (?P<n2>{n})\((?P<n3>{n}), (?P<n4>{n}), (?P<n5>{n}), (?P<n6>{n})\)',]

func_pat_list = [
    # rf'{s}(?P<n1>{n}) = (?P<n2>{n})', 
    rf'(?P<n2>{n})\((?P<n3>{n})\)', 
    rf'(?P<n2>{n})\((?P<n3>{n}), (?P<n4>{n})\)', 
    rf'(?P<n2>{n})\((?P<n3>{n}), (?P<n4>{n}), (?P<n5>{n})\)', 
    rf'(?P<n2>{n})\((?P<n3>{n}), (?P<n4>{n}), (?P<n5>{n}), (?P<n6>{n})\)',]

sig_list = [
    # '{n2}',
    '{n2}({n3})',
    '{n2}({n3}, {n4})',
    '{n2}({n3}, {n4}, {n5})',
    '{n2}({n3}, {n4}, {n5}, {n6})',
]


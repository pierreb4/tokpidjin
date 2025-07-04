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


import solvers_pre
import solvers_evo

Path('solvers_lnk.py').touch()
import solvers_lnk
Path('solvers_dir.py').touch()
import solvers_dir


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


def get_source(task_id, imports=None, best_only=False):    
    if imports is None:
        imports = [solvers_evo, solvers_pre]
    for imp in imports:
        if imp == solvers_pre and task_id in BAD_SOLVERS:
            # Skip bad solvers from solvers_pre
            continue

        if imp == solvers_dir:
            mod_list = []
            weights = []
            best_score = 0
            best_item = None
            # list files in solver_dir/solve_{task_id}/*
            files = glob.glob(f'solver_dir/solve_{task_id}/*/*.py')
            if not files:
                continue
            for file in files:
                sections = file.split('/')
                curr_item = {
                    'path': file,
                    'name': f'solve_{sections[-1][:-3]}'}

                score = int(sections[-2])
                if score > best_score:
                    best_score = score
                    best_item = curr_item

                mod_list.append(curr_item)
                weights.append(score)

            if not best_only:
                mod_item = random.choices(mod_list, weights=weights, k=1)[0]
            else:
                mod_item = best_item

            if not mod_item:
                continue

            solver_module = load_path(mod_item['path'])
            func_name = mod_item['name']
            solver = getattr(solver_module, func_name)
            print_l(f'Found solver: {func_name} in {solver_module.__name__}')
            return func_name, inspect.getsource(solver)

        else:
            func_name = f'solve_{task_id}'
            if hasattr(imp, func_name):
                solver = getattr(imp, func_name)
                # print_l(f'Found solver: {func_name} in {imp.__name__}')
                return func_name, inspect.getsource(solver)
    return None, None


def get_solvers(imports, best_only=False):
    # Get both train and test tasks
    train_data = get_data(train=True)
    eval_data = get_data(train=False)

    total_data = {k: {**train_data[k], **eval_data[k]} for k in ['train', 'test']}
    task_list = list(total_data['train'].keys())

    # Exclude known bad solvers
    bad_solvers = BAD_SOLVERS
    task_list = [task_id for task_id in task_list if task_id not in bad_solvers]

    solvers = {}
    for task_id in task_list:
        func_name, source = get_source(task_id, imports, best_only=best_only)
        if source is not None:
            solvers[task_id] = (func_name, source)

    return solvers


def load_path(file_path):
    """
    Dynamically load a Python module from a file path
    Args: module_name: Path to the Python file to load
    Returns: Loaded module object
    """
    module_name = file_path[:-3].replace('/', '.')
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Module file not found: {file_path}")
        
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


def old_run_with_timeout(func, args, timeout=5):
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(func, *args)
        try:
            return (False, future.result(timeout=timeout))
        except concurrent.futures.TimeoutError:
            return (True, None)


def run_with_timeout(func, args, timeout=5):
    try:
        return (False, func_timeout(timeout, func, args))
    except FunctionTimedOut:
        return (True, None)


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


import os

# Only set CUDA environment if CUDA_HOME doesn't exist or if running in Kaggle
# This prevents bus errors when CUDA paths don't exist
cuda_home = "/usr/local/cuda-12.5"
if os.path.exists(cuda_home) or "KAGGLE_KERNEL_RUN_TYPE" in os.environ:
    os.environ["CUDA_HOME"] = cuda_home
    os.environ["PATH"] = f"{cuda_home}/bin:" + os.environ["PATH"]
    os.environ["LD_LIBRARY_PATH"] = f"{cuda_home}/lib64:" + os.environ.get("LD_LIBRARY_PATH", "")
    cuda_stub_path = f"{cuda_home}/targets/x86_64-linux/lib/stubs"
    if "LD_LIBRARY_PATH" in os.environ:
        os.environ["LD_LIBRARY_PATH"] += f":{cuda_stub_path}"
    else:
        os.environ["LD_LIBRARY_PATH"] = cuda_stub_path

import json
import inspect
import ast
import concurrent.futures
import importlib.util
import sys
import random
import glob
import asyncio
import threading

from pathlib import Path
from collections import namedtuple
from timeit import default_timer as timer
# from concurrent.futures import ProcessPoolExecutor


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
# import solvers_evo

Solver = namedtuple('Solver', ['name', 'path', 'source', 'o_score', 't_score'])
Differ = namedtuple('Differ', ['name', 'path', 'source', 's_score', 't_score'])

Mutation = namedtuple('Mutation', ['present', 'old', 'new'])
HintValue = namedtuple('HintValue', ['hint', 'value'])

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

DO_PRINT_LIST = [ 'mbp-2022.lan', 'mbp-2022.local', 'simone' ]
# DO_PRINT_LIST = [ 'simone' ]
DO_DEBUG = False
DO_PRINT = False
# DO_PRINT = os.uname()[1] in DO_PRINT_LIST
# DO_PRINT = os.uname()[1].startswith('mbp') or os.uname()[1] == 'simone'
DO_PRINT = os.uname()[1] == 'simone'
DO_PRINT = os.uname()[1].startswith('mbp-2022')

# Thread-based timeout function (no asyncio needed!)
from queue import Queue, Empty

def call_with_timeout(func, args, timeout=5):
    """
    Call a function with a timeout using threads (no asyncio).
    
    This is a pure threading approach that doesn't interfere with ThreadPoolExecutor
    or asyncio event loops. Each timeout runs in its own daemon thread.
    
    DAEMON + EXCEPTION RE-RAISING: Threads are daemon (clean exit) but critical
    exceptions (MemoryError, SystemError) are re-raised in the main thread to
    crash immediately instead of being silently ignored.
    
    Args:
        func: Function to call
        args: List of arguments to pass to function
        timeout: Timeout in seconds
    
    Returns:
        (timed_out: bool, result: Any)
        - (False, result) if function completed successfully
        - (True, None) if function timed out
        - Raises exception if critical error occurred
    """
    result_queue = Queue()
    exception_queue = Queue()
    
    def worker():
        try:
            result = func(*args)
            result_queue.put(result)
        except Exception as e:
            exception_queue.put(e)
    
    thread = threading.Thread(target=worker)
    thread.daemon = True  # Daemon: Allow clean Python exit
    thread.start()
    thread.join(timeout=timeout)
    
    if thread.is_alive():
        # Thread is still running after timeout
        return True, None  # (timed_out, result)
    
    # Check for exceptions
    try:
        exception = exception_queue.get_nowait()
        # Re-raise critical exceptions immediately
        if isinstance(exception, (MemoryError, SystemError, KeyboardInterrupt)):
            raise exception
        # Log other exceptions for debugging
        print_l(f"Exception in timeout thread: {type(exception).__name__}: {exception}")
        return True, None  # Treat non-critical exceptions as timeouts
    except Empty:
        pass
    
    # Get successful result
    try:
        result = result_queue.get_nowait()
        return False, result  # (timed_out, result)
    except Empty:
        return True, None


# Dual thread pool architecture to avoid nested usage conflicts
# 
# High-level executor: For parallel batch operations (sample scoring, batch inline)
# Low-level executor: For run_with_timeout and other internal operations
# 
# This separation prevents thread pool deadlock where high-level operations
# that use the executor internally would exhaust all workers.

_high_level_executor = None
_low_level_executor = None
_executor_lock = threading.Lock()

def get_high_level_executor():
    """
    Get executor for high-level parallel operations (sample scoring, batch processing).
    
    Use this for:
    - Parallel sample scoring
    - Batch inline_variables processing
    - Other top-level parallel operations
    
    Start with 4 workers (conservative), can be increased to 6-8 if stable.
    """
    global _high_level_executor
    if _high_level_executor is None:
        with _executor_lock:
            if _high_level_executor is None:
                # Conservative start: 4 workers (same as low-level)
                # Can increase to 6-8 after validating no resource contention
                _high_level_executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    return _high_level_executor

def get_low_level_executor():
    """
    Get executor for low-level operations (run_with_timeout, internal operations).
    
    Use this for:
    - run_with_timeout wrapper
    - Internal batt() operations
    - Any operation that might be called from high-level parallel code
    
    Reasons for 4 worker limit:
    1. Avoid macOS file descriptor limits (~256 per process)
    2. Prevent resource contention (GPU, memory, I/O)
    3. Limit concurrent batt() calls which are resource-intensive
    4. Balance between parallelism and system stability
    """
    global _low_level_executor
    if _low_level_executor is None:
        with _executor_lock:
            if _low_level_executor is None:
                _low_level_executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    return _low_level_executor

def get_executor():
    """
    Get default executor for backward compatibility.
    
    Legacy code uses this, which returns the low-level executor.
    New code should use get_high_level_executor() or get_low_level_executor() explicitly.
    """
    return get_low_level_executor()


def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def symlink(file_path, link_path):
    """
    Create a symlink for the given file.
    If the symlink already exists, remove it and create a new one.
    """
    home_folder = Path.home()

    if home_folder == Path('/root'):
        # Running in Kaggle
        full_name = f'/kaggle/working/tokpidjin/{file_path}'
    else:
        full_name = f'{home_folder}/dsl/tokpidjin/{file_path}'

    try:
        os.symlink(full_name, link_path)
    except FileExistsError:
        os.remove(link_path)
        os.symlink(full_name, link_path)


class VariableInliner(ast.NodeTransformer):
    def __init__(self):
        self.assignments = {}
        self.safe_to_inline = set()  # Track which variables are safe to inline
        self.processing = set()      # Track variables being processed to avoid recursion loops
        self.recursion_depth = 0     # Track recursion depth to prevent infinite loops
        self.max_recursion_depth = 100  # Maximum recursion depth before bailing out


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
            # Avoid infinite recursion - check if we're in a cycle
            if node.id in self.processing:
                return node
            
            # Check recursion depth
            if self.recursion_depth > self.max_recursion_depth:
                # Hit recursion limit - return original name instead of inlining
                return node
                
            # Track that we're processing this variable
            self.processing.add(node.id)
            self.recursion_depth += 1

            try:
                # Get a deep copy of the expression to substitute
                expr = ast.parse(ast.unparse(self.assignments[node.id])).body[0].value
                
                # Recursively process the expression to inline any variables inside it
                result = self.visit(expr)
            except (RecursionError, OverflowError) as e:
                # Recursion limit or memory issue - bail out and return original node
                result = node
            finally:
                # Done processing this variable
                self.recursion_depth -= 1
                self.processing.discard(node.id)
            
            return result
            
        return node


def inline_variables(source_code, timeout_seconds=0.5):
    """
    Inline variable assignments in source code.
    
    Args:
        source_code: Python source code string
        timeout_seconds: Maximum time allowed for inlining (default 0.1s, vs 30s previously)
                        Normal solvers inline in <100ms. 0.1s timeout catches infinite loops.
        
    Returns:
        str: Inlined source code
        
    Raises:
        TimeoutError: If inlining takes too long (likely infinite loop in AST visitor)
        
    Notes:
        - Reduced from 30s to 0.1s: normal inlining is <100ms, generous enough for pathological cases
        - If timeout occurs, solver is skipped (caught in run_batt.py inline_one/inline_differ)
        - AST parsing errors also caught and handled gracefully
    """
    start_total = timer()
    
    def _inline_with_timeout():
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
    
    # Run with timeout protection
    from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeoutError
    try:
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(_inline_with_timeout)
            try:
                result = future.result(timeout=timeout_seconds)
                return result
            except FutureTimeoutError:
                raise TimeoutError(f"inline_variables timed out after {timeout_seconds}s - likely infinite loop in AST visitor")
    except TimeoutError:
        # Re-raise timeout errors
        raise
    except Exception as e:
        # For other errors, try to return something reasonable
        raise RuntimeError(f"inline_variables failed: {e}") from e


def parallel_inline_variables(source_codes):
    """Process multiple source codes in parallel"""
    with ProcessPoolExecutor() as executor:
        return list(executor.map(inline_variables, source_codes))


class GPUVariableInliner(VariableInliner):
    def __init__(self, use_gpu=True):
        super().__init__()
        self.use_gpu = use_gpu and GPU_AVAILABLE
        
    def batch_process(self, nodes):
        """Process multiple AST nodes in parallel"""
        if self.use_gpu and len(nodes) > 10:
            return self._gpu_batch_visit(nodes)
        return [self.visit(node) for node in nodes]


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
    prefix = '../arc-prize-2025'
    stage = 'training' if train else 'evaluation'
    challenges_path = f'{prefix}/arc-agi_{stage}_challenges.json'
    solutions_path = f'{prefix}/arc-agi_{stage}_solutions.json'

    with open(challenges_path) as fp:
        challenges = json.load(fp)
    with open(solutions_path) as fp:
        solutions = json.load(fp)

    # Combine challenges and solutions into data
    data = {}
    for task_id, challenge in challenges.items():
        # print_l(f'{task_id = } - {challenge = }')
        if task_id in solutions:
            data[task_id] = challenge
            # print_l(f'{solutions[task_id] = }')
            # Add output to each test case
            for i, test_case in enumerate(data[task_id]['test']):
                if i < len(solutions[task_id]):
                    test_case['output'] = solutions[task_id][i]

    # assert False, "Halt here - Troubleshooting"

    # if sort_by_size:
    #     # Get entries sorted by file size
    #     entries = [(entry.name, entry.stat().st_size) 
    #               for entry in os.scandir(path) if entry.is_file()]
    #     sorted_entries = sorted(entries, key=lambda x: x[1])
    #     files_to_process = [fn for fn, _ in sorted_entries]
    # else:
    #     # Get entries in default order
    #     files_to_process = os.listdir(path)
    
    # # Process each file (or just the specified task_id)
    # for fn in files_to_process:
    #     task_key = fn.rstrip('.json')
    #     if task_id is None or task_key == task_id:
    #         with open(f'{path}/{fn}') as f:
    #             data[task_key] = json.load(f)
    
    # Convert to tuples for immutability
    # Rename 'train' samples 'demo' to avoid confusion with the 'train' dataset
    # So we have train/eval datasets and demo/test samples
    ast = lambda g: tuple(tuple(r) for r in g)
    return {
        'demo': {k: [{
            'input': ast(e['input']),
            'output': ast(e['output']),
        } for e in v['train']] for k, v in data.items()},
        'test': {k: [{
            'input': ast(e['input']),
            'output': ast(e['output']),
        } for e in v['test']] for k, v in data.items()}
    }


def old_get_data(train=True, sort_by_size=False, task_id=None):
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
    # Rename 'train' samples 'demo' to avoid confusion with the 'train' dataset
    # So we have train/eval datasets and demo/test samples
    ast = lambda g: tuple(tuple(r) for r in g)
    return {
        'demo': {k: [{
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
    best_solver = Solver('solve', 'solve_identity.py', solve_identity, 0, 0)

    for imp in imports:
        if imp == solvers_pre and task_id in BAD_SOLVERS:
            # Skip bad solvers from solvers_pre
            continue

        if imp == solvers_dir:
            solver_list = []
            weights = []
            best_o_score = -1
            best_item = None
            # file_paths = glob.glob(f'solver_dir/solve_{task_id}/[0-9]*/[0-9]*/[0-9a-f]*.py')

            # Pick solver from this task only if it solves at least one sample
            file_paths = glob.glob(f'solver_dir/solve_{task_id}/[1-9]*/[0-9]*/[0-9a-f]*.py')
            if not file_paths:
                # print_l(f'No solver found for {task_id}, using identity')
                # return Solver('solve', None, None, 0, 0)
                # return Solver('solve', None, solve_identity, 0, 0)

                # Pick random solver from any task
                # file_paths = glob.glob('solver_dir/solve_*/[0-9]*/[0-9]*/[0-9a-f]*.py')
                continue
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
                        0, 0)

    # print_l(f'No solver found for {task_id}, using None')
    return Solver('solve', None, None, 0, 0)
    # return Solver('solve', None, solve_identity, 0, 0)


def get_solvers(imports, best_only=False):
    # Get both train and test tasks
    train_data = get_data(train=True)
    # eval_data = get_data(train=False)
    # total_data = {k: {**train_data[k], **eval_data[k]} for k in ['demo', 'test']}
    total_data = {k: {**train_data[k]} for k in ['demo', 'test']}

    task_list = list(total_data['demo'].keys())

    # Exclude known bad solvers
    # bad_solvers = BAD_SOLVERS
    # task_list = [task_id for task_id in task_list if task_id not in bad_solvers]

    solvers = {}
    for task_id in task_list:
        solver = get_solver_source(task_id, imports, best_only=best_only)
        if solver.source is not None:
            solvers[task_id] = solver

    return solvers


def get_differs(import_names, best_only=False):
    differs = {}
    for imp_name in import_names:
        if imp_name == 'differs':
            differ_module = importlib.import_module(imp_name)
            for name in dir(differ_module):
                if name.startswith('differ_'):
                    differ = getattr(differ_module, name)
                    differs[name] = Differ(name, imp_name, inspect.getsource(differ), 0, 999)
        else:
            # new_imp_name = f'differ_md5.{imp_name}'
            # differ_module = importlib.import_module(new_imp_name)
            # differ = getattr(differ_module, 'differ')
            # name = f'differ_{imp_name}'
            # differs[name] = Differ(name, imp_name, inspect.getsource(differ), 0, 999)

            sections = imp_name.split('/')
            # Updated path structure: differ_dir/solve_{task_id}/{s_score}/{t_score}/{md5}
            s_score = int(sections[2])
            t_score = int(sections[3])
            # solver_md5 = sections[4]
            # differ_md5 = sections[5]
            differ_md5 = sections[4]

            differ_module = importlib.import_module(f'differ_md5.{differ_md5}')
            differ = getattr(differ_module, 'differ')
            name = f'differ_{differ_md5}'
            differs[name] = Differ(name, differ_md5, inspect.getsource(differ), s_score, t_score)

    return differs


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


# def run_with_timeout(func, args, timeout=5):
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         future = executor.submit(func, *args)
#         try:
#             result = future.result(timeout=timeout)
#             return False, result
#         except concurrent.futures.TimeoutError:
#             return True, None



async def run_with_timeout(func, args, timeout=5):
    """
    Run function with timeout. Uses thread executor with proper timeout handling.
    """
    try:
        # Use thread executor with proper timeout handling
        loop = asyncio.get_event_loop()
        executor = get_low_level_executor()
        
        # Run in executor with timeout
        result = await asyncio.wait_for(
            loop.run_in_executor(executor, func, *args), 
            timeout
        )
        return False, result
    except asyncio.TimeoutError:
        # Timeout occurred - return timeout flag
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


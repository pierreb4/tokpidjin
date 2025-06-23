import os
import json
import inspect
import ast
import concurrent.futures

import solvers_pre
import solvers_evo


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
    'a65b410d', # Gets closer, but no solve
    '6773b310', # Gets closer, but no solve
    'ef135b50', # Gets closer, but no solve
    '6a1e5592', # Gets closer, but no solve
    'a8d7556c', # Gets closer, but no solve
    'd06dbe63', # Gets closer, but no solve
    '484b58aa', # Gets closer, but no solve
    'e26a3af2', # Seems to hang
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


def get_source(task_id):
    if hasattr(solvers_evo, f'solve_{task_id}'):
        solver = getattr(solvers_evo, f'solve_{task_id}')
    elif hasattr(solvers_pre, f'solve_{task_id}'):
        if task_id in BAD_SOLVERS:
            return None
        solver = getattr(solvers_pre, f'solve_{task_id}')
    else:
        return None

    return inspect.getsource(solver)


def get_solvers():
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
        source = get_source(task_id)
        if source is not None:
            solvers[task_id] = source

    return solvers


def run_with_timeout(func, args, timeout=5):
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(func, *args)
        try:
            result = (False, future.result(timeout=timeout))
        except concurrent.futures.TimeoutError:
            # print_l(f'Timeout in {func.__name__}({args})')
            # print_l(f'Timeout in {func.__name__}')
            result = (True, None)
    return result


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


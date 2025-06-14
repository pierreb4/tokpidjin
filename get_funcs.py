import importlib
import re
import ast

from utils import *

from dsl import *
import dsl
import solvers_pre
# Replace some solvers in solvers_pre with ones from solvers_evo
import solvers_evo


def get_variables(solver_source):
    # solver_source contains a single function definition
    # with each line an assignment to a variable
    lines = solver_source.split('\n')
    
    # Split each line at '=' to get variable names and their values
    assignments = [line.split('=', 1) for line in lines if ' = ' in line]
    # Create a dictionary to hold variable names and their values
    variables = {}
    for var, value in assignments:
        var = var.strip()
        value = value.strip()
        if var and value:
            # Store the variable name and its value in the dictionary
            variables[var] = value
    # Print the variable names and their values
    # for var, value in variables.items():
    #     print_l(f"{var} = {value}")
    return variables


def rename_args_by_return_order(code):
    # Extract the function signature and body
    match = re.match(r'def\s+(\w+)\(([^)]*)\):\s*\n?\s*return\s+(.*)', code, re.DOTALL)
    if not match:
        return 0, "Input code is not a valid one-line function"

    func_name, args_str, return_expr = match.groups()
    args = [arg.strip() for arg in args_str.split(',') if arg.strip()]

    if not args:
        # If there are no arguments, return the original code
        return 0, code

    # Find the order of arguments as they first appear in the return expression
    arg_pattern = r'\b(' + '|'.join(map(re.escape, args)) + r')\b'
    found_args = []
    for m in re.finditer(arg_pattern, return_expr):
        arg = m.group(1)
        if arg not in found_args:
            found_args.append(arg)

    # If any arguments are not used in return, append them at the end in original order
    for arg in args:
        if arg not in found_args:
            found_args.append(arg)

    # Map old argument names to new a1, a2, ...
    # Use 'a' as prefix to avoid collisions during replacement
    arg_map = {old: f'a{i+1}' for i, old in enumerate(found_args)}
    arg_num = len(found_args)

    # Replace old argument names with new ones in the return expression
    new_return_expr = return_expr
    for old_arg, new_arg in arg_map.items():
        new_return_expr = re.sub(r'\b' + re.escape(old_arg) + r'\b', new_arg, new_return_expr)

    # Build the new function signature in the new order
    new_args_list = [arg_map[arg] for arg in found_args]

    return arg_num, f'def {func_name}({", ".join(new_args_list)}):\n    return {new_return_expr}'


def type_to_string(type_obj):
    """Convert a type object to its string representation."""
    if isinstance(type_obj, str):
        return type_obj
    elif hasattr(type_obj, '__name__'):
        return type_obj.__name__
    elif str(type_obj) == "<class 'int'>":
        return 'int'
    elif str(type_obj) == "<class 'str'>":
        return 'str'
    elif str(type_obj) == "<class 'bool'>":
        return 'bool'
    else:
        # For complex types like typing.Callable, typing.Tuple[...], etc.
        type_str = str(type_obj)
        # Clean up the string representation
        if type_str.startswith('typing.'):
            return type_str.replace('typing.', '')
        return type_str


def get_arg_types_from_call(node, globals_dict):
    arg_types = {}
    if isinstance(node, ast.Call):
        f_name = node.func.id if isinstance(node.func, ast.Name) else None
        if f_name and f_name in globals_dict:
            func = globals_dict[f_name]
            if hasattr(func, '__annotations__'):
                annotations = func.__annotations__

                # Only add individual argument names (not full expressions) and return type
                for i, arg in enumerate(node.args):
                    # Only a\d+ variables are considered
                    if isinstance(arg, ast.Name) and re.match(r'S\b|I\b|[ax]\d+\b$', arg.id):
                    # if isinstance(arg, ast.Name) and not re.match(r'^[A-Z]\d+$', arg.id):
                        param_names = list(annotations.keys())
                        if i < len(param_names) and param_names[i] != 'return':
                            arg_types[arg.id] = type_to_string(annotations[param_names[i]])

                # Add return type if available
                if 'return' in annotations:
                    arg_types['return'] = type_to_string(annotations['return'])
        elif f_name is not None:
            arg_types[f_name] = 'Callable'

        # Recursively process nested calls
        for arg in node.args:
            arg_types |= get_arg_types_from_call(arg, globals_dict)

    return arg_types


def collect_all_arg_types(func_code, globals_dict):
    all_arg_d = {}
    tree = ast.parse(func_code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            all_arg_d |= get_arg_types_from_call(node, globals_dict)
    return all_arg_d


def get_funcs(candidates, task_id, variables):
    ref_var = {}
    for var, value in variables.items():
        ref_var[var] = []
        x_vars = re.findall(r'\bS\b|\bI\b|\bx\d+\b', value) or ['']

        # Keep list of references for each value
        for x_var in x_vars:
            if x_var == '':
                continue
            if x_var not in ref_var[var]:
                ref_var[var].append(x_var) 

        # Generate function for each variable found
        for old_x_var in x_vars:
            if old_x_var in ['S', 'I']:
                continue

            if old_x_var == '':
                func_name = f"get_{task_id}_{var}_c"
                func_body = value
                func_args = ''
            else:
                func_name = f"get_{task_id}_{var}_{old_x_var}"
                old_x_var_pattern = r'\b' + old_x_var + r'\b'
                func_body = re.sub(old_x_var_pattern, variables[old_x_var], value)

                ref_list = set()
                for v in ref_var[var]:
                    if v != old_x_var:
                        ref_list.add(v)
                    else:
                        ref_list.update(ref_var[v])

                func_args = ', '.join(ref_list)
            
            func_code = f"def {func_name}({func_args}):\n    return {func_body}"
            arg_num, func_code = rename_args_by_return_order(func_code)

            # Get resulting arguments and type hints
            all_arg_d = collect_all_arg_types(func_code, globals())

            # Add missing variable hints if not present
            for i in range(arg_num):
                arg_name = f'a{i+1}'
                if arg_name not in all_arg_d:
                    all_arg_d[arg_name] = 'Any'

            return_type = 'Any'
            tree = ast.parse(func_code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Fix argument annotations
                    for arg in node.args.args:
                        if arg.arg in all_arg_d:
                            arg.annotation = ast.Name(id=all_arg_d[arg.arg], ctx=ast.Load())
        
                    # Fix return type annotation
                    if 'return' in all_arg_d:
                        return_type = all_arg_d['return']
                        node.returns = ast.Name(id=return_type, ctx=ast.Load())

            ast.fix_missing_locations(tree)
            func_code = ast.unparse(tree)

            lines = func_code.split('\n')
            return_call = lines[-1].strip()
            if return_call.startswith('return '):
                func_body = return_call[7:]

            # Put in a tuple non-return types sorted by arg name
            arg_d = all_arg_d.copy()
            # print_l(f'{func_name = } - {arg_d = }')
            sorted_args = sorted(arg_d.items(), key=lambda x: x[0])
            all_arg_t = tuple(v for k, v in sorted_args if k != 'return')

            func_d = {
                (
                    func_name,
                    return_type,
                    *all_arg_t,
                ): func_body,
            }

            with open(f'solver_dsl/{func_name}.py', 'w') as f:
                f.write(f"{func_code}\n\n")
                f.write(f"# {all_arg_d}\n\n")
                f.write(f"{func_d = }\n\n")

            if arg_num != len(all_arg_t):
                print_l(f'!!! ERROR !!! solver_dsl/{func_name}.py - {arg_num = }')
                print_l(f'{func_body = }')
                print_l(f'{all_arg_t = }') 
                print_l(f'{all_arg_d = }')
                continue

            if f'{return_type}' not in candidates.keys():
                candidates[f'{return_type}'] = set()
            candidates[f'{return_type}'].add((f'{func_body}', f'{all_arg_t}'))


def get_source(obj):
    """Get source for an object, returning reconstructed source if not available."""
    try:
        return inspect.getsource(obj)
    except (OSError, TypeError) as e:
        # Check for stored source attribute first
        if hasattr(obj, "__solver_source__"):
            return obj.__solver_source__

        # For dynamically loaded solver functions, reconstruct basic signature
        if callable(obj) and obj.__name__.startswith("solve_"):
            task_id = obj.__name__[6:]  # Extract task ID from function name
            return f"def {obj.__name__}(S, I):\n    # Dynamically loaded solver for task {task_id}\n    pass"

        print_l(f'- Exception! - {obj.__name__}')
        show_exception("exec fail", e)

        # For other cases, return empty string silently
        return ""


def write_solvers_dsl(candidates):
    with open('solvers_dsl.py', 'w') as f:
        f.write(f'{candidates = }')


def main(task_id=None):
    """Main function that runs the solver builder.
    
    Args:
        task_id: Optional task ID to focus on. If None, a random task will be selected.
    """
    quiet = True
    
    train_data = get_data(train=True)
    eval_data = get_data(train=False)
    total_data = {k: {**train_data[k], **eval_data[k]} for k in train_data.keys()}

    if task_id is None:
        count = -1
        task_id_list = list(total_data['train'].keys()) 
    else:
        count = 1
        task_id_list = [task_id]

    candidates = {}
    for task_id in task_id_list:
        # Get solver source from solver_evo/solve_{task_id}.def or solvers_pre/solve_{task_id}.def
        try:
            module_name = f"solver_evo.solve_{task_id}_xxx"
            mod = importlib.import_module(module_name)
        except ModuleNotFoundError:
            try:
                module_name = f"solver_pre.solve_{task_id}_xxx"
                mod = importlib.import_module(module_name)
            except ModuleNotFoundError:
                if not quiet:
                    print(f"Module for task {task_id} not found in either solvers_evo or solvers_pre.")
                continue

        solver = getattr(mod, f"solve_{task_id}")
        solver_source = get_source(solver)
        variables = get_variables(solver_source)
        get_funcs(candidates, task_id, variables)

        count -= 1
        if count == 0:
            break

    write_solvers_dsl(candidates)


if __name__ == '__main__':
    import sys
    
    # Check if a task_id was provided as a command-line argument
    if len(sys.argv) > 1:
        task_id = sys.argv[1]
        main(task_id)
    else:
        main()  # Run with a random task ID

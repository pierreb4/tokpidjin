""" Words that go blue in comments: BUG FIXME HACK NOTE TODO XXX """

import inspect
import traceback
import ast
import re
import random
import time
import types
import os
from timeit import default_timer as timer
from typing import Annotated, get_origin, get_args
import typing

from utils import *
from constants import *
from helpers import *
from dsl import *
from get_funcs import *
from solvers_dsl import candidates
import dsl
import solvers_pre
# Replace some solvers in solvers_pre with ones from solvers_evo
import solvers_evo

def in_dev():
    return os.path.basename(__file__) == 'regen_dev.py'


def build_solver_dict(total_data, max_attempt=3, task_id_list=None):

    start_time = timer()

    filename = 'solvers_gen.out'
    with open(filename, 'w') as f:
        f.write(f"")

    # Create skeleton for solvers_gen.py
    filename = 'solvers_gen.py'
    with open(filename, 'w') as f:
        f.write(f"")

    solver_dict = {}
    cand_dict = {}
    pass_dict = {}
    best_match = {}
    arg_dict = {}
    solver_dict['done_hint'] = set()

    # Don't exclude task_id_list from learning
    todo_set = set()
    todo_set = add_todo_set(total_data, None, todo_set, None)

    solver_dict['todo_hint_sorted'] = [t[1] for t in sorted(todo_set)]

    dist_score_dict = {}
    hint_list = []
    call_score_dict = {}

    # Count the steps, as we may select the same function
    # several times, as long as it's a different call
    # Add steps for each task in turn
    g_correct = 0
    step = 0
    while step < 100000:
        step += 1
        # print_l(f'{step = }')

        if len(hint_list) > 0:
            hint = hint_list.pop(0)
        else:
            # NOTE This is training as we know it now :)
            hint = get_next_hint(solver_dict)

        if hint is None:
            break

        # Look for candidates that pass all samples
        got_closer = False
        for task_id in total_data['train'].keys():
            if task_id not in solver_dict.keys():
                solver_dict[task_id] = {}
            if 'todo' not in solver_dict[task_id].keys():
                solver_dict[task_id]['todo'] = True
            if 'source_gen' not in solver_dict[task_id].keys():
                solver_dict[task_id]['source_gen'] = []

            # Skip to specific tasks if we got a task_id_list
            if len(task_id_list) > 0 and task_id not in task_id_list:
                continue

            if step == 1:
                print_l(f'-- {task_id} -----')
            
            # Add test samples to the task
            task = total_data['train'][task_id] + total_data['test'][task_id]
            if task_id not in dist_score_dict.keys():
                dist_score_dict[task_id] = {}

            just_done = False
            for izzo in ['iz', 'zo']:
                # Check hint to see what helps. Sometimes this solves the task
                # NOTE Checks test sample(s), not train sample(s)
                #      Might pass testing and not pass training
                #      See tasks: 6455b5f5, 39a8645d, 9ddd00f0, d017b73f
                if not solver_dict[task_id]['todo']:
                    break
                just_done, solver_list = check_done(task, task_id, cand_dict, \
                        call_score_dict, dist_score_dict, pass_dict, hint, izzo)

                if hint in MONITORING_HINTS:
                    print_l(f'{just_done = }')

                """
                What comes here or close by:
                - check_done
                - start_list: add encode or policy step, follow type flavor
                - close_list: add decode step, need to be reversible later
                - check_list: add hint checker, source constants and/or prune
                - check_hint
                """


            if solver_dict[task_id]['todo']:
                # Only add steps when needed
                if not just_done:
                    got_closer, start_from = check_hint(task, task_id, cand_dict, \
                        call_score_dict, dist_score_dict, pass_dict, hint, step)

                if just_done:
                    # Solver passes training. We can keep checking hints on it
                    # (when working on multiple tasks), but no need to add more steps
                    solver_dict[task_id]['source_gen'] += solver_list
                    solver_source = '\n'.join(solver_list)

                    # Add to solvers_gen.py
                    if solver_source != []:
                        eval_str = "e" if task_id in EVALUATION_TASK_IDS else "t"

                        print(solver_source)
                        print_l(f"# {eval_str} - {step = } in {timer() - start_time:.1f}s\n\n")

                        # Also save to 'solver_evo/solve_{task_id}.def'
                        with open(f'solver_evo/solve_{task_id}.def', 'w') as f:
                            f.write(f"# Not intended to run standalone!\n\n")
                            f.write(solver_source)
                            f.write(f"\n# {eval_str} - {step = } in {timer() - start_time:.1f}s\n")

                    # Done with this task
                    solver_dict[task_id]['todo'] = False
                    g_correct += 1

        # Exit early when testing
        if len(task_id_list) == 0 and g_correct >= max_attempt:
            break

        if got_closer:
            todo_set = add_todo_set(total_data, start_from, todo_set, task_id_list)
            solver_dict['todo_hint_sorted'] = [t[1] for t in sorted(todo_set)]

    return solver_dict


def get_next_hint(solver_dict):
    for hint in solver_dict['todo_hint_sorted']:
        if hint in solver_dict['done_hint']:
            continue
        solver_dict['done_hint'].add(hint)
        return hint
    return None


def replace_random(value, input_list):
    current_idx = input_list.index(value)
    if current_idx == 0:  # First element
        offset = 1
    elif current_idx == len(input_list) - 1:  # Last element
        offset = -1
    else:
        offset = random.choice([-1, 1])
    
    new_idx = current_idx + offset
    return input_list[new_idx]


def safe_getsource(obj):
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

        
def get_full_hint(func_name):
    # NOTE If it's not found in globals() and it's a variable (x_n),
    # we might be able to see what it contains (maybe via dereferencing)
    if func_name in globals():
        func = globals()[func_name]
        values = [t for var, t in func.__annotations__.items()]
        n = len(values) - 1
        keys = ['n2', 'n3', 'n4', 'n5', 'n6'][:n] + ['return']
        # values = [t for var, t in func.__annotations__.items() if var != 'return']
        # keys = ['n3', 'n4', 'n5', 'n6']
        # hint_dict = {'n3': 'Grid', 'n4': 'C_iz', 'n5': 'C_zo'}
        return dict(zip(keys, values))
    else:
        if not re.match(r'^x[0-9]*$', func_name):
            print_l(f"Warning: Function {func_name} not found in globals()")
        func = None
        return {}


def get_hint_dict(func_name):
    # NOTE If it's not found in globals() and it's a variable (x_n),
    # we might be able to see what it contains (maybe via dereferencing)
    if func_name in globals():
        func = globals()[func_name]
        # values = [func.__name__] + [t for var, t in func.__annotations__.items() if var != 'return']
        # keys = ['n2', 'n3', 'n4', 'n5', 'n6']
        values = [t for var, t in func.__annotations__.items() if var != 'return']
        keys = ['n3', 'n4', 'n5', 'n6']
        # hint_dict = {'n3': 'Grid', 'n4': 'C_iz', 'n5': 'C_zo'}
        return dict(zip(keys, values))
    else:
        if not re.match(r'^x[0-9]*$', func_name):
            print_l(f"Warning: Function {func_name} not found in globals()")
        func = None
        return {}


def solve_p_g(key, m_dict, hint_dict, S, solver) -> str:
    # regen.py:274: solver.__name__ = 'solve_54d9e175'
    # regen.py:275: key = 'n3' - hint_dict[key] = 'Grid' - hint_dict = {'n3': 'Grid', 'n4': 'C_', 'n5': 'C_'}
    # regen.py:276: x_n = '6' - m_dict[key] = 'x6' - m_dict = {'n1': 'x7', 'n2': 'replace', 'n3': 'x6', 'n4': 'BLUE', 'n5': 'MAGENTA'}

    # For when there's no substitution
    pass_through = m_dict[key]

    # Work on color
    if hint_dict[key] != 'Grid':
        return pass_through

    # Ignore function calls, such as b_iz_n or b_zo_n
    # NOTE Would need to check x_dict, as x var could point one of those
    if not re.match(r'^x\d+$', m_dict[key]):
        return pass_through

    # Just use x number
    x_n = m_dict[key][1:]

    # Proceed with subbing attempt
    print_again = False
    # if solver.__name__ == 'solve_54d9e175':
    #     print_l(f"{solver.__name__ = }")
    #     print_l(f"{key = } - {hint_dict[key] = } - {hint_dict = }")
    #     print_l(f"{x_n = } - {m_dict[key] = } - {m_dict = }")
    #     print_again = True

    try:
        val_t = dsl.s_iz(S, solver, x_n, p_g)
    except Exception as e:
        # show_exception(f"Error in s_iz for {solver.__name__}", e)
        return pass_through
    if print_again and val_t != ():
        print_l(f"No error in s_iz: {solver = } - {val_t = }")
    r_n = val_t.index(color) if color in val_t else None
    if r_n is not None:
        # Or? f's_iz_n(S, {solver.__name__}, X{x_n}, p_g, R{r_n})'
        print_l(f's_iz_n(S, {solver.__name__}, {x_n}, p_g, R{r_n})')
        return f's_iz_n(S, {solver.__name__}, {x_n}, p_g, R{r_n})'
    try:
        val_t = dsl.s_zo(S, solver, x_n, p_g)
    except Exception as e:
        # show_exception(f"Error in s_zo for {solver.__name__}", e)
        return pass_through
    if print_again and val_t != ():
        print_l(f"No error in s_iz: {solver = } - {val_t = }")
    r_n = val_t.index(color) if color in val_t else None
    if r_n is not None:
        # Or? f's_zo_n(S, {solver.__name__}, X{x_n}, p_g, R{r_n})'
        print_l(f's_zo_n(S, {solver.__name__}, {x_n}, p_g, R{r_n})')
        return f's_zo_n(S, {solver.__name__}, {x_n}, p_g, R{r_n})'
    return pass_through
    

def get_hints(node_name):
    if node_name not in globals():
        return None

    global_id = globals()[node_name]
    if not inspect.isfunction(global_id):
        return None

    return [t for var, t in global_id.__annotations__.items()]


def get_func_details(call_node):
    args = []
    for arg in call_node.args:
        if isinstance(arg, ast.Name):
            args.append(arg.id)
        elif isinstance(arg, ast.Constant):
            args.append(arg.value)            
        else:
            # Convert to string representation
            args.append(ast.unparse(arg))

    # Handle different types of function calls
    if isinstance(call_node.func, ast.Name):
        func_id = call_node.func.id
    elif isinstance(call_node.func, ast.Attribute):
        func_id = call_node.func.attr
    # elif isinstance(call_node.func, ast.Call):
    #     # For nested function calls, use the string representation
    #     func_id = ast.unparse(call_node.func)
    else:
        # For other cases, use the string representation
        func_id = ast.unparse(call_node.func)

    return func_id, args


def substitute_const(self, node_value):
    """Recursively substitute constants in all nested function calls."""

    # If this is a Call node, process it
    if isinstance(node_value, ast.Call):
        expr = ast.unparse(node_value)
        parsed_expr = ast.parse(expr, mode='eval')

        func_id, func_arg = get_func_details(parsed_expr.body)
        hints = get_hints(func_id)
        
        if hints is not None:
            # First, recursively process arguments that are also function calls
            for i, arg in enumerate(node_value.args):
                if isinstance(arg, ast.Call):
                    substitution_result = substitute_const(self, arg)
                    if substitution_result is not None:
                        node_value.args[i] = substitution_result
            
            # Then apply hint-based substitutions
            for i, arg in enumerate(func_arg):
                if arg is None or i >= len(hints):
                    continue
                    
                hint = hints[i]
                
                if hint in ['Any', 'C_']:
                    func_arg[i] = substitute_color(self, arg)
                elif hint == 'FL':
                    func_arg[i] = substitute_rank(self, arg, FL_NAMES)
                elif hint == 'F_':
                    func_arg[i] = substitute_rank(self, arg, F_NAMES)
                elif hint == 'L_':
                    func_arg[i] = substitute_rank(self, arg, L_NAMES)
                elif hint == 'R_':
                    func_arg[i] = substitute_symbol(self, arg, R_NAMES)
                elif hint == 'R4':
                    func_arg[i] = substitute_symbol(self, arg, R4_NAMES)
                elif hint == 'R8':
                    func_arg[i] = substitute_symbol(self, arg, R8_NAMES)
                    self.score += 1
                elif hint == 'A8':
                    func_arg[i] = substitute_grid_angle(self, arg)
                elif hint not in [ 'Samples', 'Grid', 'Tuple', 
                        'Object', 'Objects', 'FrozenSet', 'Patch', 
                        'Callable', 'Container', 'ContainerContainer',
                        'Integer', 'IntegerSet', 'Numerical', 'Indices', 
                        'Boolean', 'IJ', 'A4', 
                    ]:
                    print_l(f'{hint = }')

                # if func_arg[i] in GENERIC_CONSTANTS.keys():
                #     self.score += 1

            # TODO Add to score for each hard-coded constant
            # Rebuild and return the call with the modified argument(s)
            return (ast.Call(
                func=ast.Name(id=func_id, ctx=ast.Load()),
                args=[ast.Name(id=arg, ctx=ast.Load()) if isinstance(arg, str) 
                    else arg for arg in func_arg],
                keywords=[])
            )
    
    # If this node has child nodes that could be function calls, process them
    # NOTE Not sure about score
    elif hasattr(node_value, 'args'):
        for i, arg in enumerate(node_value.args):
            if isinstance(arg, ast.Call):
                substitution_result = substitute_const(self, arg)
                if substitution_result is not None:
                    node_value.args[i] = substitution_result
    
    return None


def substitute_color(self, arg, constant_dict=COLORS):
    budget_random = 0.01

    # Get number corresponding to color constant
    # NOTE Maybe some x_n variables carry constants and could be replaced?
    if arg in constant_dict.keys():
        c = constant_dict[arg]
    elif arg in CONSTANTS.keys() and CONSTANTS[arg] in constant_dict.values():
        c = CONSTANTS[arg]
    else:
        # Probably 'Any' and not a color constant
        return arg

    S = self.S
    c_iz = dsl.c_iz(S, p_g)
    c_zo = dsl.c_zo(S, p_g)

    if c in c_iz and random.random() < 0.5:
        # Change the score at substitution time
        self.score -= 1
        return f'c_iz_n(identity(S), identity(p_g), identity(rbind(get_nth_t, F{c_iz.index(c)})))'
    elif c in c_zo and random.random() < 0.5:
        # Change the score at substitution time
        self.score -= 1
        return f'c_zo_n(identity(S), identity(p_g), identity(rbind(get_nth_t, F{c_zo.index(c)})))'
    elif random.random() < budget_random:
        # Same as usual random replacement
        return random.choice(list(constant_dict.keys()))

    # Get name corresponding to number
    constant_list = list(constant_dict.keys())
    return constant_list[c]


def substitute_grid_angle(self, arg, constant_dict=R8_NAMES):
    budget_random = 0.01

    # Only substitute constants 
    if arg not in constant_dict.keys():
        return arg

    c = constant_dict[arg]
    S = self.S
    if c == dsl.a_mr(S) and random.random() < 0.5:
        # Change the score at substitution time
        self.score -= 1
        return f'identity(a_mr(S))'        
    elif random.random() < budget_random:
        # Same as usual random replacement
        return random.choice(list(constant_dict.keys()))
    
    return arg


def substitute_rank(self, arg, constant_dict):
    budget_random = 0.01

    # Only substitute constants 
    if arg not in constant_dict.keys():
        return arg
    
    if random.random() < budget_random:
        return replace_random(arg, list(constant_dict.keys()))

    return arg


def substitute_symbol(self, arg, constant_dict):
    budget_random = 0.01

    # Substitute constants or calls
    if random.random() < budget_random:
        return random.choice(list(constant_dict.keys()))

    return arg


class VariableInliner(ast.NodeTransformer):
    def __init__(self, task_id, S, todo_set=set(), score=0):
        self.task_id = task_id
        self.S = S
        self.todo_set = todo_set
        self.score = score
        self.assignments = {}
        self.safe_to_inline = set()  # Track which variables are safe to inline
        self.processing = set()      # Track variables being processed to avoid recursion loops
        self.func_name = ''
        self.all_func_names = set()  # NEW: Track all function names seen
        self.func_name_counts = {}   # NEW: Count frequency of each function name
        self.func_name_order = []    # NEW: Track order of function names encountered

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
        
        # Then apply constant substitution to the entire expression tree
        substitution_result = substitute_const(self, node.value)
        if substitution_result is not None:
            node.value = substitution_result

        # if random.random() < 0.01:
        #     print_l(f'{original_value = } - {self.score = }')
    
        # Store the expression for later substitution
        self.assignments[var_name] = node.value
        self.safe_to_inline.add(var_name)

        # Log the substitution if it changed
        new_value = ast.unparse(node.value)

        # Get node's function name and track it
        if isinstance(node.value, ast.Call) \
            and isinstance(node.value.func, ast.Name):
            self.func_name = node.value.func.id
            
            # NEW: Track all function names
            self.all_func_names.add(self.func_name)
            self.func_name_counts[self.func_name] = self.func_name_counts.get(self.func_name, 0) + 1
            if self.func_name not in self.func_name_order:
                self.func_name_order.append(self.func_name)

            if self.func_name == 'a_mr':
                count = len(re.findall(rf'\b{re.escape(self.func_name)}\b', new_value))
                self.score -= min(2, count) * 2
                # print_l(f"{self.func_name = } - {count = } - {self.func_name_counts[self.func_name] = }")
            elif self.func_name == 'c_iz_n':
                count = len(re.findall(rf'\b{re.escape(self.func_name)}\b', new_value))
                self.score -= min(4, count) * 6
            elif self.func_name == 'c_zo_n':
                count = len(re.findall(rf'\b{re.escape(self.func_name)}\b', new_value))
                self.score -= min(4, count) * 6
            else:
                self.score += 1

        if var_name == 'O':
            # XXX Temporary, to recreate old sorting
            # self.score = len(new_value)

            self.todo_set.add((self.score, new_value, self.task_id))

        # Keep the assignment in the output (don't return None)
        return node


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


    def get_func_name_statistics(self):
        """Return statistics about function names encountered."""
        return {
            'all_func_names': self.all_func_names,
            'func_name_counts': self.func_name_counts,
            'func_name_order': self.func_name_order,
            'total_unique_functions': len(self.all_func_names),
            'most_common_functions': sorted(self.func_name_counts.items(), 
                                          key=lambda x: x[1], reverse=True)
        }


def inline_variables(task_id, source_code, S, todo_set):
    tree = ast.parse(source_code)
    inliner = VariableInliner(task_id, S, todo_set, 0)
    
    # Process tree and collect assignments
    tree = inliner.visit(tree)

    # NEW: Print function name statistics
    # stats = inliner.get_func_name_statistics()
    # print(f"Function Name Statistics:")
    # print(f"  Total unique functions: {stats['total_unique_functions']}")
    # print(f"  All function names: {sorted(stats['all_func_names'])}")
    # print(f"  Function counts: {stats['func_name_counts']}")
    # print(f"  Order encountered: {stats['func_name_order']}")
    # print(f"  Most common functions: {stats['most_common_functions'][:10]}")  # Top 10

    # Convert back to source code
    ast.fix_missing_locations(tree)

    # if in_dev() and len(source_code) < 84:
    #         print_l(f'-- {len(source_code) = } -----')
    #         print(f'{source_code}')
    #         print(f'{ast.unparse(tree)}')

    return ast.unparse(tree)


def add_todo_set(total_data, start_from, todo_set, task_id_list=None):
    """ Get todo set from solver code """

    if task_id_list is None:
        task_id_list = []

    for task_id in total_data['train'].keys():
        if task_id in task_id_list:
            continue

        # Use 'train', not 'test' samples
        task = total_data['train'][task_id]
        S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in task)

        try:
            # Check that solver is in module
            if hasattr(solvers_evo, f'solve_{task_id}'):
                solver = getattr(solvers_evo, f'solve_{task_id}')
            elif hasattr(solvers_pre, f'solve_{task_id}'):
                if task_id in BAD_SOLVERS:
                    continue
                solver = getattr(solvers_pre, f'solve_{task_id}')
            else:
                # print_l(f"Warning: No solver for task {task_id}")
                continue
        except AttributeError:
            show_exception(f"No solver for task {task_id}")
            continue

        solver_source = safe_getsource(solver)

        # Replace a call or 2
        random_budget = 0.8
        while random.random() < random_budget:
            variables = get_variables(solver_source)

            if len(variables) == 0:
                break

            # Select a random variable to replace
            var_to_replace = random.choice(list(variables.items()))
            func_code = var_to_replace[1]
            all_arg_d = collect_all_arg_types(func_code, globals())

            # Select possible candidates
            selection = set()
            if 'return' not in all_arg_d \
                    or all_arg_d['return'] not in candidates.keys():
                continue

            for cand in candidates[all_arg_d['return']]:
                sorted_args = sorted(all_arg_d.items(), key=lambda x: x[0])
                all_arg_t = tuple(v for k, v in sorted_args if k != 'return')

                if cand[1] == f'{all_arg_t}':
                    selection.add(cand)

            # Pick a candidate from the selection and replace
            if selection:
                pick = random.choice(list(selection))
                if in_dev() and random.random() < 0.01/random_budget:
                    print_l(f'{task_id} - {pick = }')

                sub_id = 1
                cand_code = pick[0]
                for old_arg, old_type in all_arg_d.items():
                    if old_arg == 'return':
                        continue
                    cand_code = re.sub(rf'\ba{sub_id}\b', old_arg, cand_code)
                    sub_id += 1

                repl_var = var_to_replace[0]
                srch_pat = re.escape(f'{repl_var} = {var_to_replace[1]}')
                repl_pat = f'{repl_var} = {cand_code}'
                solver_source = re.sub(srch_pat, repl_pat, solver_source)
            random_budget /= 2

        if start_from is not None:
            lines = solver_source.split('\n')
            for i, line in enumerate(lines):
                if not line.strip().startswith('def '):
                    lines[i] = re.sub(r'\bI\b', start_from, line)
            solver_source = '\n'.join(lines)

        # Add to to_do from this solver
        one_source = inline_variables(task_id, solver_source, S, todo_set)
        # print(f'{one_source = }')

    for tup in todo_set:
        if match := re.search(r'[ax]\d+', tup[1]):
            print_l(f"Found {match[0]} in {tup[1]}")
            assert False

    print_l(f'-- {len(todo_set) = } -----')

    if in_dev():
        sorted_todo_set = sorted(todo_set, key=lambda s: (len(s), s))
        with open('todo_set_dev.txt', 'w') as f:
            for item in sorted_todo_set:
                f.write(f"{item}\n")

        for item in sorted_todo_set:
            if os.path.exists(f'solver_evo/solve_{item[2]}.def'):
                continue
            # Don't pick as next the task that we are currently working on
            if os.path.exists('next_task_dev.txt'):
                with open('next_task_dev.txt', 'r') as f:
                    next_task = f.read().strip()
                if next_task == item[2]:
                    continue
            with open('next_task_dev.txt', 'w') as f:
                f.write(f"{item[2]}\n")
            break

    return todo_set


def old_add_todo_set(data, start_from, todo_set, task_id_list=None):
    """ Get todo set from solver code """

    if task_id_list is None:
        task_id_list = []

    todo_set = set()
    # NOTE data may be total_data
    for task_id in data['train'].keys():
        if task_id in task_id_list:
            continue

        # Use 'train', not 'test' samples
        task = data['train'][task_id]
        S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in task)

        try:
            # Check that solver is in module
            if hasattr(solvers_evo, f'solve_{task_id}'):
                solver = getattr(solvers_evo, f'solve_{task_id}')
            elif hasattr(solvers_pre, f'solve_{task_id}'):
                solver = getattr(solvers_pre, f'solve_{task_id}')
            else:
                # print_l(f"Warning: No solver for task {task_id}")
                continue
        except AttributeError:
            show_exception(f"No solver for task {task_id}")
            continue
            
        solver_source = safe_getsource(solver)
        solver_list = solver_source.split('\n')

        x_dict = {}
        budget_random = 0.5
        
        for line in solver_list.copy():
            if line.startswith('    return'):
                break
            if line.startswith('def'):
                continue
            # Ignore comment, pass, test and intermediate return lines
            if line.startswith('    #'):
                continue
            if line.startswith('    pass'):
                continue
            if line.startswith('    if'):
                continue
            if line.startswith('        return'):
                continue


            # if re.match(r'^\s*x2 =', line):
            #     print_l(f"{task_id = } - {line = }")

            # if start_from is not None:
            #     # print_l(f"Replacing 'I' with {start_from} in {line.lstrip()}")
            #     line = re.sub(r'\bI\b', start_from, line)

                # if line.startswith('    O = x2('): 
                #     print_l(f"Here! {line}")


            cand_set = set()
            for i, pattern in enumerate(call_pat_list):
                match = re.match(pattern, line)
                if not match:
                    # print_l(f'No match: {i} - {line.lstrip()}')
                    continue

                m_dict = match.groupdict()

                print_again = False
                hint_dict = get_hint_dict(m_dict['n2'])

                for key, value in hint_dict.items():
                    # Ranking constants
                    if value == 'FL' and m_dict[key] in FL_NAMES.keys():
                        if random.random() < budget_random:
                            m_dict[key] = replace_random(m_dict[key], list(FL_NAMES.keys()))
                    elif value == 'F_' and m_dict[key] in F_NAMES.keys():
                        if random.random() < budget_random:
                            m_dict[key] = replace_random(m_dict[key], list(F_NAMES.keys()))
                    elif value == 'L_' and m_dict[key] in L_NAMES.keys():
                        if random.random() < budget_random:
                            m_dict[key] = replace_random(m_dict[key], list(L_NAMES.keys()))
                    # Symbolic constants
                    elif value == 'R4' and m_dict[key] in R4_NAMES.keys():
                        if random.random() < budget_random:
                            budget_random /= 2
                            m_dict[key] = random.choice(list(R4_NAMES.keys()))
                    elif value == 'R8' and m_dict[key] in R8_NAMES.keys():
                        if random.random() < budget_random:
                            budget_random /= 2
                            m_dict[key] = random.choice(list(R8_NAMES.keys()))
                    elif value == 'R_' and m_dict[key] in R_NAMES.keys():
                        if random.random() < budget_random:
                            budget_random /= 2
                            m_dict[key] = random.choice(list(R_NAMES.keys()))

                    # Deal with color constants (either generic or specific)
                    elif value == 'C_' and m_dict[key] in COLORS.keys():
                        # Get number corresponding to color constant
                        color = COLORS[m_dict[key]]
                        # Get name corresponding to number (in case we substitute)
                        # m_dict[key] = color_list[color]
                        color_list = list(COLORS.keys())
                        m_dict[key] = color_list[color]

                        val_t = dsl.b_iz(S, p_g)
                        r_n = val_t.index(color) if color in val_t else None
                        if r_n is not None:
                            m_dict[key] = f'b_iz_n(S, p_g, F{r_n})'
                        elif random.random() < budget_random:
                            budget_random /= 2
                            m_dict[key] = random.choice(list(COLORS.keys()))

                        val_t = dsl.b_zo(S, p_g)
                        r_n = val_t.index(color) if color in val_t else None
                        if r_n is not None:
                            m_dict[key] = f'b_zo_n(S, p_g, F{r_n})'
                        elif random.random() < budget_random:
                            budget_random /= 2
                            m_dict[key] = random.choice(list(COLORS.keys()))

                    # NOTE We need to add some sorting bits in here, as we can't directly index objects
                    #      See comments near f_iz
                    elif value == 'Object' and m_dict[key] in FL_NAMES.keys():
                        # Get number corresponding to F_ constant
                        obj_num = FL_NAMES[m_dict[key]]
                        # Get name corresponding to number (in case we substitute)
                        rank_list = list(FL_NAMES.keys())
                        m_dict[key] = rank_list[obj_num]

                        obj_diff = dsl.f_iz(S, ottt_g)
                        sorted_obj_diff = sorted(container, key=size, reverse=True)
                        f_n = sorted_obj_diff.index(obj_num) if obj_num in sorted_obj_diff else None
                        if f_n is not None:
                            m_dict[key] = f'f_iz_n(S, ottt_g, size, F{f_n})'

                        obj_diff = dsl.f_zo(S, ottt_g)
                        sorted_obj_diff = sorted(container, key=size, reverse=True)
                        f_n = sorted_obj_diff.index(obj_num) if obj_num in sorted_obj_diff else None
                        if f_n is not None:
                            m_dict[key] = f'f_zo_n(S, ottt_g, size, F{f_n})'


                # Replace x_n values with function calls
                for m_var, m_val in m_dict.items():
                    # Add x_n as placeholder entry to x_dict
                    if m_var == 'n1':
                        x_dict[m_val] = m_val

                    # Dereference x_n variables when we can
                    if m_val in x_dict:
                        m_dict[m_var] = x_dict[m_val]


                # print_l(f'{sig_list[i] = }')
                # print_l(f'{m_dict = }')
                # print_l(f'{x_dict = }')

                # Rebuild current line as single call
                x_dict[m_dict['n1']] = sig_list[i].format(**m_dict)

                # print_l(f"{x_dict[m_dict['n1']] = }")

                # if x_dict[m_dict['n1']] == 'x2(fill(fill(I, b_zo_n(S, p_g, F0), shoot(astuple(decrement(decrement(height_t(I))), ONE), UP_RIGHT)), b_zo_n(S, p_g, F1), shoot(astuple(decrement(height_t(I)), ONE), RIGHT)))':
                #     print_l("Here!")

                # if re.match(r'^x\d+$', x_dict[m_dict['n1']]) or re.match(r'^O$', x_dict[m_dict['n1']]):
                #     print_l(f"Warning: x_n or O in {x_dict[m_dict['n1']]} for {task_id} - {line.lstrip()}")

                # Add to dict of runtime values
                try:
                    # cand_dict[x_dict[m_dict['n1']]] = exec_var_dict[j][m_dict['n1']]
                    cand_set.add(x_dict[m_dict['n1']])
                except KeyError as e:
                    show_exception(f"KeyError in cand_dict for {task_id}", e)

                # Make 'No match found' message below work
                break
            else:
                # print_l(f'Retry match: {line.lstrip()}')
                pattern = re.compile(
                    r"""
                    ^\s*(?P<n1>\w+)\s*=\s*  # Variable name
                    (?P<n2>.*\))\s*$        # Everything until last parenthesis
                    """,
                    re.VERBOSE
                )

                if match := re.match(pattern, line):
                    m = match.groupdict()

                    # Replace x_n values with function calls
                    for m_var, m_val in m.items():
                        # Add x_n as placeholder entry to x_dict
                        if m_var == 'n1':
                            x_dict[m_val] = m_val

                        # Dereference x_n variables when we can
                        if m_val in x_dict:
                            m[m_var] = x_dict[m_val]

                        # Rebuild current line as single call
                        x_dict[m['n1']] = m['n2']

                    # if m['n2'] == 'x2(fill(fill(I, b_zo_n(S, p_g, F0), shoot(astuple(decrement(decrement(height_t(I))), ONE), UP_RIGHT)), b_zo_n(S, p_g, F1), shoot(astuple(decrement(height_t(I)), ONE), RIGHT)))':
                    #     print_l("Here!")

                    # Add to dict of runtime values
                    try:
                        # cand_dict[x_dict[m['n1']]] = exec_var_dict[j][m['n1']]
                        cand_set.add(x_dict[m['n1']])
                    except KeyError as e:
                        show_exception(f"KeyError in cand_dict for {task_id}", e)
                else:
                    print_l(f'No match found for line: {line.lstrip()}')

        todo_set |= cand_set

    return todo_set


def check_done(task, task_id, cand_dict, call_score_dict, dist_score_dict, \
        pass_dict, hint, izzo):
    """ check that the task is solved and look for constraints """

    hint_sig = re.sub(r'\bI\b', '{n3}', hint)

    if hint in MONITORING_HINTS:
        print_l(f'{hint_sig = }')

    # NOTE Enable print for given hint(s) only
    if hint in ['shape(I)', 'width(I)', 'height(I)']:
        do_print = False
    else:
        do_print = False

    # NOTE Careful about test sample output leaks
    hint_I = hint_sig.format(n3='I')
    hint_O = hint_sig.format(n3='O')

    solved = True
    val_pass = None
    all_pass = True
    for i, sample in enumerate(task):
        if task_id not in cand_dict.keys():
            cand_dict[task_id] = {}

        if i not in cand_dict[task_id].keys():
            cand_dict[task_id][i] = {}

        cand_dict[task_id][i]['I'] = sample['input']
        cand_dict[task_id][i]['O'] = sample['output']

        exec_var_dict = {
            'S': tuple((tuple(sample['input']), tuple(sample['output'])) for sample in task),
            'I': sample['input'], 
            'O': sample['output'],
            'cand_dict': cand_dict,
        }

        get_cache(task_id, i, hint_I, exec_var_dict)
        get_cache(task_id, i, hint_O, exec_var_dict)

        Y_k, Y_v = compare_cache(cand_dict[task_id][i], hint_I, hint_O, izzo)

        # Check that hint passes all samples
        # First, check that comparison is valid and result not empty
        if Y_k is None or Y_v == frozenset() or Y_v == tuple():

            if hint in MONITORING_HINTS:
                print_l(f'{Y_k = } - {Y_v = } - {izzo = }')

            all_pass = False
        else:
            # Initial setup for val_pass
            if val_pass is None:
                val_pass = Y_v
            else:
                if val_pass != Y_v:
                    # Keep the common part of the sets, if any, else fail
                    if type(val_pass) == type(Y_v) == frozenset:
                        val_pass = intersection(val_pass, Y_v)
                        if val_pass == frozenset():
                            all_pass = False
                    elif type(val_pass) == type(Y_v) == tuple:
                        val_pass = and_tuple(val_pass, Y_v)
                        if val_pass == tuple():
                            all_pass = False
                    else:
                        assert(f"Unknown type: {type(val_pass)}")

            # if hint == 'palette(I)':
            #     print_l(f'{izzo = } - {Y_k = } - {Y_v = } - {val_pass = }')
            #     if hint in call_score_dict.keys():
            #         print_l(f'{hint = } - {call_score_dict[hint] = }')
            #     if Y_k in dist_score_dict[task_id]:
            #         print_l(f'{Y_k = } - {dist_score_dict[task_id][Y_k] = }')

        # Solve for this (usually)
        if sample['output'] != cand_dict[task_id][i][hint_I]:
            if hint in MONITORING_HINTS:
                print(f'{cand_dict[task_id][i][hint_I]}')
                print(f'{sample["output"]}')
            solved = False

    if all_pass and val_pass is not None:
        # Check that hint is usable
        if Y_k is not None and val_pass != frozenset() and val_pass != tuple():
            Y_k is not None and do_print and print_l(f'{Y_k = } - {val_pass = } - {izzo = }')

            if task_id not in pass_dict.keys():
                pass_dict[task_id] = {}

            # Check that val_pass is not already in pass_dict[task_id]
            if val_pass not in pass_dict[task_id].values():
                pass_dict[task_id][Y_k] = val_pass
                dist_score_dict[task_id][Y_k] = val_pass

    if solved:
        do_print and print_l(f"- {task_id} - {hint} - {izzo} - check_done")
        
        # Main solver function
        solver_code = f"def solve_{task_id}(S, I):\n    return {hint_I}\n"
                
        return True, [solver_code]

    # Not solved
    return False, []


def issubsequence(t1, t2):
    n, m = len(t1), len(t2)
    for i in range(m - n + 1):
        if t2[i:i+n] == t1:
            return True
    return False


def check_hint(task, task_id, cand_dict, call_score_dict, dist_score_dict, \
        pass_dict, hint, step):
    """ check if previous constraints have relaxed """

    hint_sig = re.sub(r'\bI\b', '{n3}', hint)

    # NOTE Enable print for given hint(s) only
    if hint in ['shape(I)', 'width(I)', 'height(I)']:
        do_print = False
    else:
        do_print = False

    # NOTE Careful about test sample output leaks
    hint_I = hint_sig.format(n3='I')
    hint_O = hint_sig.format(n3='O')

    if task_id not in pass_dict.keys():
        pass_dict[task_id] = {}

    got_closer = False
    start_from = None
    can_use = 0
    hint_count = 0
    for hint_k, hint_v in pass_dict[task_id].items():
        # print_l(f'{hint_k = } - {hint_v = }')
        hint_count += 1
        # Only check the first hints while experimenting
        # NOTE Maybe compute and use hint_k call_score
        #      Or limit this to segmenting functions
        if hint_count > 4000:
            print_l('Tried too many hints')
            break

        # Check that this can be a hint at all
        if not got_id_str_in(hint_k, 'I'):
            continue

        val_pass = None
        all_pass = True
        for i, sample in enumerate(task):
            if task_id not in cand_dict.keys():
                cand_dict[task_id] = {}

            if i not in cand_dict[task_id].keys():
                cand_dict[task_id][i] = {}

            cand_dict[task_id][i]['I'] = sample['input']
            cand_dict[task_id][i]['O'] = sample['output']

            exec_var_dict = {
                'S': tuple((tuple(sample['input']), tuple(sample['output'])) for sample in task),
                'I': sample['input'], 
                'O': sample['output'],
                'cand_dict': cand_dict,
            }

            hint_Ik = re.sub(r'\bO\b', hint_I, hint_k)

            # Only compare palette for now
            if 'palette' not in hint_k:
                continue

            get_cache(task_id, i, hint_Ik, exec_var_dict)

            Y_k = hint_Ik
            Y_v = cand_dict[task_id][i][hint_Ik]

            # Check that hint passes all samples
            # NOTE Logic could use a cleanup
            if Y_v is None or Y_v == frozenset() or Y_v == tuple():
                all_pass = False
            else:
                if val_pass is None:
                    val_pass = Y_v
                else:
                    if val_pass != Y_v:
                        # Keep the common part of the sets, if any, else fail
                        if isinstance(val_pass, frozenset) and isinstance(Y_v, frozenset):
                            val_pass = intersection(val_pass, Y_v)
                            if val_pass == frozenset():
                                all_pass = False
                        elif isinstance(val_pass, tuple) and isinstance(Y_v, tuple):
                            val_pass = and_tuple(val_pass, Y_v)
                            if val_pass == tuple():
                                all_pass = False
                        else:
                            assert(f"Unknown type: {type(val_pass)}")

        
        if all_pass and val_pass is not None:
            Y_ks = hint_k

            if type(Y_v) == frozenset and val_pass.issubset(hint_v):
                if hint_k not in dist_score_dict[task_id]:
                    print_l(f'>- Not in dist_score_dict[task_id]:')
                    print_l(f'-> {hint_k = } - {val_pass = }')
                    dist_score_dict[task_id][hint_k] = val_pass
                elif len(val_pass) < len(dist_score_dict[task_id][hint_k]):
                    # We got closer to solution
                    got_closer = True
                    start_from = hint
                    # print_l(f'>- Got closer with {hint}:')
                    # print_l(f'-> {hint_k = } - {val_pass = }')
                    # dist_score_dict[task_id][hint_k] = val_pass
            elif type(Y_v) == tuple and issubsequence(val_pass, hint_v):
                if hint_k not in dist_score_dict[task_id]:
                    print_l(f'>- Not in dist_score_dict[task_id]:')
                    print_l(f'-> {hint_k = } - {val_pass = }')
                    dist_score_dict[task_id][hint_k] = val_pass
                elif len(val_pass) < len(dist_score_dict[task_id][hint_k]):
                    # We got closer to solution
                    got_closer = True
                    start_from = hint
                    # print_l(f'>- Got closer with {hint}:')
                    # print_l(f'-> {hint_k = } - {val_pass = }')
                    # dist_score_dict[task_id][hint_k] = val_pass

    if can_use > 20:
        with open('solvers_gen.py', 'a') as f:
            f.write(f"# {can_use = } - {step = } - {task_id = } - {hint = }\n")
        with open('solvers_gen.out', 'a') as f:
            f.write(f"{can_use} - {hint = }\n")

        print_l(f'{can_use = } - {step = } - {task_id = } - {hint = }')
    
    return got_closer, start_from


def compare_cache(task_cand_dict, hint_I, hint_O, izzo):
    """
    Might need a good cleanup
    TODO Check and remove dead code
    """
    if hint_I not in task_cand_dict.keys():
        return None, None
    elif hint_O not in task_cand_dict.keys():
        return None, None
    elif type(task_cand_dict[hint_I]) in [type(None), types.FunctionType]:
        return None, None
    elif type(task_cand_dict[hint_O]) in [type(None), types.FunctionType]:
        return None, None
    elif type(task_cand_dict[hint_I]) == type(task_cand_dict[hint_O]) == bool:
        return None, None
    elif type(task_cand_dict[hint_I]) == type(task_cand_dict[hint_O]) == int:
        return None, None
    elif izzo == 'iz':
        return f"difference({hint_I}, {hint_O})", \
                difference(task_cand_dict[hint_I], task_cand_dict[hint_O])
    elif izzo == 'zo':
        return f"difference({hint_O}, {hint_I})", \
                difference(task_cand_dict[hint_O], task_cand_dict[hint_I])


# Now modify the get_cache function to properly find the helper functions
def get_cache(task_id, i, hint, exec_var_dict):
    """Execute a hint and cache its result for a specific task and sample"""
    
    # Validate inputs to avoid cryptic errors
    if not isinstance(task_id, str) or not isinstance(i, int) or not isinstance(hint, str):
        print_l(f"Invalid inputs to get_cache: task_id={type(task_id)}, i={type(i)}, hint={type(hint)}")
        return False
    
    # Avoid problematic hints that might crash the script
    if 'import' in hint.lower() or '__' in hint:
        print_l(f"Potentially unsafe hint rejected: {hint}")
        return False
    
    # Prepare the execution statements
    cache_hint_line = f"cand_dict['{task_id}'][{i}]['{hint}'] = {hint}"
    clean_hint_line = f"cand_dict['{task_id}'][{i}]['{hint}'] = None"
    
    # Import ALL DSL functions recursively from all submodules
    # First, add direct attributes from dsl_modules
    for attr_name in dir(dsl):
        if not attr_name.startswith('__'):
            exec_var_dict[attr_name] = getattr(dsl, attr_name)
    
    # # Then, recursively check for submodules and add their functions
    # for attr_name in dir(dsl):
    #     if not attr_name.startswith('__'):
    #         attr = getattr(dsl, attr_name)
    #         if isinstance(attr, types.ModuleType):
    #             print_l(f"Adding DSL attribute: {attr_name}")
    #             # This is a submodule
    #             for func_name in dir(attr):
    #                 if not func_name.startswith('__'):
    #                     exec_var_dict[func_name] = getattr(attr, func_name)
    
    # # Add special functions if they exist
    # special_funcs = ['b_iz_n', 'b_zo_n', 'p']
    # for func_name in special_funcs:
    #     if func_name in globals():
    #         exec_var_dict[func_name] = globals()[func_name]


    # We only need solvers from solvers_evo because they 
    # are used in s_iz, s_zo and related calls
    for func in dir(solvers_evo):
        if func.startswith('solve_'):
            # Add all solvers to the execution dictionary
            exec_var_dict[func] = getattr(solvers_evo, func)

    # Add constants
    for constant_name in ALL_CONSTANT_NAMES:
        if constant_name in globals():
            exec_var_dict[constant_name] = globals()[constant_name]

    try:
        exec(cache_hint_line, None, exec_var_dict)
    except TypeError as e:
        # Put None in the cache, so we can continue
        if len(cache_hint_line) < 99:
            print_l(f'- Exception! - {cache_hint_line}')
            show_exception('- exec fail', e)
        exec(clean_hint_line, None, exec_var_dict)
    except (AttributeError, 
            IndexError, 
            RuntimeError,
            StopIteration, 
            ValueError, 
            ZeroDivisionError) as e:
        # Put None in the cache, so we can continue
        # if len(cache_hint_line) < 99:
        # print_l(f'- Exception! - {cache_hint_line}')
        # show_exception(f"- exec fail", e)
        exec(clean_hint_line, None, exec_var_dict)
    except Exception as e:
        print_l(f"- Exception! - {task_id = }")
        print_l(f"- cache_hint_line: {cache_hint_line}")
        show_exception('- exec fail', e)
        print_l(f"- traceback: {traceback.format_exc()}")


def load_evaluation_task_ids():
    """Load the set of task IDs from the evaluation dataset."""
    eval_task_ids = set()
    try:
        eval_data = get_data(train=False)  # Load evaluation dataset
        for task_id in eval_data['train'].keys():
            eval_task_ids.add(task_id)
    except Exception as e:
        print(f"Warning: Could not load evaluation dataset: {e}")
    
    return eval_task_ids

# Load evaluation task IDs once at startup
EVALUATION_TASK_IDS = load_evaluation_task_ids()
MONITORING_TASK_IDS = {
#     'ba97ae07'
}
MONITORING_HINTS = {
    # 'fill(I, get_common_rank_t(apply(color, totuple(o_g(I, R5))), F0), backdrop(f_ofcolor(I, get_common_rank_t(apply(color, totuple(o_g(I, R5))), F0))))'
}
# Solvers in solvers_pre.py that don't work
BAD_SOLVERS = {
    '27a28665',
    '29623171',
    '39a8645d',
    '50846271',
    '6455b5f5',
    '6855a6e4',
    '88a62173',
    '9af7a82c',
    '9f236235',
    'a3325580',
    'a64e4611',
    'a87f7484',
    'b230c067',
    'ba97ae07',
    'c8cbb738',
    'd6ad076f',
    'e40b9e2f',
    'a65b410d', # Gets closer, but no solve
    '6773b310', # Gets closer, but no solve
    'ef135b50', # Gets closer, but no solve
    '6a1e5592', # Gets closer, but no solve
    'a8d7556c', # Gets closer, but no solve
    'e26a3af2', # Seems to hang
} 


def main(task_id=None):
    """Main function that runs the solver builder.
    
    Args:
        task_id: Optional task ID to focus on. If None, a random task will be selected.
    """
    train_data = get_data(train=True)
    eval_data = get_data(train=False)

    # Group 'train' and 'eval' data, each task has 'train' and 'test' samples
    total_data = {}
    for k in train_data.keys():
        total_data[k] = {**train_data[k], **eval_data[k]}

    if task_id is None:
        if in_dev():
            # Train data
            task_list = list(train_data['train'].keys())
            # Evaluation data
            # task_list = list(eval_data['train'].keys())
        else:
            # Total data
            task_list = list(total_data['train'].keys())

        # Exclude known bad solvers
        bad_solvers = []
        task_list = [task_id for task_id in task_list if task_id not in bad_solvers]

        task_sizes = []
        for task_id in task_list:
        # for task_id in ['44f52bb0']:
            size = 0
            for S in total_data['train'][task_id] + total_data['test'][task_id]:
                for ex in S.values():
                    size += sum(len(inner) for inner in ex)
            task_sizes.append(size)

        weighted_tasks = list(zip(task_list, task_sizes))
        inverse_weights = [1/size for _, size in weighted_tasks]

        while True:
            task_id = random.choices(
                [t_id for t_id, _ in weighted_tasks],
                weights=inverse_weights,
                k=1
            )[0]

            # Skip tasks with existing solver most of the time
            if os.path.exists(f'solver_evo/solve_{task_id}.def'):
                # Sometimes try to improve existing solver
                if random.random() < 0.9:
                    continue
            
            break

    task_id_list = [task_id]
    # https://kts.github.io/arc-viewer/page4/#ea32f347
    # task_id_list = ['ea32f347'] # test feature size and rank (near task 2)

    # Solvers using palette
    # task_id_list = ['0e206a2e']
    # task_id_list = ['1e32b0e9']
    # task_id_list = ['22168020']
    # task_id_list = ['68b16354'] # test hmirror
    # task_id_list = ['ea32f347', 'c8f0f002', 'b1948b0a'] # test replace
    # task_id_list = ['b1948b0a'] # test generate constant
    # task_id_list = ['ea32f347'] # test relax constraint
    # task_id_list = ['c444b776'] # last 10-step solver
    # task_id_list = ['760b3cac'] # last 10-step solver but one
    # task_id_list = ['2c608aff'] # last 9-step solver
    # task_id_list = ['d90796e8'] # last 9-step solver but one
    # task_id_list = ['28bf18c6'] # 2nd 4-step solver
    # task_id_list = ['253bf280'] # partial solving in check_done
    # task_id_list = ['d631b094'] # inject s_iz call insted of ZERO
    # task_id_list = ['f76d97a5'] # task with palette
    # task_id_list = ['d9fac9be'] # task with palette and size change
    # task_id_list = ['b6afb2da'] # test helper
    # task_id_list = ['0ca9ddb6'] # check izzo

    # NOTE Max attempt only taken into account when task_id_list is empty
    max_attempt = 4000
    solver_dict = build_solver_dict(total_data, max_attempt, task_id_list)


if __name__ == '__main__':
    import sys
    
    # Check if a task_id was provided as a command-line argument
    if len(sys.argv) > 1:
        task_id = sys.argv[1]
        main(task_id)
    else:
        main()  # Run with a random task ID
    # main()
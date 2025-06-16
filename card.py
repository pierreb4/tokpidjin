from utils import *


# Combine all solvers in solver_evo into a single one

# Outline with examples:

# 1. Read all source files in the solver_evo directory
"""
def solve_f25fbde4(S, I):
    x1 = o_g(I, R7)
    x2 = get_nth_f(x1, F0)
    x3 = subgrid(x2, I)
    O = upscale_t(x3, TWO)
    return O

def solve_a740d043(S, I):
    x1 = o_g(I, R7)
    x2 = merge_f(x1)
    x3 = subgrid(x2, I)
    O = replace(x3, ONE, ZERO)
    return O

# 2. Rename all variables to avoid conflicts
def solve_f25fbde4(S, I):
    t[0] = x1 = o_g(I, R7)
idx['x1']['f25fbde4'] = 0

def solve_a740d043(S, I):
    t[0] = x1 = o_g(I, R7)
idx['x1']['solve_a740d043'] = 0
next_idx = 1

def solve_f25fbde4(S, I):
    t[0] = x1 = o_g(I, R7)
    t[1] = x2 = get_nth_f(t[0], F0)
idx['x2']['f25fbde4'] = 1

def solve_a740d043(S, I):
    t[0] = x1 = o_g(I, R7)
    t[2] = x2 = merge_f(t[0])
idx['x2']['solve_a740d043'] = 2
next_idx = 3

def solve_f25fbde4(S, I):
    t[0] = x1 = o_g(I, R7)
    t[1] = x2 = get_nth_f(t[0], F0)
    t[3] = x3 = subgrid(t[1], I)
idx['x3']['f25fbde4'] = 3

def solve_a740d043(S, I):
    t[0] = x1 = o_g(I, R7)
    t[2] = x2 = merge_f(t[0])
    t[4] = x3 = subgrid(t[2], I)
idx['x3']['solve_a740d043'] = 4
next_idx = 5

def solve_f25fbde4(S, I):
    t[0] = x1 = o_g(I, R7)
    t[1] = x2 = get_nth_f(t[0], F0)
    t[3] = x3 = subgrid(t[1], I)
    t[5] = O = upscale_t(t[3], TWO)
    O -> check_done(t[5])

def solve_a740d043(S, I):
    t[0] = x1 = o_g(I, R7)
    t[2] = x2 = merge_f(t[0])
    t[4] = x3 = subgrid(t[2], I)
    t[6] = O = replace(t[4], ONE, ZERO)
    O -> check_done(t[6])
"""

# 3. Output a single file, batt.py


def get_equals(solver):
    # Catalog assignments in solvers
    equals = {}
    for line in solver.split('\n'):
        if ' = ' in line:
            parts = line.split('=')
            var_name = parts[0].strip()
            value = parts[1].strip()
            equals[var_name] = value
    return equals


def main():
    solvers = get_solvers()
    print_l(solvers.keys())

    print(solvers['73182012'])

    equals = {}
    for task_id, source in solvers.items():
        equals[task_id] = get_equals(source)
    
    print_l(f"{get_equals(solvers['73182012']) = }")

    count = 2
    t_num = 0
    t_call = {}
    t_name = {}
    while count > 0:
        count -= 1

        # Print the next entry, if any, of each solver
        sub_count = 20
        for task_id, source in solvers.items():
            sub_count -= 1
            if sub_count <= 0:
                break
            if not equals[task_id]:
                continue
            x_name, x_call = next(iter(equals[task_id].items()))


            if x_call not in t_name.keys():
                t_k = f't{t_num}'
                t_call[t_k] = x_call
                t_name[x_call] = t_k
                t_num += 1

                print_l(f"{task_id}: {x_name} = {x_call}")
                print_l(f"{task_id}: {t_k} = {t_call[t_k]}")

                # Print new source code
                t_source = f"{t_k} = {t_call[t_k]}\n"
                print_l(t_source)

            # Replace x variable names with new t variable name
            for replace_task_id, replace_source in solvers.items():
                # Just check the firsst assignment
                r_equal = equals[replace_task_id].popitem()
                if r_equal is None:
                    break

                r_x_name, r_x_code = r_equal
                if r_x_code in t_name.keys():
                    if r_x_name == 'O':
                        print_l('check_done(t_name)')
                    else:
                        # Replace r_x_code with t_name[r_x_code]
                        r_equal[r_x_name] = t_name[r_x_code]
                        del equals[replace_task_id][r_x_name]

                        # Replace r_x_name with t_name[r_x_code]
                        # in the rest of the solver
                        # NOTE Also deal with possible cascading replacements
                        replace_source = replace_source.replace(r_x_code, t_name[r_x_code])



if __name__ == "__main__":
    main()
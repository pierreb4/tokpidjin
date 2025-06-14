def solve_0b148d64_one(S, I):
    return subgrid(get_arg_rank_f(partition(I), size, L1), I)


def solve_0b148d64(S, I, x=0):
    x1 = partition(I)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, L1)
    if x == 2:
        return x2
    O = subgrid(x2, I)
    return O

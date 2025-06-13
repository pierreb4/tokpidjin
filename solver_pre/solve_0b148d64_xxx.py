def solve_0b148d64_one(S, I):
    return subgrid(get_arg_rank_f(partition(I), size, L1), I)


def solve_0b148d64(S, I):
    x1 = partition(I)
    x2 = get_arg_rank_f(x1, size, L1)
    O = subgrid(x2, I)
    return O

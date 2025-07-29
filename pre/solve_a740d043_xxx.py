def solve_a740d043_one(S, I):
    return replace(subgrid(merge_f(o_g(I, R7)), I), ONE, ZERO)


def solve_a740d043(S, I):
    x1 = o_g(I, R7)
    x2 = merge_f(x1)
    x3 = subgrid(x2, I)
    O = replace(x3, ONE, ZERO)
    return O

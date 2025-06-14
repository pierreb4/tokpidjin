def solve_a740d043_one(S, I):
    return replace(subgrid(merge_f(o_g(I, R7)), I), ONE, ZERO)


def solve_a740d043(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    O = replace(x3, ONE, ZERO)
    return O

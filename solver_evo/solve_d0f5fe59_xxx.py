def solve_d0f5fe59_one(S, I):
    return fill(canvas(BLACK, astuple(size_f(o_g(I, R5)), size_f(o_g(I, R5)))), CYAN, shoot(ORIGIN, UNITY))


def solve_d0f5fe59(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = size_f(x1)
    if x == 2:
        return x2
    x3 = astuple(x2, x2)
    if x == 3:
        return x3
    x4 = canvas(BLACK, x3)
    if x == 4:
        return x4
    x5 = shoot(ORIGIN, UNITY)
    if x == 5:
        return x5
    O = fill(x4, CYAN, x5)
    return O

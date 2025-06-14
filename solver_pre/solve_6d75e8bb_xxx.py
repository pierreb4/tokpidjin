def solve_6d75e8bb_one(S, I):
    return paint(I, shift(asobject(replace(subgrid(get_nth_f(o_g(I, R5), F0), I), ZERO, TWO)), corner(get_nth_f(o_g(I, R5), F0), R0)))


def solve_6d75e8bb(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = replace(x3, ZERO, TWO)
    if x == 4:
        return x4
    x5 = asobject(x4)
    if x == 5:
        return x5
    x6 = corner(x2, R0)
    if x == 6:
        return x6
    x7 = shift(x5, x6)
    if x == 7:
        return x7
    O = paint(I, x7)
    return O

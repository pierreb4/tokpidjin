def solve_6d75e8bb_one(S, I):
    return paint(I, shift(asobject(replace(subgrid(get_nth_f(o_g(I, R5), F0), I), ZERO, TWO)), corner(get_nth_f(o_g(I, R5), F0), R0)))


def solve_6d75e8bb(S, I):
    x1 = o_g(I, R5)
    x2 = get_nth_f(x1, F0)
    x3 = subgrid(x2, I)
    x4 = replace(x3, ZERO, TWO)
    x5 = asobject(x4)
    x6 = corner(x2, R0)
    x7 = shift(x5, x6)
    O = paint(I, x7)
    return O

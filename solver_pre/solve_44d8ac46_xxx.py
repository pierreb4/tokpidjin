def solve_44d8ac46_one(S, I):
    return fill(I, TWO, mfilter_f(apply(delta, o_g(I, R5)), square_f))


def solve_44d8ac46(S, I):
    x1 = o_g(I, R5)
    x2 = apply(delta, x1)
    x3 = mfilter_f(x2, square_f)
    O = fill(I, TWO, x3)
    return O

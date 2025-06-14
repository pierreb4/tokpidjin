def solve_44d8ac46_one(S, I):
    return fill(I, TWO, mfilter_f(apply(delta, o_g(I, R5)), square_f))


def solve_44d8ac46(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = apply(delta, x1)
    if x == 2:
        return x2
    x3 = mfilter_f(x2, square_f)
    if x == 3:
        return x3
    O = fill(I, TWO, x3)
    return O

def solve_50cb2852_one(S, I):
    return fill(I, EIGHT, mapply(compose(backdrop, inbox), o_g(I, R5)))


def solve_50cb2852(S, I):
    x1 = compose(backdrop, inbox)
    x2 = o_g(I, R5)
    x3 = mapply(x1, x2)
    O = fill(I, EIGHT, x3)
    return O

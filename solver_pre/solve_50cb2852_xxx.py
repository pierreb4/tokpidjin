def solve_50cb2852_one(S, I):
    return fill(I, EIGHT, mapply(compose(backdrop, inbox), o_g(I, R5)))


def solve_50cb2852(S, I, x=0):
    x1 = compose(backdrop, inbox)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = mapply(x1, x2)
    if x == 3:
        return x3
    O = fill(I, EIGHT, x3)
    return O

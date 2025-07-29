def solve_54d9e175_one(S, I):
    return replace(replace(replace(replace(paint(I, mapply(fork(recolor_i, color, compose(neighbors, center)), sizefilter(o_g(I, R5), ONE))), ONE, SIX), TWO, SEVEN), THREE, EIGHT), FOUR, NINE)


def solve_54d9e175(S, I):
    x1 = compose(neighbors, center)
    x2 = fork(recolor_i, color, x1)
    x3 = o_g(I, R5)
    x4 = sizefilter(x3, ONE)
    x5 = mapply(x2, x4)
    x6 = paint(I, x5)
    x7 = replace(x6, ONE, SIX)
    x8 = replace(x7, TWO, SEVEN)
    x9 = replace(x8, THREE, EIGHT)
    O = replace(x9, FOUR, NINE)
    return O

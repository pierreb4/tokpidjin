def solve_54d9e175_one(S, I):
    return replace(replace(replace(replace(paint(I, mapply(fork(recolor_i, color, compose(neighbors, center)), sizefilter(o_g(I, R5), ONE))), ONE, SIX), TWO, SEVEN), THREE, EIGHT), FOUR, NINE)


def solve_54d9e175(S, I, x=0):
    x1 = compose(neighbors, center)
    if x == 1:
        return x1
    x2 = fork(recolor_i, color, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = sizefilter(x3, ONE)
    if x == 4:
        return x4
    x5 = mapply(x2, x4)
    if x == 5:
        return x5
    x6 = paint(I, x5)
    if x == 6:
        return x6
    x7 = replace(x6, ONE, SIX)
    if x == 7:
        return x7
    x8 = replace(x7, TWO, SEVEN)
    if x == 8:
        return x8
    x9 = replace(x8, THREE, EIGHT)
    if x == 9:
        return x9
    O = replace(x9, FOUR, NINE)
    return O

def solve_6773b310_one(S, I):
    return downscale(replace(fill(compress(I), ONE, mfilter(apply(rbind(toobject, compress(I)), apply(fork(insert, identity, neighbors), shift(apply(rbind(multiply, THREE), insert(ORIGIN, neighbors(ORIGIN))), astuple(FOUR, FOUR)))), matcher(rbind(colorcount_f, SIX), TWO))), SIX, ZERO), THREE)


def solve_6773b310(S, I):
    x1 = compress(I)
    x2 = rbind(toobject, x1)
    x3 = fork(insert, identity, neighbors)
    x4 = rbind(multiply, THREE)
    x5 = neighbors(ORIGIN)
    x6 = insert(ORIGIN, x5)
    x7 = apply(x4, x6)
    x8 = astuple(FOUR, FOUR)
    x9 = shift(x7, x8)
    x10 = apply(x3, x9)
    x11 = apply(x2, x10)
    x12 = rbind(colorcount_f, SIX)
    x13 = matcher(x12, TWO)
    x14 = mfilter(x11, x13)
    x15 = fill(x1, ONE, x14)
    x16 = replace(x15, SIX, ZERO)
    O = downscale(x16, THREE)
    return O

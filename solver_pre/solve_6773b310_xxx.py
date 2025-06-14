def solve_6773b310_one(S, I):
    return downscale(replace(fill(compress(I), ONE, mfilter(apply(rbind(toobject, compress(I)), apply(fork(insert, identity, neighbors), shift(apply(rbind(multiply, THREE), insert(ORIGIN, neighbors(ORIGIN))), astuple(FOUR, FOUR)))), matcher(rbind(colorcount_f, SIX), TWO))), SIX, ZERO), THREE)


def solve_6773b310(S, I, x=0):
    x1 = compress(I)
    if x == 1:
        return x1
    x2 = rbind(toobject, x1)
    if x == 2:
        return x2
    x3 = fork(insert, identity, neighbors)
    if x == 3:
        return x3
    x4 = rbind(multiply, THREE)
    if x == 4:
        return x4
    x5 = neighbors(ORIGIN)
    if x == 5:
        return x5
    x6 = insert(ORIGIN, x5)
    if x == 6:
        return x6
    x7 = apply(x4, x6)
    if x == 7:
        return x7
    x8 = astuple(FOUR, FOUR)
    if x == 8:
        return x8
    x9 = shift(x7, x8)
    if x == 9:
        return x9
    x10 = apply(x3, x9)
    if x == 10:
        return x10
    x11 = apply(x2, x10)
    if x == 11:
        return x11
    x12 = rbind(colorcount_f, SIX)
    if x == 12:
        return x12
    x13 = matcher(x12, TWO)
    if x == 13:
        return x13
    x14 = mfilter(x11, x13)
    if x == 14:
        return x14
    x15 = fill(x1, ONE, x14)
    if x == 15:
        return x15
    x16 = replace(x15, SIX, ZERO)
    if x == 16:
        return x16
    O = downscale(x16, THREE)
    return O

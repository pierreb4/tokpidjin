def solve_1fad071e_one(S, I):
    return hconcat(canvas(ONE, astuple(ONE, size_f(sizefilter(colorfilter(o_g(I, R5), ONE), FOUR)))), canvas(ZERO, astuple(ONE, subtract(FIVE, size_f(sizefilter(colorfilter(o_g(I, R5), ONE), FOUR))))))


def solve_1fad071e(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ONE)
    if x == 2:
        return x2
    x3 = sizefilter(x2, FOUR)
    if x == 3:
        return x3
    x4 = size_f(x3)
    if x == 4:
        return x4
    x5 = astuple(ONE, x4)
    if x == 5:
        return x5
    x6 = canvas(ONE, x5)
    if x == 6:
        return x6
    x7 = subtract(FIVE, x4)
    if x == 7:
        return x7
    x8 = astuple(ONE, x7)
    if x == 8:
        return x8
    x9 = canvas(ZERO, x8)
    if x == 9:
        return x9
    O = hconcat(x6, x9)
    return O

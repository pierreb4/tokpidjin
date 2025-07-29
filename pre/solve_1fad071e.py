def solve_1fad071e_one(S, I):
    return hconcat(canvas(ONE, astuple(ONE, size_f(sizefilter(colorfilter(o_g(I, R5), ONE), FOUR)))), canvas(ZERO, astuple(ONE, subtract(FIVE, size_f(sizefilter(colorfilter(o_g(I, R5), ONE), FOUR))))))


def solve_1fad071e(S, I):
    x1 = o_g(I, R5)
    x2 = colorfilter(x1, ONE)
    x3 = sizefilter(x2, FOUR)
    x4 = size_f(x3)
    x5 = astuple(ONE, x4)
    x6 = canvas(ONE, x5)
    x7 = subtract(FIVE, x4)
    x8 = astuple(ONE, x7)
    x9 = canvas(ZERO, x8)
    O = hconcat(x6, x9)
    return O

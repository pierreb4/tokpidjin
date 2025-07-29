def solve_a5f85a15_one(S, I):
    return fill(I, FOUR, mapply(lbind(shift, papply(astuple, apply(decrement, apply(double, interval(ONE, NINE, ONE))), apply(decrement, apply(double, interval(ONE, NINE, ONE))))), apply(rbind(corner, R0), o_g(I, R7))))


def solve_a5f85a15(S, I):
    x1 = interval(ONE, NINE, ONE)
    x2 = apply(double, x1)
    x3 = apply(decrement, x2)
    x4 = papply(astuple, x3, x3)
    x5 = lbind(shift, x4)
    x6 = rbind(corner, R0)
    x7 = o_g(I, R7)
    x8 = apply(x6, x7)
    x9 = mapply(x5, x8)
    O = fill(I, FOUR, x9)
    return O

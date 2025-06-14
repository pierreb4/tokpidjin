def solve_a5f85a15_one(S, I):
    return fill(I, YELLOW, mapply(lbind(shift, papply(astuple, apply(decrement, apply(double, interval(ONE, NINE, ONE))), apply(decrement, apply(double, interval(ONE, NINE, ONE))))), apply(rbind(corner, R0), o_g(I, R7))))


def solve_a5f85a15(S, I, x=0):
    x1 = interval(ONE, NINE, ONE)
    if x == 1:
        return x1
    x2 = apply(double, x1)
    if x == 2:
        return x2
    x3 = apply(decrement, x2)
    if x == 3:
        return x3
    x4 = papply(astuple, x3, x3)
    if x == 4:
        return x4
    x5 = lbind(shift, x4)
    if x == 5:
        return x5
    x6 = rbind(corner, R0)
    if x == 6:
        return x6
    x7 = o_g(I, R7)
    if x == 7:
        return x7
    x8 = apply(x6, x7)
    if x == 8:
        return x8
    x9 = mapply(x5, x8)
    if x == 9:
        return x9
    O = fill(I, YELLOW, x9)
    return O

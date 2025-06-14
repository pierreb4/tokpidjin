def solve_91413438_one(S, I):
    return merge_t(hsplit(paint(hconcat(I, canvas(ZERO, astuple(THREE, subtract(multiply(multiply(colorcount_t(I, ZERO), THREE), colorcount_t(I, ZERO)), THREE)))), mapply(compose(lbind(shift, get_nth_f(o_g(hconcat(I, canvas(ZERO, astuple(THREE, subtract(multiply(multiply(colorcount_t(I, ZERO), THREE), colorcount_t(I, ZERO)), THREE)))), R7), F0)), tojvec), apply(rbind(multiply, THREE), interval(ZERO, subtract(NINE, colorcount_t(I, ZERO)), ONE)))), colorcount_t(I, ZERO)))


def solve_91413438(S, I, x=0):
    x1 = colorcount_t(I, ZERO)
    if x == 1:
        return x1
    x2 = multiply(x1, THREE)
    if x == 2:
        return x2
    x3 = multiply(x2, x1)
    if x == 3:
        return x3
    x4 = subtract(x3, THREE)
    if x == 4:
        return x4
    x5 = astuple(THREE, x4)
    if x == 5:
        return x5
    x6 = canvas(ZERO, x5)
    if x == 6:
        return x6
    x7 = hconcat(I, x6)
    if x == 7:
        return x7
    x8 = o_g(x7, R7)
    if x == 8:
        return x8
    x9 = get_nth_f(x8, F0)
    if x == 9:
        return x9
    x10 = lbind(shift, x9)
    if x == 10:
        return x10
    x11 = compose(x10, tojvec)
    if x == 11:
        return x11
    x12 = rbind(multiply, THREE)
    if x == 12:
        return x12
    x13 = subtract(NINE, x1)
    if x == 13:
        return x13
    x14 = interval(ZERO, x13, ONE)
    if x == 14:
        return x14
    x15 = apply(x12, x14)
    if x == 15:
        return x15
    x16 = mapply(x11, x15)
    if x == 16:
        return x16
    x17 = paint(x7, x16)
    if x == 17:
        return x17
    x18 = hsplit(x17, x1)
    if x == 18:
        return x18
    O = merge_t(x18)
    return O

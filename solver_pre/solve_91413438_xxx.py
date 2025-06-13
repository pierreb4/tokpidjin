def solve_91413438_one(S, I):
    return merge_t(hsplit(paint(hconcat(I, canvas(ZERO, astuple(THREE, subtract(multiply(multiply(colorcount_t(I, ZERO), THREE), colorcount_t(I, ZERO)), THREE)))), mapply(compose(lbind(shift, get_nth_f(o_g(hconcat(I, canvas(ZERO, astuple(THREE, subtract(multiply(multiply(colorcount_t(I, ZERO), THREE), colorcount_t(I, ZERO)), THREE)))), R7), F0)), tojvec), apply(rbind(multiply, THREE), interval(ZERO, subtract(NINE, colorcount_t(I, ZERO)), ONE)))), colorcount_t(I, ZERO)))


def solve_91413438(S, I):
    x1 = colorcount_t(I, ZERO)
    x2 = multiply(x1, THREE)
    x3 = multiply(x2, x1)
    x4 = subtract(x3, THREE)
    x5 = astuple(THREE, x4)
    x6 = canvas(ZERO, x5)
    x7 = hconcat(I, x6)
    x8 = o_g(x7, R7)
    x9 = get_nth_f(x8, F0)
    x10 = lbind(shift, x9)
    x11 = compose(x10, tojvec)
    x12 = rbind(multiply, THREE)
    x13 = subtract(NINE, x1)
    x14 = interval(ZERO, x13, ONE)
    x15 = apply(x12, x14)
    x16 = mapply(x11, x15)
    x17 = paint(x7, x16)
    x18 = hsplit(x17, x1)
    O = merge_t(x18)
    return O

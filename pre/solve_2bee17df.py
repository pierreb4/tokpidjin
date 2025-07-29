def solve_2bee17df_one(S, I):
    return underfill(I, THREE, merge_t(astuple(mapply(hfrontier, sfilter_t(pair(interval(ZERO, height_t(I), ONE), compose(lbind(apply, matcher(rbind(colorcount_t, ZERO), subtract(height_t(I), TWO))), rbind(vsplit, height_t(I)))(I)), rbind(get_nth_f, L1))), mapply(vfrontier, sfilter_t(pair(compose(lbind(apply, matcher(rbind(colorcount_t, ZERO), subtract(height_t(I), TWO))), rbind(vsplit, height_t(I)))(mir_rot_t(I, R4)), interval(ZERO, height_t(I), ONE)), rbind(get_nth_f, F0))))))


def solve_2bee17df(S, I):
    x1 = height_t(I)
    x2 = interval(ZERO, x1, ONE)
    x3 = rbind(colorcount_t, ZERO)
    x4 = subtract(x1, TWO)
    x5 = matcher(x3, x4)
    x6 = lbind(apply, x5)
    x7 = rbind(vsplit, x1)
    x8 = compose(x6, x7)
    x9 = x8(I)
    x10 = pair(x2, x9)
    x11 = rbind(get_nth_f, L1)
    x12 = sfilter_t(x10, x11)
    x13 = mapply(hfrontier, x12)
    x14 = mir_rot_t(I, R4)
    x15 = x8(x14)
    x16 = pair(x15, x2)
    x17 = rbind(get_nth_f, F0)
    x18 = sfilter_t(x16, x17)
    x19 = mapply(vfrontier, x18)
    x20 = astuple(x13, x19)
    x21 = merge_t(x20)
    O = underfill(I, THREE, x21)
    return O

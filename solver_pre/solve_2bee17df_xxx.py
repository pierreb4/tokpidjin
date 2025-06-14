def solve_2bee17df_one(S, I):
    return underfill(I, THREE, merge_t(astuple(mapply(hfrontier, sfilter_t(pair(interval(ZERO, height_t(I), ONE), compose(lbind(apply, matcher(rbind(colorcount_t, ZERO), subtract(height_t(I), TWO))), rbind(vsplit, height_t(I)))(I)), rbind(get_nth_f, L1))), mapply(vfrontier, sfilter_t(pair(compose(lbind(apply, matcher(rbind(colorcount_t, ZERO), subtract(height_t(I), TWO))), rbind(vsplit, height_t(I)))(mir_rot_t(I, R4)), interval(ZERO, height_t(I), ONE)), rbind(get_nth_f, F0))))))


def solve_2bee17df(S, I, x=0):
    x1 = height_t(I)
    if x == 1:
        return x1
    x2 = interval(ZERO, x1, ONE)
    if x == 2:
        return x2
    x3 = rbind(colorcount_t, ZERO)
    if x == 3:
        return x3
    x4 = subtract(x1, TWO)
    if x == 4:
        return x4
    x5 = matcher(x3, x4)
    if x == 5:
        return x5
    x6 = lbind(apply, x5)
    if x == 6:
        return x6
    x7 = rbind(vsplit, x1)
    if x == 7:
        return x7
    x8 = compose(x6, x7)
    if x == 8:
        return x8
    x9 = x8(I)
    if x == 9:
        return x9
    x10 = pair(x2, x9)
    if x == 10:
        return x10
    x11 = rbind(get_nth_f, L1)
    if x == 11:
        return x11
    x12 = sfilter_t(x10, x11)
    if x == 12:
        return x12
    x13 = mapply(hfrontier, x12)
    if x == 13:
        return x13
    x14 = mir_rot_t(I, R4)
    if x == 14:
        return x14
    x15 = x8(x14)
    if x == 15:
        return x15
    x16 = pair(x15, x2)
    if x == 16:
        return x16
    x17 = rbind(get_nth_f, F0)
    if x == 17:
        return x17
    x18 = sfilter_t(x16, x17)
    if x == 18:
        return x18
    x19 = mapply(vfrontier, x18)
    if x == 19:
        return x19
    x20 = astuple(x13, x19)
    if x == 20:
        return x20
    x21 = merge_t(x20)
    if x == 21:
        return x21
    O = underfill(I, THREE, x21)
    return O

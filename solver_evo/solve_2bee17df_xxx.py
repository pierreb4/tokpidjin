def solve_2bee17df_one(S, I):
    return underfill(I, c_zo_n(identity(S), identity(p_g), identity(rbind(get_nth_t, F0))), merge_t(astuple(mapply(hfrontier, sfilter_t(pair(interval(ZERO, height_t(I), ONE), compose(lbind(apply, matcher(rbind(colorcount_t, BLACK), subtract(height_t(I), TWO))), rbind(vsplit, height_t(I)))(I)), rbind(get_nth_f, L1))), mapply(vfrontier, sfilter_t(pair(compose(lbind(apply, matcher(rbind(colorcount_t, BLACK), subtract(height_t(I), TWO))), rbind(vsplit, height_t(I)))(mir_rot_t(I, R4)), interval(ZERO, height_t(I), ONE)), rbind(get_nth_f, F0))))))


def solve_2bee17df(S, I, x=0):
    x1 = identity(S)
    if x == 1:
        return x1
    x2 = identity(p_g)
    if x == 2:
        return x2
    x3 = rbind(get_nth_t, F0)
    if x == 3:
        return x3
    x4 = identity(x3)
    if x == 4:
        return x4
    x5 = c_zo_n(x1, x2, x4)
    if x == 5:
        return x5
    x6 = height_t(I)
    if x == 6:
        return x6
    x7 = interval(ZERO, x6, ONE)
    if x == 7:
        return x7
    x8 = rbind(colorcount_t, BLACK)
    if x == 8:
        return x8
    x9 = subtract(x6, TWO)
    if x == 9:
        return x9
    x10 = matcher(x8, x9)
    if x == 10:
        return x10
    x11 = lbind(apply, x10)
    if x == 11:
        return x11
    x12 = rbind(vsplit, x6)
    if x == 12:
        return x12
    x13 = compose(x11, x12)
    if x == 13:
        return x13
    x14 = x13(I)
    if x == 14:
        return x14
    x15 = pair(x7, x14)
    if x == 15:
        return x15
    x16 = rbind(get_nth_f, L1)
    if x == 16:
        return x16
    x17 = sfilter_t(x15, x16)
    if x == 17:
        return x17
    x18 = mapply(hfrontier, x17)
    if x == 18:
        return x18
    x19 = mir_rot_t(I, R4)
    if x == 19:
        return x19
    x20 = x13(x19)
    if x == 20:
        return x20
    x21 = pair(x20, x7)
    if x == 21:
        return x21
    x22 = rbind(get_nth_f, F0)
    if x == 22:
        return x22
    x23 = sfilter_t(x21, x22)
    if x == 23:
        return x23
    x24 = mapply(vfrontier, x23)
    if x == 24:
        return x24
    x25 = astuple(x18, x24)
    if x == 25:
        return x25
    x26 = merge_t(x25)
    if x == 26:
        return x26
    O = underfill(I, x5, x26)
    return O

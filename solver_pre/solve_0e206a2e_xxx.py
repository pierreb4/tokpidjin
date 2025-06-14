def solve_0e206a2e_one(S, I):
    return cover(paint(I, mapply(fork(mapply, compose(lbind(lbind, shift), normalize), fork(apply, chain(compose(lbind(rbind, subtract), rbind(corner, R0)), rbind(sfilter, compose(rbind(contained, remove(get_arg_rank_f(remove(ZERO, palette_t(I)), lbind(colorcount_t, I), F0), remove(ZERO, palette_t(I)))), rbind(get_nth_f, F0))), normalize), chain(lbind(occurrences, I), rbind(sfilter, compose(rbind(contained, remove(get_arg_rank_f(remove(ZERO, palette_t(I)), lbind(colorcount_t, I), F0), remove(ZERO, palette_t(I)))), rbind(get_nth_f, F0))), normalize))), mapply(lbind(rapply, combine(combine(astuple(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1)), astuple(rbind(mir_rot_f, R0), rbind(mir_rot_f, R2))), totuple(apply(fork(compose, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), product(combine(astuple(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1)), astuple(rbind(mir_rot_f, R0), rbind(mir_rot_f, R2))), combine(astuple(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1)), astuple(rbind(mir_rot_f, R0), rbind(mir_rot_f, R2)))))))), sfilter(o_g(I, R1), compose(rbind(greater, ONE), numcolors_f))))), merge_f(sfilter(o_g(I, R1), compose(rbind(greater, ONE), numcolors_f))))


def solve_0e206a2e(S, I, x=0):
    x1 = lbind(lbind, shift)
    if x == 1:
        return x1
    x2 = compose(x1, normalize)
    if x == 2:
        return x2
    x3 = lbind(rbind, subtract)
    if x == 3:
        return x3
    x4 = rbind(corner, R0)
    if x == 4:
        return x4
    x5 = compose(x3, x4)
    if x == 5:
        return x5
    x6 = palette_t(I)
    if x == 6:
        return x6
    x7 = remove(ZERO, x6)
    if x == 7:
        return x7
    x8 = lbind(colorcount_t, I)
    if x == 8:
        return x8
    x9 = get_arg_rank_f(x7, x8, F0)
    if x == 9:
        return x9
    x10 = remove(x9, x7)
    if x == 10:
        return x10
    x11 = rbind(contained, x10)
    if x == 11:
        return x11
    x12 = rbind(get_nth_f, F0)
    if x == 12:
        return x12
    x13 = compose(x11, x12)
    if x == 13:
        return x13
    x14 = rbind(sfilter, x13)
    if x == 14:
        return x14
    x15 = chain(x5, x14, normalize)
    if x == 15:
        return x15
    x16 = lbind(occurrences, I)
    if x == 16:
        return x16
    x17 = chain(x16, x14, normalize)
    if x == 17:
        return x17
    x18 = fork(apply, x15, x17)
    if x == 18:
        return x18
    x19 = fork(mapply, x2, x18)
    if x == 19:
        return x19
    x20 = rbind(mir_rot_f, R3)
    if x == 20:
        return x20
    x21 = rbind(mir_rot_f, R1)
    if x == 21:
        return x21
    x22 = astuple(x20, x21)
    if x == 22:
        return x22
    x23 = rbind(mir_rot_f, R0)
    if x == 23:
        return x23
    x24 = rbind(mir_rot_f, R2)
    if x == 24:
        return x24
    x25 = astuple(x23, x24)
    if x == 25:
        return x25
    x26 = combine(x22, x25)
    if x == 26:
        return x26
    x27 = rbind(get_nth_f, L1)
    if x == 27:
        return x27
    x28 = fork(compose, x12, x27)
    if x == 28:
        return x28
    x29 = product(x26, x26)
    if x == 29:
        return x29
    x30 = apply(x28, x29)
    if x == 30:
        return x30
    x31 = totuple(x30)
    if x == 31:
        return x31
    x32 = combine(x26, x31)
    if x == 32:
        return x32
    x33 = lbind(rapply, x32)
    if x == 33:
        return x33
    x34 = o_g(I, R1)
    if x == 34:
        return x34
    x35 = rbind(greater, ONE)
    if x == 35:
        return x35
    x36 = compose(x35, numcolors_f)
    if x == 36:
        return x36
    x37 = sfilter(x34, x36)
    if x == 37:
        return x37
    x38 = mapply(x33, x37)
    if x == 38:
        return x38
    x39 = mapply(x19, x38)
    if x == 39:
        return x39
    x40 = paint(I, x39)
    if x == 40:
        return x40
    x41 = merge_f(x37)
    if x == 41:
        return x41
    O = cover(x40, x41)
    return O

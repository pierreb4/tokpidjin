def solve_36d67576_one(S, I):
    return paint(I, mapply(fork(mapply, compose(lbind(lbind, shift), normalize), fork(apply, chain(compose(lbind(rbind, subtract), rbind(corner, R0)), rbind(sfilter, compose(rbind(contained, astuple(TWO, FOUR)), rbind(get_nth_f, F0))), normalize), chain(lbind(occurrences, I), rbind(sfilter, compose(rbind(contained, astuple(TWO, FOUR)), rbind(get_nth_f, F0))), normalize))), rapply_t(combine(combine(astuple(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1)), astuple(rbind(mir_rot_f, R0), rbind(mir_rot_f, R2))), totuple(apply(fork(compose, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), product(combine(astuple(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1)), astuple(rbind(mir_rot_f, R0), rbind(mir_rot_f, R2))), combine(astuple(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1)), astuple(rbind(mir_rot_f, R0), rbind(mir_rot_f, R2))))))), get_arg_rank_f(o_g(I, R1), numcolors_f, F0))))


def solve_36d67576(S, I, x=0):
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
    x6 = astuple(TWO, FOUR)
    if x == 6:
        return x6
    x7 = rbind(contained, x6)
    if x == 7:
        return x7
    x8 = rbind(get_nth_f, F0)
    if x == 8:
        return x8
    x9 = compose(x7, x8)
    if x == 9:
        return x9
    x10 = rbind(sfilter, x9)
    if x == 10:
        return x10
    x11 = chain(x5, x10, normalize)
    if x == 11:
        return x11
    x12 = lbind(occurrences, I)
    if x == 12:
        return x12
    x13 = chain(x12, x10, normalize)
    if x == 13:
        return x13
    x14 = fork(apply, x11, x13)
    if x == 14:
        return x14
    x15 = fork(mapply, x2, x14)
    if x == 15:
        return x15
    x16 = rbind(mir_rot_f, R3)
    if x == 16:
        return x16
    x17 = rbind(mir_rot_f, R1)
    if x == 17:
        return x17
    x18 = astuple(x16, x17)
    if x == 18:
        return x18
    x19 = rbind(mir_rot_f, R0)
    if x == 19:
        return x19
    x20 = rbind(mir_rot_f, R2)
    if x == 20:
        return x20
    x21 = astuple(x19, x20)
    if x == 21:
        return x21
    x22 = combine(x18, x21)
    if x == 22:
        return x22
    x23 = rbind(get_nth_f, L1)
    if x == 23:
        return x23
    x24 = fork(compose, x8, x23)
    if x == 24:
        return x24
    x25 = product(x22, x22)
    if x == 25:
        return x25
    x26 = apply(x24, x25)
    if x == 26:
        return x26
    x27 = totuple(x26)
    if x == 27:
        return x27
    x28 = combine(x22, x27)
    if x == 28:
        return x28
    x29 = o_g(I, R1)
    if x == 29:
        return x29
    x30 = get_arg_rank_f(x29, numcolors_f, F0)
    if x == 30:
        return x30
    x31 = rapply_t(x28, x30)
    if x == 31:
        return x31
    x32 = mapply(x15, x31)
    if x == 32:
        return x32
    O = paint(I, x32)
    return O

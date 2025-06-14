def solve_6aa20dc0_one(S, I):
    return paint(I, mapply(fork(mapply, lbind(lbind, shift), compose(lbind(occurrences, I), fork(difference, identity, fork(sfilter, identity, compose(lbind(matcher, rbind(get_nth_f, F0)), rbind(get_color_rank_f, F0)))))), rapply_f(apply(fork(compose, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), product(insert(rbind(mir_rot_f, R1), insert(rbind(mir_rot_f, R3), insert(rbind(mir_rot_f, R0), insert(rbind(mir_rot_f, R2), initset(identity))))), apply(lbind(rbind, upscale_f), interval(ONE, FOUR, ONE)))), normalize(get_arg_rank_f(o_g(I, R3), numcolors_f, F0)))))


def solve_6aa20dc0(S, I, x=0):
    x1 = lbind(lbind, shift)
    if x == 1:
        return x1
    x2 = lbind(occurrences, I)
    if x == 2:
        return x2
    x3 = rbind(get_nth_f, F0)
    if x == 3:
        return x3
    x4 = lbind(matcher, x3)
    if x == 4:
        return x4
    x5 = rbind(get_color_rank_f, F0)
    if x == 5:
        return x5
    x6 = compose(x4, x5)
    if x == 6:
        return x6
    x7 = fork(sfilter, identity, x6)
    if x == 7:
        return x7
    x8 = fork(difference, identity, x7)
    if x == 8:
        return x8
    x9 = compose(x2, x8)
    if x == 9:
        return x9
    x10 = fork(mapply, x1, x9)
    if x == 10:
        return x10
    x11 = rbind(get_nth_f, L1)
    if x == 11:
        return x11
    x12 = fork(compose, x3, x11)
    if x == 12:
        return x12
    x13 = rbind(mir_rot_f, R1)
    if x == 13:
        return x13
    x14 = rbind(mir_rot_f, R3)
    if x == 14:
        return x14
    x15 = rbind(mir_rot_f, R0)
    if x == 15:
        return x15
    x16 = rbind(mir_rot_f, R2)
    if x == 16:
        return x16
    x17 = initset(identity)
    if x == 17:
        return x17
    x18 = insert(x16, x17)
    if x == 18:
        return x18
    x19 = insert(x15, x18)
    if x == 19:
        return x19
    x20 = insert(x14, x19)
    if x == 20:
        return x20
    x21 = insert(x13, x20)
    if x == 21:
        return x21
    x22 = lbind(rbind, upscale_f)
    if x == 22:
        return x22
    x23 = interval(ONE, FOUR, ONE)
    if x == 23:
        return x23
    x24 = apply(x22, x23)
    if x == 24:
        return x24
    x25 = product(x21, x24)
    if x == 25:
        return x25
    x26 = apply(x12, x25)
    if x == 26:
        return x26
    x27 = o_g(I, R3)
    if x == 27:
        return x27
    x28 = get_arg_rank_f(x27, numcolors_f, F0)
    if x == 28:
        return x28
    x29 = normalize(x28)
    if x == 29:
        return x29
    x30 = rapply_f(x26, x29)
    if x == 30:
        return x30
    x31 = mapply(x10, x30)
    if x == 31:
        return x31
    O = paint(I, x31)
    return O

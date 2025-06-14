def solve_447fd412_one(S, I):
    return paint(I, mapply(fork(mapply, lbind(lbind, shift), compose(lbind(apply, increment), fork(apply, chain(lbind(rbind, subtract), rbind(corner, R0), fork(difference, identity, fork(sfilter, identity, compose(lbind(matcher, rbind(get_nth_f, F0)), rbind(get_color_rank_f, F0))))), chain(lbind(occurrences, I), fork(combine, identity, compose(lbind(recolor_i, ZERO), outbox)), fork(difference, identity, fork(sfilter, identity, compose(lbind(matcher, rbind(get_nth_f, F0)), rbind(get_color_rank_f, F0)))))))), rapply_t(apply(lbind(rbind, upscale_f), interval(ONE, FOUR, ONE)), normalize(get_arg_rank_f(o_g(I, R3), numcolors_f, F0)))))


def solve_447fd412(S, I, x=0):
    x1 = lbind(lbind, shift)
    if x == 1:
        return x1
    x2 = lbind(apply, increment)
    if x == 2:
        return x2
    x3 = lbind(rbind, subtract)
    if x == 3:
        return x3
    x4 = rbind(corner, R0)
    if x == 4:
        return x4
    x5 = rbind(get_nth_f, F0)
    if x == 5:
        return x5
    x6 = lbind(matcher, x5)
    if x == 6:
        return x6
    x7 = rbind(get_color_rank_f, F0)
    if x == 7:
        return x7
    x8 = compose(x6, x7)
    if x == 8:
        return x8
    x9 = fork(sfilter, identity, x8)
    if x == 9:
        return x9
    x10 = fork(difference, identity, x9)
    if x == 10:
        return x10
    x11 = chain(x3, x4, x10)
    if x == 11:
        return x11
    x12 = lbind(occurrences, I)
    if x == 12:
        return x12
    x13 = lbind(recolor_i, ZERO)
    if x == 13:
        return x13
    x14 = compose(x13, outbox)
    if x == 14:
        return x14
    x15 = fork(combine, identity, x14)
    if x == 15:
        return x15
    x16 = chain(x12, x15, x10)
    if x == 16:
        return x16
    x17 = fork(apply, x11, x16)
    if x == 17:
        return x17
    x18 = compose(x2, x17)
    if x == 18:
        return x18
    x19 = fork(mapply, x1, x18)
    if x == 19:
        return x19
    x20 = lbind(rbind, upscale_f)
    if x == 20:
        return x20
    x21 = interval(ONE, FOUR, ONE)
    if x == 21:
        return x21
    x22 = apply(x20, x21)
    if x == 22:
        return x22
    x23 = o_g(I, R3)
    if x == 23:
        return x23
    x24 = get_arg_rank_f(x23, numcolors_f, F0)
    if x == 24:
        return x24
    x25 = normalize(x24)
    if x == 25:
        return x25
    x26 = rapply_t(x22, x25)
    if x == 26:
        return x26
    x27 = mapply(x19, x26)
    if x == 27:
        return x27
    O = paint(I, x27)
    return O

def solve_72322fa7_one(S, I):
    return paint(paint(I, mapply(fork(mapply, compose(lbind(lbind, shift), normalize), compose(lbind(occurrences, I), fork(sfilter, identity, compose(lbind(matcher, rbind(get_nth_f, F0)), rbind(get_color_rank_f, F0))))), difference(o_g(I, R3), sfilter_f(o_g(I, R3), matcher(numcolors_f, ONE))))), mapply(fork(mapply, compose(lbind(lbind, shift), normalize), fork(apply, compose(lbind(rbind, add), fork(subtract, rbind(corner, R0), compose(rbind(corner, R0), fork(difference, identity, fork(sfilter, identity, compose(lbind(matcher, rbind(get_nth_f, F0)), rbind(get_color_rank_f, F0))))))), compose(lbind(occurrences, I), fork(difference, identity, fork(sfilter, identity, compose(lbind(matcher, rbind(get_nth_f, F0)), rbind(get_color_rank_f, F0))))))), difference(o_g(I, R3), sfilter_f(o_g(I, R3), matcher(numcolors_f, ONE)))))


def solve_72322fa7(S, I, x=0):
    x1 = lbind(lbind, shift)
    if x == 1:
        return x1
    x2 = compose(x1, normalize)
    if x == 2:
        return x2
    x3 = lbind(occurrences, I)
    if x == 3:
        return x3
    x4 = rbind(get_nth_f, F0)
    if x == 4:
        return x4
    x5 = lbind(matcher, x4)
    if x == 5:
        return x5
    x6 = rbind(get_color_rank_f, F0)
    if x == 6:
        return x6
    x7 = compose(x5, x6)
    if x == 7:
        return x7
    x8 = fork(sfilter, identity, x7)
    if x == 8:
        return x8
    x9 = compose(x3, x8)
    if x == 9:
        return x9
    x10 = fork(mapply, x2, x9)
    if x == 10:
        return x10
    x11 = o_g(I, R3)
    if x == 11:
        return x11
    x12 = matcher(numcolors_f, ONE)
    if x == 12:
        return x12
    x13 = sfilter_f(x11, x12)
    if x == 13:
        return x13
    x14 = difference(x11, x13)
    if x == 14:
        return x14
    x15 = mapply(x10, x14)
    if x == 15:
        return x15
    x16 = paint(I, x15)
    if x == 16:
        return x16
    x17 = lbind(rbind, add)
    if x == 17:
        return x17
    x18 = rbind(corner, R0)
    if x == 18:
        return x18
    x19 = fork(difference, identity, x8)
    if x == 19:
        return x19
    x20 = compose(x18, x19)
    if x == 20:
        return x20
    x21 = fork(subtract, x18, x20)
    if x == 21:
        return x21
    x22 = compose(x17, x21)
    if x == 22:
        return x22
    x23 = compose(x3, x19)
    if x == 23:
        return x23
    x24 = fork(apply, x22, x23)
    if x == 24:
        return x24
    x25 = fork(mapply, x2, x24)
    if x == 25:
        return x25
    x26 = mapply(x25, x14)
    if x == 26:
        return x26
    O = paint(x16, x26)
    return O

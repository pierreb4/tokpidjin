def solve_7837ac64_one(S, I):
    return downscale(power(compose(rbind(mir_rot_t, R1), chain(lbind(apply, rbind(get_nth_f, F0)), rbind(sfilter, chain(flip, rbind(contained, interval(ZERO, height_t(subgrid(merge_f(remove_f(get_arg_rank_f(fgpartition(I), size, F0), fgpartition(I))), I)), increment(height_f(get_nth_f(colorfilter(o_g(subgrid(merge_f(remove_f(get_arg_rank_f(fgpartition(I), size, F0), fgpartition(I))), I), R4), ZERO), F0))))), rbind(get_nth_f, L1))), rbind(pair, interval(ZERO, height_t(subgrid(merge_f(remove_f(get_arg_rank_f(fgpartition(I), size, F0), fgpartition(I))), I)), ONE)))), TWO)(paint(subgrid(merge_f(remove_f(get_arg_rank_f(fgpartition(I), size, F0), fgpartition(I))), I), mapply(fork(recolor_o, compose(color, chain(rbind(toobject, subgrid(merge_f(remove_f(get_arg_rank_f(fgpartition(I), size, F0), fgpartition(I))), I)), corners, outbox)), identity), sfilter(colorfilter(o_g(subgrid(merge_f(remove_f(get_arg_rank_f(fgpartition(I), size, F0), fgpartition(I))), I), R4), ZERO), fork(both, compose(flip, chain(lbind(contained, chain(color, merge, frontiers)(I)), palette_f, chain(rbind(toobject, subgrid(merge_f(remove_f(get_arg_rank_f(fgpartition(I), size, F0), fgpartition(I))), I)), corners, outbox))), matcher(compose(numcolors_f, chain(rbind(toobject, subgrid(merge_f(remove_f(get_arg_rank_f(fgpartition(I), size, F0), fgpartition(I))), I)), corners, outbox)), ONE)))))), height_f(get_nth_f(colorfilter(o_g(subgrid(merge_f(remove_f(get_arg_rank_f(fgpartition(I), size, F0), fgpartition(I))), I), R4), ZERO), F0)))


def solve_7837ac64(S, I, x=0):
    x1 = rbind(mir_rot_t, R1)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, F0)
    if x == 2:
        return x2
    x3 = lbind(apply, x2)
    if x == 3:
        return x3
    x4 = fgpartition(I)
    if x == 4:
        return x4
    x5 = get_arg_rank_f(x4, size, F0)
    if x == 5:
        return x5
    x6 = remove_f(x5, x4)
    if x == 6:
        return x6
    x7 = merge_f(x6)
    if x == 7:
        return x7
    x8 = subgrid(x7, I)
    if x == 8:
        return x8
    x9 = height_t(x8)
    if x == 9:
        return x9
    x10 = o_g(x8, R4)
    if x == 10:
        return x10
    x11 = colorfilter(x10, ZERO)
    if x == 11:
        return x11
    x12 = get_nth_f(x11, F0)
    if x == 12:
        return x12
    x13 = height_f(x12)
    if x == 13:
        return x13
    x14 = increment(x13)
    if x == 14:
        return x14
    x15 = interval(ZERO, x9, x14)
    if x == 15:
        return x15
    x16 = rbind(contained, x15)
    if x == 16:
        return x16
    x17 = rbind(get_nth_f, L1)
    if x == 17:
        return x17
    x18 = chain(flip, x16, x17)
    if x == 18:
        return x18
    x19 = rbind(sfilter, x18)
    if x == 19:
        return x19
    x20 = interval(ZERO, x9, ONE)
    if x == 20:
        return x20
    x21 = rbind(pair, x20)
    if x == 21:
        return x21
    x22 = chain(x3, x19, x21)
    if x == 22:
        return x22
    x23 = compose(x1, x22)
    if x == 23:
        return x23
    x24 = power(x23, TWO)
    if x == 24:
        return x24
    x25 = rbind(toobject, x8)
    if x == 25:
        return x25
    x26 = chain(x25, corners, outbox)
    if x == 26:
        return x26
    x27 = compose(color, x26)
    if x == 27:
        return x27
    x28 = fork(recolor_o, x27, identity)
    if x == 28:
        return x28
    x29 = chain(color, merge, frontiers)
    if x == 29:
        return x29
    x30 = x29(I)
    if x == 30:
        return x30
    x31 = lbind(contained, x30)
    if x == 31:
        return x31
    x32 = chain(x31, palette_f, x26)
    if x == 32:
        return x32
    x33 = compose(flip, x32)
    if x == 33:
        return x33
    x34 = compose(numcolors_f, x26)
    if x == 34:
        return x34
    x35 = matcher(x34, ONE)
    if x == 35:
        return x35
    x36 = fork(both, x33, x35)
    if x == 36:
        return x36
    x37 = sfilter(x11, x36)
    if x == 37:
        return x37
    x38 = mapply(x28, x37)
    if x == 38:
        return x38
    x39 = paint(x8, x38)
    if x == 39:
        return x39
    x40 = x24(x39)
    if x == 40:
        return x40
    O = downscale(x40, x13)
    return O

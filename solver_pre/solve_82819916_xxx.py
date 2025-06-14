def solve_82819916_one(S, I):
    return paint(I, mapply(fork(combine, fork(recolor_o, compose(rbind(get_nth_f, F0), rbind(rbind(get_arg_rank, L1), compose(rbind(get_nth_f, L1), rbind(get_nth_f, L1)))), compose(lbind(shift, sfilter_f(normalize(get_arg_rank_f(o_g(I, R3), size, F0)), matcher(rbind(get_nth_f, F0), compose(rbind(get_nth_f, F0), rbind(rbind(get_arg_rank, L1), compose(rbind(get_nth_f, L1), rbind(get_nth_f, L1))))(normalize(get_arg_rank_f(o_g(I, R3), size, F0)))))), compose(toivec, rbind(col_row, R1)))), fork(recolor_o, fork(other, palette_f, compose(rbind(get_nth_f, F0), rbind(rbind(get_arg_rank, L1), compose(rbind(get_nth_f, L1), rbind(get_nth_f, L1))))), compose(lbind(shift, difference(normalize(get_arg_rank_f(o_g(I, R3), size, F0)), sfilter_f(normalize(get_arg_rank_f(o_g(I, R3), size, F0)), matcher(rbind(get_nth_f, F0), compose(rbind(get_nth_f, F0), rbind(rbind(get_arg_rank, L1), compose(rbind(get_nth_f, L1), rbind(get_nth_f, L1))))(normalize(get_arg_rank_f(o_g(I, R3), size, F0))))))), compose(toivec, rbind(col_row, R1))))), remove_f(get_arg_rank_f(o_g(I, R3), size, F0), o_g(I, R3))))


def solve_82819916(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = rbind(get_arg_rank, L1)
    if x == 2:
        return x2
    x3 = rbind(get_nth_f, L1)
    if x == 3:
        return x3
    x4 = compose(x3, x3)
    if x == 4:
        return x4
    x5 = rbind(x2, x4)
    if x == 5:
        return x5
    x6 = compose(x1, x5)
    if x == 6:
        return x6
    x7 = o_g(I, R3)
    if x == 7:
        return x7
    x8 = get_arg_rank_f(x7, size, F0)
    if x == 8:
        return x8
    x9 = normalize(x8)
    if x == 9:
        return x9
    x10 = x6(x9)
    if x == 10:
        return x10
    x11 = matcher(x1, x10)
    if x == 11:
        return x11
    x12 = sfilter_f(x9, x11)
    if x == 12:
        return x12
    x13 = lbind(shift, x12)
    if x == 13:
        return x13
    x14 = rbind(col_row, R1)
    if x == 14:
        return x14
    x15 = compose(toivec, x14)
    if x == 15:
        return x15
    x16 = compose(x13, x15)
    if x == 16:
        return x16
    x17 = fork(recolor_o, x6, x16)
    if x == 17:
        return x17
    x18 = fork(other, palette_f, x6)
    if x == 18:
        return x18
    x19 = difference(x9, x12)
    if x == 19:
        return x19
    x20 = lbind(shift, x19)
    if x == 20:
        return x20
    x21 = compose(x20, x15)
    if x == 21:
        return x21
    x22 = fork(recolor_o, x18, x21)
    if x == 22:
        return x22
    x23 = fork(combine, x17, x22)
    if x == 23:
        return x23
    x24 = remove_f(x8, x7)
    if x == 24:
        return x24
    x25 = mapply(x23, x24)
    if x == 25:
        return x25
    O = paint(I, x25)
    return O

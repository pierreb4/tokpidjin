def solve_57aa92db_one(S, I):
    return paint(paint(I, mapply(fork(recolor_o, chain(chain(rbind(get_nth_f, F0), lbind(remove, ZERO), palette_f), rbind(toobject, I), outbox), fork(upscale_f, compose(lbind(shift, normalize_o(get_arg_rank_f(o_g(I, R3), fork(subtract, compose(rbind(get_rank, F0), fork(apply, lbind(lbind, colorcount_f), palette_f)), compose(rbind(get_rank, L1), fork(apply, lbind(lbind, colorcount_f), palette_f))), F0))), fork(subtract, rbind(corner, R0), compose(lbind(multiply, corner(sfilter_f(normalize_o(get_arg_rank_f(o_g(I, R3), fork(subtract, compose(rbind(get_rank, F0), fork(apply, lbind(lbind, colorcount_f), palette_f)), compose(rbind(get_rank, L1), fork(apply, lbind(lbind, colorcount_f), palette_f))), F0)), matcher(rbind(get_nth_f, F0), get_color_rank_f(get_arg_rank_f(o_g(I, R3), fork(subtract, compose(rbind(get_rank, F0), fork(apply, lbind(lbind, colorcount_f), palette_f)), compose(rbind(get_rank, L1), fork(apply, lbind(lbind, colorcount_f), palette_f))), F0), L1))), R0)), width_f))), width_f)), colorfilter(o_g(I, R5), get_color_rank_f(get_arg_rank_f(o_g(I, R3), fork(subtract, compose(rbind(get_rank, F0), fork(apply, lbind(lbind, colorcount_f), palette_f)), compose(rbind(get_rank, L1), fork(apply, lbind(lbind, colorcount_f), palette_f))), F0), L1)))), merge_f(o_g(I, R5)))


def solve_57aa92db(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = lbind(remove, ZERO)
    if x == 2:
        return x2
    x3 = chain(x1, x2, palette_f)
    if x == 3:
        return x3
    x4 = rbind(toobject, I)
    if x == 4:
        return x4
    x5 = chain(x3, x4, outbox)
    if x == 5:
        return x5
    x6 = o_g(I, R3)
    if x == 6:
        return x6
    x7 = rbind(get_rank, F0)
    if x == 7:
        return x7
    x8 = lbind(lbind, colorcount_f)
    if x == 8:
        return x8
    x9 = fork(apply, x8, palette_f)
    if x == 9:
        return x9
    x10 = compose(x7, x9)
    if x == 10:
        return x10
    x11 = rbind(get_rank, L1)
    if x == 11:
        return x11
    x12 = compose(x11, x9)
    if x == 12:
        return x12
    x13 = fork(subtract, x10, x12)
    if x == 13:
        return x13
    x14 = get_arg_rank_f(x6, x13, F0)
    if x == 14:
        return x14
    x15 = normalize_o(x14)
    if x == 15:
        return x15
    x16 = lbind(shift, x15)
    if x == 16:
        return x16
    x17 = rbind(corner, R0)
    if x == 17:
        return x17
    x18 = get_color_rank_f(x14, L1)
    if x == 18:
        return x18
    x19 = matcher(x1, x18)
    if x == 19:
        return x19
    x20 = sfilter_f(x15, x19)
    if x == 20:
        return x20
    x21 = corner(x20, R0)
    if x == 21:
        return x21
    x22 = lbind(multiply, x21)
    if x == 22:
        return x22
    x23 = compose(x22, width_f)
    if x == 23:
        return x23
    x24 = fork(subtract, x17, x23)
    if x == 24:
        return x24
    x25 = compose(x16, x24)
    if x == 25:
        return x25
    x26 = fork(upscale_f, x25, width_f)
    if x == 26:
        return x26
    x27 = fork(recolor_o, x5, x26)
    if x == 27:
        return x27
    x28 = o_g(I, R5)
    if x == 28:
        return x28
    x29 = colorfilter(x28, x18)
    if x == 29:
        return x29
    x30 = mapply(x27, x29)
    if x == 30:
        return x30
    x31 = paint(I, x30)
    if x == 31:
        return x31
    x32 = merge_f(x28)
    if x == 32:
        return x32
    O = paint(x31, x32)
    return O

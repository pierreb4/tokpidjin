def solve_952a094c_one(S, I):
    return paint(cover(I, merge_f(sizefilter(o_g(I, R5), ONE))), apply(fork(astuple, compose(color, chain(lbind(rbind(get_arg_rank, F0), sizefilter(o_g(I, R5), ONE)), lbind(rbind, manhattan), initset)), identity), corners(outbox(get_arg_rank_f(o_g(I, R5), size, F0)))))


def solve_952a094c(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = merge_f(x2)
    if x == 3:
        return x3
    x4 = cover(I, x3)
    if x == 4:
        return x4
    x5 = rbind(get_arg_rank, F0)
    if x == 5:
        return x5
    x6 = lbind(x5, x2)
    if x == 6:
        return x6
    x7 = lbind(rbind, manhattan)
    if x == 7:
        return x7
    x8 = chain(x6, x7, initset)
    if x == 8:
        return x8
    x9 = compose(color, x8)
    if x == 9:
        return x9
    x10 = fork(astuple, x9, identity)
    if x == 10:
        return x10
    x11 = get_arg_rank_f(x1, size, F0)
    if x == 11:
        return x11
    x12 = outbox(x11)
    if x == 12:
        return x12
    x13 = corners(x12)
    if x == 13:
        return x13
    x14 = apply(x10, x13)
    if x == 14:
        return x14
    O = paint(x4, x14)
    return O

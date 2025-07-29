def solve_952a094c_one(S, I):
    return paint(cover(I, merge_f(sizefilter(o_g(I, R5), ONE))), apply(fork(astuple, compose(color, chain(lbind(rbind(get_arg_rank, F0), sizefilter(o_g(I, R5), ONE)), lbind(rbind, manhattan), initset)), identity), corners(outbox(get_arg_rank_f(o_g(I, R5), size, F0)))))


def solve_952a094c(S, I):
    x1 = o_g(I, R5)
    x2 = sizefilter(x1, ONE)
    x3 = merge_f(x2)
    x4 = cover(I, x3)
    x5 = rbind(get_arg_rank, F0)
    x6 = lbind(x5, x2)
    x7 = lbind(rbind, manhattan)
    x8 = chain(x6, x7, initset)
    x9 = compose(color, x8)
    x10 = fork(astuple, x9, identity)
    x11 = get_arg_rank_f(x1, size, F0)
    x12 = outbox(x11)
    x13 = corners(x12)
    x14 = apply(x10, x13)
    O = paint(x4, x14)
    return O

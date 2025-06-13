def solve_f35d900a_one(S, I):
    return fill(paint(I, mapply(fork(recolor_i, compose(lbind(other, remove(ZERO, palette_t(I))), color), outbox), o_g(I, R5))), FIVE, sfilter_f(difference(box(mapply(toindices, o_g(I, R5))), mapply(toindices, o_g(I, R5))), compose(even, fork(manhattan, initset, chain(initset, lbind(rbind(get_arg_rank, L1), mapply(toindices, o_g(I, R5))), chain(rbind(compose, initset), lbind(rbind, manhattan), initset))))))


def solve_f35d900a(S, I):
    x1 = palette_t(I)
    x2 = remove(ZERO, x1)
    x3 = lbind(other, x2)
    x4 = compose(x3, color)
    x5 = fork(recolor_i, x4, outbox)
    x6 = o_g(I, R5)
    x7 = mapply(x5, x6)
    x8 = paint(I, x7)
    x9 = mapply(toindices, x6)
    x10 = box(x9)
    x11 = difference(x10, x9)
    x12 = rbind(get_arg_rank, L1)
    x13 = lbind(x12, x9)
    x14 = rbind(compose, initset)
    x15 = lbind(rbind, manhattan)
    x16 = chain(x14, x15, initset)
    x17 = chain(initset, x13, x16)
    x18 = fork(manhattan, initset, x17)
    x19 = compose(even, x18)
    x20 = sfilter_f(x11, x19)
    O = fill(x8, FIVE, x20)
    return O

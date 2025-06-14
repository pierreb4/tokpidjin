def solve_f35d900a_one(S, I):
    return fill(paint(I, mapply(fork(recolor_i, compose(lbind(other, remove(ZERO, palette_t(I))), color), outbox), o_g(I, R5))), FIVE, sfilter_f(difference(box(mapply(toindices, o_g(I, R5))), mapply(toindices, o_g(I, R5))), compose(even, fork(manhattan, initset, chain(initset, lbind(rbind(get_arg_rank, L1), mapply(toindices, o_g(I, R5))), chain(rbind(compose, initset), lbind(rbind, manhattan), initset))))))


def solve_f35d900a(S, I, x=0):
    x1 = palette_t(I)
    if x == 1:
        return x1
    x2 = remove(ZERO, x1)
    if x == 2:
        return x2
    x3 = lbind(other, x2)
    if x == 3:
        return x3
    x4 = compose(x3, color)
    if x == 4:
        return x4
    x5 = fork(recolor_i, x4, outbox)
    if x == 5:
        return x5
    x6 = o_g(I, R5)
    if x == 6:
        return x6
    x7 = mapply(x5, x6)
    if x == 7:
        return x7
    x8 = paint(I, x7)
    if x == 8:
        return x8
    x9 = mapply(toindices, x6)
    if x == 9:
        return x9
    x10 = box(x9)
    if x == 10:
        return x10
    x11 = difference(x10, x9)
    if x == 11:
        return x11
    x12 = rbind(get_arg_rank, L1)
    if x == 12:
        return x12
    x13 = lbind(x12, x9)
    if x == 13:
        return x13
    x14 = rbind(compose, initset)
    if x == 14:
        return x14
    x15 = lbind(rbind, manhattan)
    if x == 15:
        return x15
    x16 = chain(x14, x15, initset)
    if x == 16:
        return x16
    x17 = chain(initset, x13, x16)
    if x == 17:
        return x17
    x18 = fork(manhattan, initset, x17)
    if x == 18:
        return x18
    x19 = compose(even, x18)
    if x == 19:
        return x19
    x20 = sfilter_f(x11, x19)
    if x == 20:
        return x20
    O = fill(x8, FIVE, x20)
    return O

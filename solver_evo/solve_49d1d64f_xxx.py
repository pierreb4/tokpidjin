def solve_49d1d64f_one(S, I):
    return paint(paint(canvas(BLACK, add(shape_t(I), TWO)), shift(asobject(I), UNITY)), apply(fork(astuple, chain(rbind(get_nth_f, F0), lbind(rbind(get_arg_rank, L1), shift(asobject(I), UNITY)), chain(rbind(compose, initset), lbind(lbind, manhattan), initset)), identity), fork(difference, box, corners)(asindices(canvas(BLACK, add(shape_t(I), TWO))))))


def solve_49d1d64f(S, I):
    x1 = shape_t(I)
    x2 = add(x1, TWO)
    x3 = canvas(BLACK, x2)
    x4 = asobject(I)
    x5 = shift(x4, UNITY)
    x6 = paint(x3, x5)
    x7 = rbind(get_nth_f, F0)
    x8 = rbind(get_arg_rank, L1)
    x9 = lbind(x8, x5)
    x10 = rbind(compose, initset)
    x11 = lbind(lbind, manhattan)
    x12 = chain(x10, x11, initset)
    x13 = chain(x7, x9, x12)
    x14 = fork(astuple, x13, identity)
    x15 = fork(difference, box, corners)
    x16 = asindices(x3)
    x17 = x15(x16)
    x18 = apply(x14, x17)
    O = paint(x6, x18)
    return O

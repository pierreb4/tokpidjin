def solve_49d1d64f_one(S, I):
    return paint(paint(canvas(BLACK, add(shape_t(I), TWO)), shift(asobject(I), UNITY)), apply(fork(astuple, chain(rbind(get_nth_f, F0), lbind(rbind(get_arg_rank, L1), shift(asobject(I), UNITY)), chain(rbind(compose, initset), lbind(lbind, manhattan), initset)), identity), fork(difference, box, corners)(asindices(canvas(BLACK, add(shape_t(I), TWO))))))


def solve_49d1d64f(S, I, x=0):
    x1 = shape_t(I)
    if x == 1:
        return x1
    x2 = add(x1, TWO)
    if x == 2:
        return x2
    x3 = canvas(BLACK, x2)
    if x == 3:
        return x3
    x4 = asobject(I)
    if x == 4:
        return x4
    x5 = shift(x4, UNITY)
    if x == 5:
        return x5
    x6 = paint(x3, x5)
    if x == 6:
        return x6
    x7 = rbind(get_nth_f, F0)
    if x == 7:
        return x7
    x8 = rbind(get_arg_rank, L1)
    if x == 8:
        return x8
    x9 = lbind(x8, x5)
    if x == 9:
        return x9
    x10 = rbind(compose, initset)
    if x == 10:
        return x10
    x11 = lbind(lbind, manhattan)
    if x == 11:
        return x11
    x12 = chain(x10, x11, initset)
    if x == 12:
        return x12
    x13 = chain(x7, x9, x12)
    if x == 13:
        return x13
    x14 = fork(astuple, x13, identity)
    if x == 14:
        return x14
    x15 = fork(difference, box, corners)
    if x == 15:
        return x15
    x16 = asindices(x3)
    if x == 16:
        return x16
    x17 = x15(x16)
    if x == 17:
        return x17
    x18 = apply(x14, x17)
    if x == 18:
        return x18
    O = paint(x6, x18)
    return O

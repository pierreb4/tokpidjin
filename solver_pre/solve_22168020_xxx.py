def solve_22168020_one(S, I):
    return paint(I, mapply(fork(recolor_i, identity, compose(merge, fork(lbind(prapply, connect), lbind(f_ofcolor, I), lbind(f_ofcolor, I)))), remove(ZERO, palette_t(I))))


def solve_22168020(S, I):
    x1 = lbind(prapply, connect)
    x2 = lbind(f_ofcolor, I)
    x3 = fork(x1, x2, x2)
    x4 = compose(merge, x3)
    x5 = fork(recolor_i, identity, x4)
    x6 = palette_t(I)
    x7 = remove(ZERO, x6)
    x8 = mapply(x5, x7)
    O = paint(I, x8)
    return O

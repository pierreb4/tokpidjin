def solve_22168020_one(S, I):
    return paint(I, mapply(fork(recolor_i, identity, compose(merge, fork(lbind(prapply, connect), lbind(f_ofcolor, I), lbind(f_ofcolor, I)))), remove(BLACK, palette_t(I))))


def solve_22168020(S, I, x=0):
    x1 = lbind(prapply, connect)
    if x == 1:
        return x1
    x2 = lbind(f_ofcolor, I)
    if x == 2:
        return x2
    x3 = fork(x1, x2, x2)
    if x == 3:
        return x3
    x4 = compose(merge, x3)
    if x == 4:
        return x4
    x5 = fork(recolor_i, identity, x4)
    if x == 5:
        return x5
    x6 = palette_t(I)
    if x == 6:
        return x6
    x7 = remove(BLACK, x6)
    if x == 7:
        return x7
    x8 = mapply(x5, x7)
    if x == 8:
        return x8
    O = paint(I, x8)
    return O

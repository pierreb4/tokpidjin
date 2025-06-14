def solve_c8cbb738_one(S, I):
    return paint(canvas(get_color_rank_t(I, F0), get_val_rank_f(fgpartition(I), shape_f, F0)), mapply(fork(shift, identity, chain(halve, lbind(subtract, get_val_rank_f(fgpartition(I), shape_f, F0)), shape_f)), apply(normalize, fgpartition(I))))


def solve_c8cbb738(S, I, x=0):
    x1 = get_color_rank_t(I, F0)
    if x == 1:
        return x1
    x2 = fgpartition(I)
    if x == 2:
        return x2
    x3 = get_val_rank_f(x2, shape_f, F0)
    if x == 3:
        return x3
    x4 = canvas(x1, x3)
    if x == 4:
        return x4
    x5 = lbind(subtract, x3)
    if x == 5:
        return x5
    x6 = chain(halve, x5, shape_f)
    if x == 6:
        return x6
    x7 = fork(shift, identity, x6)
    if x == 7:
        return x7
    x8 = apply(normalize, x2)
    if x == 8:
        return x8
    x9 = mapply(x7, x8)
    if x == 9:
        return x9
    O = paint(x4, x9)
    return O

def solve_c8cbb738_one(S, I):
    return paint(canvas(get_color_rank_t(I, F0), get_val_rank_f(fgpartition(I), shape_f, F0)), mapply(fork(shift, identity, chain(halve, lbind(subtract, get_val_rank_f(fgpartition(I), shape_f, F0)), shape_f)), apply(normalize, fgpartition(I))))


def solve_c8cbb738(S, I):
    x1 = get_color_rank_t(I, F0)
    x2 = fgpartition(I)
    x3 = get_val_rank_f(x2, shape_f, F0)
    x4 = canvas(x1, x3)
    x5 = lbind(subtract, x3)
    x6 = chain(halve, x5, shape_f)
    x7 = fork(shift, identity, x6)
    x8 = apply(normalize, x2)
    x9 = mapply(x7, x8)
    O = paint(x4, x9)
    return O

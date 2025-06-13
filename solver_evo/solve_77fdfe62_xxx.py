def solve_77fdfe62_one(S, I):
    return fill(upscale_t(compress(replace(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)), BLACK), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK)), halve(width_t(subgrid(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1))), I)))), BLACK, f_ofcolor(subgrid(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1))), I), BLACK))


def solve_77fdfe62(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F1)
    x3 = c_iz_n(S, x1, x2)
    x4 = replace(I, x3, BLACK)
    x5 = rbind(get_nth_t, F0)
    x6 = c_iz_n(S, x1, x5)
    x7 = replace(x4, x6, BLACK)
    x8 = compress(x7)
    x9 = f_ofcolor(I, x3)
    x10 = subgrid(x9, I)
    x11 = width_t(x10)
    x12 = halve(x11)
    x13 = upscale_t(x8, x12)
    x14 = f_ofcolor(x10, BLACK)
    O = fill(x13, BLACK, x14)
    return O

def solve_7c008303_one(S, I):
    return fill(upscale_t(compress(replace(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)), BLACK)), THREE), BLACK, f_ofcolor(subgrid(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), I), BLACK))


def solve_7c008303(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_iz_n(S, x1, x2)
    x4 = replace(I, x3, BLACK)
    x5 = rbind(get_nth_t, F1)
    x6 = c_iz_n(S, x1, x5)
    x7 = replace(x4, x6, BLACK)
    x8 = compress(x7)
    x9 = upscale_t(x8, THREE)
    x10 = f_ofcolor(I, x3)
    x11 = subgrid(x10, I)
    x12 = f_ofcolor(x11, BLACK)
    O = fill(x9, BLACK, x12)
    return O

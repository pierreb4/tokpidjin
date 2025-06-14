def solve_7c008303_one(S, I):
    return fill(upscale_t(compress(replace(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)), BLACK)), THREE), BLACK, f_ofcolor(subgrid(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), I), BLACK))


def solve_7c008303(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_iz_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = replace(I, x3, BLACK)
    if x == 4:
        return x4
    x5 = rbind(get_nth_t, F1)
    if x == 5:
        return x5
    x6 = c_iz_n(S, x1, x5)
    if x == 6:
        return x6
    x7 = replace(x4, x6, BLACK)
    if x == 7:
        return x7
    x8 = compress(x7)
    if x == 8:
        return x8
    x9 = upscale_t(x8, THREE)
    if x == 9:
        return x9
    x10 = f_ofcolor(I, x3)
    if x == 10:
        return x10
    x11 = subgrid(x10, I)
    if x == 11:
        return x11
    x12 = f_ofcolor(x11, BLACK)
    if x == 12:
        return x12
    O = fill(x9, BLACK, x12)
    return O

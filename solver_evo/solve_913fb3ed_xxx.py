def solve_913fb3ed_one(S, I):
    return fill(fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), mapply(neighbors, f_ofcolor(I, GREEN))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), mapply(neighbors, f_ofcolor(I, CYAN))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(neighbors, f_ofcolor(I, RED)))


def solve_913fb3ed(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F1)
    x3 = c_zo_n(S, x1, x2)
    x4 = f_ofcolor(I, GREEN)
    x5 = mapply(neighbors, x4)
    x6 = fill(I, x3, x5)
    x7 = rbind(get_nth_t, F2)
    x8 = c_zo_n(S, x1, x7)
    x9 = f_ofcolor(I, CYAN)
    x10 = mapply(neighbors, x9)
    x11 = fill(x6, x8, x10)
    x12 = rbind(get_nth_t, F0)
    x13 = c_zo_n(S, x1, x12)
    x14 = f_ofcolor(I, RED)
    x15 = mapply(neighbors, x14)
    O = fill(x11, x13, x15)
    return O

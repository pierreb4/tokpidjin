def solve_4258a5f9_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(neighbors, f_ofcolor(I, GRAY)))


def solve_4258a5f9(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = f_ofcolor(I, GRAY)
    x5 = mapply(neighbors, x4)
    O = fill(I, x3, x5)
    return O

def solve_913fb3ed_one(S, I):
    return fill(fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), mapply(neighbors, f_ofcolor(I, GREEN))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), mapply(neighbors, f_ofcolor(I, CYAN))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(neighbors, f_ofcolor(I, RED)))


def solve_913fb3ed(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F1)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, GREEN)
    if x == 4:
        return x4
    x5 = mapply(neighbors, x4)
    if x == 5:
        return x5
    x6 = fill(I, x3, x5)
    if x == 6:
        return x6
    x7 = rbind(get_nth_t, F2)
    if x == 7:
        return x7
    x8 = c_zo_n(S, x1, x7)
    if x == 8:
        return x8
    x9 = f_ofcolor(I, CYAN)
    if x == 9:
        return x9
    x10 = mapply(neighbors, x9)
    if x == 10:
        return x10
    x11 = fill(x6, x8, x10)
    if x == 11:
        return x11
    x12 = rbind(get_nth_t, F0)
    if x == 12:
        return x12
    x13 = c_zo_n(S, x1, x12)
    if x == 13:
        return x13
    x14 = f_ofcolor(I, RED)
    if x == 14:
        return x14
    x15 = mapply(neighbors, x14)
    if x == 15:
        return x15
    O = fill(x11, x13, x15)
    return O

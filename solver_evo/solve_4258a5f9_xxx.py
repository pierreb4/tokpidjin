def solve_4258a5f9_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(neighbors, f_ofcolor(I, GRAY)))


def solve_4258a5f9(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, GRAY)
    if x == 4:
        return x4
    x5 = mapply(neighbors, x4)
    if x == 5:
        return x5
    O = fill(I, x3, x5)
    return O

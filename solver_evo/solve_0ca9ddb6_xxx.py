def solve_0ca9ddb6_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), mapply(dneighbors, f_ofcolor(I, BLUE))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(ineighbors, f_ofcolor(I, RED)))


def solve_0ca9ddb6(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F1)
    x3 = c_zo_n(S, x1, x2)
    x4 = f_ofcolor(I, BLUE)
    x5 = mapply(dneighbors, x4)
    x6 = fill(I, x3, x5)
    x7 = rbind(get_nth_t, F0)
    x8 = c_zo_n(S, x1, x7)
    x9 = f_ofcolor(I, RED)
    x10 = mapply(ineighbors, x9)
    O = fill(x6, x8, x10)
    return O

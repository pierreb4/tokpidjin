def solve_b60334d2_one(S, I):
    return fill(fill(replace(I, GRAY, BLACK), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(dneighbors, f_ofcolor(I, GRAY))), GRAY, mapply(ineighbors, f_ofcolor(I, GRAY)))


def solve_b60334d2(S, I):
    x1 = replace(I, GRAY, BLACK)
    x2 = identity(p_g)
    x3 = rbind(get_nth_t, F0)
    x4 = c_zo_n(S, x2, x3)
    x5 = f_ofcolor(I, GRAY)
    x6 = mapply(dneighbors, x5)
    x7 = fill(x1, x4, x6)
    x8 = mapply(ineighbors, x5)
    O = fill(x7, GRAY, x8)
    return O

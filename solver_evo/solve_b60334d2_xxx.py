def solve_b60334d2_one(S, I):
    return fill(fill(replace(I, GRAY, BLACK), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(dneighbors, f_ofcolor(I, GRAY))), GRAY, mapply(ineighbors, f_ofcolor(I, GRAY)))


def solve_b60334d2(S, I, x=0):
    x1 = replace(I, GRAY, BLACK)
    if x == 1:
        return x1
    x2 = identity(p_g)
    if x == 2:
        return x2
    x3 = rbind(get_nth_t, F0)
    if x == 3:
        return x3
    x4 = c_zo_n(S, x2, x3)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, GRAY)
    if x == 5:
        return x5
    x6 = mapply(dneighbors, x5)
    if x == 6:
        return x6
    x7 = fill(x1, x4, x6)
    if x == 7:
        return x7
    x8 = mapply(ineighbors, x5)
    if x == 8:
        return x8
    O = fill(x7, GRAY, x8)
    return O

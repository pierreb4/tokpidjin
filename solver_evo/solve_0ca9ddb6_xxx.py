def solve_0ca9ddb6_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), mapply(dneighbors, f_ofcolor(I, BLUE))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(ineighbors, f_ofcolor(I, RED)))


def solve_0ca9ddb6(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F1)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, BLUE)
    if x == 4:
        return x4
    x5 = mapply(dneighbors, x4)
    if x == 5:
        return x5
    x6 = fill(I, x3, x5)
    if x == 6:
        return x6
    x7 = rbind(get_nth_t, F0)
    if x == 7:
        return x7
    x8 = c_zo_n(S, x1, x7)
    if x == 8:
        return x8
    x9 = f_ofcolor(I, RED)
    if x == 9:
        return x9
    x10 = mapply(ineighbors, x9)
    if x == 10:
        return x10
    O = fill(x6, x8, x10)
    return O

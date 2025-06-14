def solve_bdad9b1f_one(S, I):
    return fill(fill(fill(I, RED, hfrontier(center(f_ofcolor(I, RED)))), CYAN, vfrontier(center(f_ofcolor(I, CYAN)))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), intersection(hfrontier(center(f_ofcolor(I, RED))), vfrontier(center(f_ofcolor(I, CYAN)))))


def solve_bdad9b1f(S, I, x=0):
    x1 = f_ofcolor(I, RED)
    if x == 1:
        return x1
    x2 = center(x1)
    if x == 2:
        return x2
    x3 = hfrontier(x2)
    if x == 3:
        return x3
    x4 = fill(I, RED, x3)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, CYAN)
    if x == 5:
        return x5
    x6 = center(x5)
    if x == 6:
        return x6
    x7 = vfrontier(x6)
    if x == 7:
        return x7
    x8 = fill(x4, CYAN, x7)
    if x == 8:
        return x8
    x9 = identity(p_g)
    if x == 9:
        return x9
    x10 = rbind(get_nth_t, F0)
    if x == 10:
        return x10
    x11 = c_zo_n(S, x9, x10)
    if x == 11:
        return x11
    x12 = intersection(x3, x7)
    if x == 12:
        return x12
    O = fill(x8, x11, x12)
    return O

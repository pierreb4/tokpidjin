def solve_bdad9b1f_one(S, I):
    return fill(fill(fill(I, RED, hfrontier(center(f_ofcolor(I, RED)))), CYAN, vfrontier(center(f_ofcolor(I, CYAN)))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), intersection(hfrontier(center(f_ofcolor(I, RED))), vfrontier(center(f_ofcolor(I, CYAN)))))


def solve_bdad9b1f(S, I):
    x1 = f_ofcolor(I, RED)
    x2 = center(x1)
    x3 = hfrontier(x2)
    x4 = fill(I, RED, x3)
    x5 = f_ofcolor(I, CYAN)
    x6 = center(x5)
    x7 = vfrontier(x6)
    x8 = fill(x4, CYAN, x7)
    x9 = identity(p_g)
    x10 = rbind(get_nth_t, F0)
    x11 = c_zo_n(S, x9, x10)
    x12 = intersection(x3, x7)
    O = fill(x8, x11, x12)
    return O

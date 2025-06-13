def solve_1b2d62fb_one(S, I):
    return fill(canvas(BLACK, shape_t(lefthalf(I))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), intersection(f_ofcolor(lefthalf(I), BLACK), f_ofcolor(righthalf(I), BLACK)))


def solve_1b2d62fb(S, I):
    x1 = lefthalf(I)
    x2 = shape_t(x1)
    x3 = canvas(BLACK, x2)
    x4 = identity(p_g)
    x5 = rbind(get_nth_t, F0)
    x6 = c_zo_n(S, x4, x5)
    x7 = f_ofcolor(x1, BLACK)
    x8 = righthalf(I)
    x9 = f_ofcolor(x8, BLACK)
    x10 = intersection(x7, x9)
    O = fill(x3, x6, x10)
    return O

def solve_94f9d214_one(S, I):
    return fill(canvas(BLACK, shape_t(bottomhalf(I))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), intersection(f_ofcolor(vconcat(vconcat(I, I), I), BLACK), f_ofcolor(bottomhalf(I), BLACK)))


def solve_94f9d214(S, I):
    x1 = bottomhalf(I)
    x2 = shape_t(x1)
    x3 = canvas(BLACK, x2)
    x4 = identity(p_g)
    x5 = rbind(get_nth_t, F0)
    x6 = c_zo_n(S, x4, x5)
    x7 = vconcat(I, I)
    x8 = vconcat(x7, I)
    x9 = f_ofcolor(x8, BLACK)
    x10 = f_ofcolor(x1, BLACK)
    x11 = intersection(x9, x10)
    O = fill(x3, x6, x11)
    return O

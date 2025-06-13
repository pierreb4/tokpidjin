def solve_31d5ba1a_one(S, I):
    return fill(canvas(BLACK, shape_t(tophalf(I))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), difference(combine_f(f_ofcolor(tophalf(I), BLACK), f_ofcolor(bottomhalf(I), BLACK)), intersection(f_ofcolor(tophalf(I), BLACK), f_ofcolor(bottomhalf(I), BLACK))))


def solve_31d5ba1a(S, I):
    x1 = tophalf(I)
    x2 = shape_t(x1)
    x3 = canvas(BLACK, x2)
    x4 = identity(p_g)
    x5 = rbind(get_nth_t, F0)
    x6 = c_zo_n(S, x4, x5)
    x7 = f_ofcolor(x1, BLACK)
    x8 = bottomhalf(I)
    x9 = f_ofcolor(x8, BLACK)
    x10 = combine_f(x7, x9)
    x11 = intersection(x7, x9)
    x12 = difference(x10, x11)
    O = fill(x3, x6, x12)
    return O

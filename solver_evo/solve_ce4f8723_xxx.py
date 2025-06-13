def solve_ce4f8723_one(S, I):
    return fill(canvas(c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), astuple(FOUR, FOUR)), BLACK, intersection(f_ofcolor(tophalf(I), BLACK), f_ofcolor(bottomhalf(I), BLACK)))


def solve_ce4f8723(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = astuple(FOUR, FOUR)
    x5 = canvas(x3, x4)
    x6 = tophalf(I)
    x7 = f_ofcolor(x6, BLACK)
    x8 = bottomhalf(I)
    x9 = f_ofcolor(x8, BLACK)
    x10 = intersection(x7, x9)
    O = fill(x5, BLACK, x10)
    return O

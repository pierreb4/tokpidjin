def solve_ce4f8723_one(S, I):
    return fill(canvas(c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), astuple(FOUR, FOUR)), BLACK, intersection(f_ofcolor(tophalf(I), BLACK), f_ofcolor(bottomhalf(I), BLACK)))


def solve_ce4f8723(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = astuple(FOUR, FOUR)
    if x == 4:
        return x4
    x5 = canvas(x3, x4)
    if x == 5:
        return x5
    x6 = tophalf(I)
    if x == 6:
        return x6
    x7 = f_ofcolor(x6, BLACK)
    if x == 7:
        return x7
    x8 = bottomhalf(I)
    if x == 8:
        return x8
    x9 = f_ofcolor(x8, BLACK)
    if x == 9:
        return x9
    x10 = intersection(x7, x9)
    if x == 10:
        return x10
    O = fill(x5, BLACK, x10)
    return O

def solve_fafffa47_one(S, I):
    return fill(canvas(BLACK, shape_t(bottomhalf(I))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), intersection(f_ofcolor(vconcat(vconcat(I, I), I), BLACK), f_ofcolor(bottomhalf(I), BLACK)))


def solve_fafffa47(S, I, x=0):
    x1 = bottomhalf(I)
    if x == 1:
        return x1
    x2 = shape_t(x1)
    if x == 2:
        return x2
    x3 = canvas(BLACK, x2)
    if x == 3:
        return x3
    x4 = identity(p_g)
    if x == 4:
        return x4
    x5 = rbind(get_nth_t, F0)
    if x == 5:
        return x5
    x6 = c_zo_n(S, x4, x5)
    if x == 6:
        return x6
    x7 = vconcat(I, I)
    if x == 7:
        return x7
    x8 = vconcat(x7, I)
    if x == 8:
        return x8
    x9 = f_ofcolor(x8, BLACK)
    if x == 9:
        return x9
    x10 = f_ofcolor(x1, BLACK)
    if x == 10:
        return x10
    x11 = intersection(x9, x10)
    if x == 11:
        return x11
    O = fill(x3, x6, x11)
    return O

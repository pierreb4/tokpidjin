def solve_31d5ba1a_one(S, I):
    return fill(canvas(BLACK, shape_t(tophalf(I))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), difference(combine_f(f_ofcolor(tophalf(I), BLACK), f_ofcolor(bottomhalf(I), BLACK)), intersection(f_ofcolor(tophalf(I), BLACK), f_ofcolor(bottomhalf(I), BLACK))))


def solve_31d5ba1a(S, I, x=0):
    x1 = tophalf(I)
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
    x7 = f_ofcolor(x1, BLACK)
    if x == 7:
        return x7
    x8 = bottomhalf(I)
    if x == 8:
        return x8
    x9 = f_ofcolor(x8, BLACK)
    if x == 9:
        return x9
    x10 = combine_f(x7, x9)
    if x == 10:
        return x10
    x11 = intersection(x7, x9)
    if x == 11:
        return x11
    x12 = difference(x10, x11)
    if x == 12:
        return x12
    O = fill(x3, x6, x12)
    return O

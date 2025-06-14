def solve_3bd67248_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), shoot(astuple(decrement(decrement(height_t(I))), ONE), UP_RIGHT)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), shoot(astuple(decrement(height_t(I)), ONE), RIGHT))


def solve_3bd67248(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = height_t(I)
    if x == 4:
        return x4
    x5 = decrement(x4)
    if x == 5:
        return x5
    x6 = decrement(x5)
    if x == 6:
        return x6
    x7 = astuple(x6, ONE)
    if x == 7:
        return x7
    x8 = shoot(x7, UP_RIGHT)
    if x == 8:
        return x8
    x9 = fill(I, x3, x8)
    if x == 9:
        return x9
    x10 = rbind(get_nth_t, F1)
    if x == 10:
        return x10
    x11 = c_zo_n(S, x1, x10)
    if x == 11:
        return x11
    x12 = astuple(x5, ONE)
    if x == 12:
        return x12
    x13 = shoot(x12, RIGHT)
    if x == 13:
        return x13
    O = fill(x9, x11, x13)
    return O

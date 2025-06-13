def solve_3bd67248_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), shoot(astuple(decrement(decrement(height_t(I))), ONE), UP_RIGHT)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), shoot(astuple(decrement(height_t(I)), ONE), RIGHT))


def solve_3bd67248(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = height_t(I)
    x5 = decrement(x4)
    x6 = decrement(x5)
    x7 = astuple(x6, ONE)
    x8 = shoot(x7, UP_RIGHT)
    x9 = fill(I, x3, x8)
    x10 = rbind(get_nth_t, F1)
    x11 = c_zo_n(S, x1, x10)
    x12 = astuple(x5, ONE)
    x13 = shoot(x12, RIGHT)
    O = fill(x9, x11, x13)
    return O

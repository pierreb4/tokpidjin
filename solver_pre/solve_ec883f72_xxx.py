def solve_ec883f72_one(S, I):
    return underfill(I, other_f(remove(ZERO, palette_t(I)), color(get_arg_rank_f(o_g(I, R7), fork(multiply, height_f, width_f), F0))), combine(combine(shoot(corner(get_arg_rank_f(o_g(I, R7), fork(multiply, height_f, width_f), F0), R3), UNITY), shoot(corner(get_arg_rank_f(o_g(I, R7), fork(multiply, height_f, width_f), F0), R2), DOWN_LEFT)), combine(shoot(corner(get_arg_rank_f(o_g(I, R7), fork(multiply, height_f, width_f), F0), R1), UP_RIGHT), shoot(corner(get_arg_rank_f(o_g(I, R7), fork(multiply, height_f, width_f), F0), R0), NEG_UNITY))))


def solve_ec883f72(S, I, x=0):
    x1 = palette_t(I)
    if x == 1:
        return x1
    x2 = remove(ZERO, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R7)
    if x == 3:
        return x3
    x4 = fork(multiply, height_f, width_f)
    if x == 4:
        return x4
    x5 = get_arg_rank_f(x3, x4, F0)
    if x == 5:
        return x5
    x6 = color(x5)
    if x == 6:
        return x6
    x7 = other_f(x2, x6)
    if x == 7:
        return x7
    x8 = corner(x5, R3)
    if x == 8:
        return x8
    x9 = shoot(x8, UNITY)
    if x == 9:
        return x9
    x10 = corner(x5, R2)
    if x == 10:
        return x10
    x11 = shoot(x10, DOWN_LEFT)
    if x == 11:
        return x11
    x12 = combine(x9, x11)
    if x == 12:
        return x12
    x13 = corner(x5, R1)
    if x == 13:
        return x13
    x14 = shoot(x13, UP_RIGHT)
    if x == 14:
        return x14
    x15 = corner(x5, R0)
    if x == 15:
        return x15
    x16 = shoot(x15, NEG_UNITY)
    if x == 16:
        return x16
    x17 = combine(x14, x16)
    if x == 17:
        return x17
    x18 = combine(x12, x17)
    if x == 18:
        return x18
    O = underfill(I, x7, x18)
    return O

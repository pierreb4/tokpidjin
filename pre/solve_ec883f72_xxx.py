def solve_ec883f72_one(S, I):
    return underfill(I, other_f(remove(ZERO, palette_t(I)), color(get_arg_rank_f(o_g(I, R7), fork(multiply, height_f, width_f), F0))), combine(combine(shoot(corner(get_arg_rank_f(o_g(I, R7), fork(multiply, height_f, width_f), F0), R3), UNITY), shoot(corner(get_arg_rank_f(o_g(I, R7), fork(multiply, height_f, width_f), F0), R2), DOWN_LEFT)), combine(shoot(corner(get_arg_rank_f(o_g(I, R7), fork(multiply, height_f, width_f), F0), R1), UP_RIGHT), shoot(corner(get_arg_rank_f(o_g(I, R7), fork(multiply, height_f, width_f), F0), R0), NEG_UNITY))))


def solve_ec883f72(S, I):
    x1 = palette_t(I)
    x2 = remove(ZERO, x1)
    x3 = o_g(I, R7)
    x4 = fork(multiply, height_f, width_f)
    x5 = get_arg_rank_f(x3, x4, F0)
    x6 = color(x5)
    x7 = other_f(x2, x6)
    x8 = corner(x5, R3)
    x9 = shoot(x8, UNITY)
    x10 = corner(x5, R2)
    x11 = shoot(x10, DOWN_LEFT)
    x12 = combine(x9, x11)
    x13 = corner(x5, R1)
    x14 = shoot(x13, UP_RIGHT)
    x15 = corner(x5, R0)
    x16 = shoot(x15, NEG_UNITY)
    x17 = combine(x14, x16)
    x18 = combine(x12, x17)
    O = underfill(I, x7, x18)
    return O

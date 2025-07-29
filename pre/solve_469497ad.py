def solve_469497ad_one(S, I):
    return paint(underfill(upscale_t(I, decrement(numcolors_t(I))), TWO, combine(combine(shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R0), NEG_UNITY), shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R0), UNITY)), combine(shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R2), DOWN_LEFT), shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R2), UP_RIGHT)))), get_arg_rank_f(o_g(underfill(upscale_t(I, decrement(numcolors_t(I))), TWO, combine(combine(shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R0), NEG_UNITY), shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R0), UNITY)), combine(shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R2), DOWN_LEFT), shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R2), UP_RIGHT)))), R5), rbind(corner, R3), F0))


def solve_469497ad(S, I):
    x1 = numcolors_t(I)
    x2 = decrement(x1)
    x3 = upscale_t(I, x2)
    x4 = o_g(x3, R1)
    x5 = get_arg_rank_f(x4, size, L1)
    x6 = corner(x5, R0)
    x7 = shoot(x6, NEG_UNITY)
    x8 = shoot(x6, UNITY)
    x9 = combine(x7, x8)
    x10 = corner(x5, R2)
    x11 = shoot(x10, DOWN_LEFT)
    x12 = shoot(x10, UP_RIGHT)
    x13 = combine(x11, x12)
    x14 = combine(x9, x13)
    x15 = underfill(x3, TWO, x14)
    x16 = o_g(x15, R5)
    x17 = rbind(corner, R3)
    x18 = get_arg_rank_f(x16, x17, F0)
    O = paint(x15, x18)
    return O

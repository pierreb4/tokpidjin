def solve_469497ad_one(S, I):
    return paint(underfill(upscale_t(I, decrement(numcolors_t(I))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), combine(combine(shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R0), NEG_UNITY), shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R0), UNITY)), combine(shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R2), DOWN_LEFT), shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R2), UP_RIGHT)))), get_arg_rank_f(o_g(underfill(upscale_t(I, decrement(numcolors_t(I))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), combine(combine(shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R0), NEG_UNITY), shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R0), UNITY)), combine(shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R2), DOWN_LEFT), shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R2), UP_RIGHT)))), R5), rbind(corner, R3), F0))


def solve_469497ad(S, I):
    x1 = numcolors_t(I)
    x2 = decrement(x1)
    x3 = upscale_t(I, x2)
    x4 = identity(p_g)
    x5 = rbind(get_nth_t, F0)
    x6 = c_zo_n(S, x4, x5)
    x7 = o_g(x3, R1)
    x8 = get_arg_rank_f(x7, size, L1)
    x9 = corner(x8, R0)
    x10 = shoot(x9, NEG_UNITY)
    x11 = shoot(x9, UNITY)
    x12 = combine(x10, x11)
    x13 = corner(x8, R2)
    x14 = shoot(x13, DOWN_LEFT)
    x15 = shoot(x13, UP_RIGHT)
    x16 = combine(x14, x15)
    x17 = combine(x12, x16)
    x18 = underfill(x3, x6, x17)
    x19 = o_g(x18, R5)
    x20 = rbind(corner, R3)
    x21 = get_arg_rank_f(x19, x20, F0)
    O = paint(x18, x21)
    return O

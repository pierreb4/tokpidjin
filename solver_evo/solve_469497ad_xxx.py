def solve_469497ad_one(S, I):
    return paint(underfill(upscale_t(I, decrement(numcolors_t(I))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), combine(combine(shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R0), NEG_UNITY), shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R0), UNITY)), combine(shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R2), DOWN_LEFT), shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R2), UP_RIGHT)))), get_arg_rank_f(o_g(underfill(upscale_t(I, decrement(numcolors_t(I))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), combine(combine(shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R0), NEG_UNITY), shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R0), UNITY)), combine(shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R2), DOWN_LEFT), shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R2), UP_RIGHT)))), R5), rbind(corner, R3), F0))


def solve_469497ad(S, I, x=0):
    x1 = numcolors_t(I)
    if x == 1:
        return x1
    x2 = decrement(x1)
    if x == 2:
        return x2
    x3 = upscale_t(I, x2)
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
    x7 = o_g(x3, R1)
    if x == 7:
        return x7
    x8 = get_arg_rank_f(x7, size, L1)
    if x == 8:
        return x8
    x9 = corner(x8, R0)
    if x == 9:
        return x9
    x10 = shoot(x9, NEG_UNITY)
    if x == 10:
        return x10
    x11 = shoot(x9, UNITY)
    if x == 11:
        return x11
    x12 = combine(x10, x11)
    if x == 12:
        return x12
    x13 = corner(x8, R2)
    if x == 13:
        return x13
    x14 = shoot(x13, DOWN_LEFT)
    if x == 14:
        return x14
    x15 = shoot(x13, UP_RIGHT)
    if x == 15:
        return x15
    x16 = combine(x14, x15)
    if x == 16:
        return x16
    x17 = combine(x12, x16)
    if x == 17:
        return x17
    x18 = underfill(x3, x6, x17)
    if x == 18:
        return x18
    x19 = o_g(x18, R5)
    if x == 19:
        return x19
    x20 = rbind(corner, R3)
    if x == 20:
        return x20
    x21 = get_arg_rank_f(x19, x20, F0)
    if x == 21:
        return x21
    O = paint(x18, x21)
    return O

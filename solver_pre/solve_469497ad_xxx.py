def solve_469497ad_one(S, I):
    return paint(underfill(upscale_t(I, decrement(numcolors_t(I))), TWO, combine(combine(shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R0), NEG_UNITY), shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R0), UNITY)), combine(shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R2), DOWN_LEFT), shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R2), UP_RIGHT)))), get_arg_rank_f(o_g(underfill(upscale_t(I, decrement(numcolors_t(I))), TWO, combine(combine(shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R0), NEG_UNITY), shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R0), UNITY)), combine(shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R2), DOWN_LEFT), shoot(corner(get_arg_rank_f(o_g(upscale_t(I, decrement(numcolors_t(I))), R1), size, L1), R2), UP_RIGHT)))), R5), rbind(corner, R3), F0))


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
    x4 = o_g(x3, R1)
    if x == 4:
        return x4
    x5 = get_arg_rank_f(x4, size, L1)
    if x == 5:
        return x5
    x6 = corner(x5, R0)
    if x == 6:
        return x6
    x7 = shoot(x6, NEG_UNITY)
    if x == 7:
        return x7
    x8 = shoot(x6, UNITY)
    if x == 8:
        return x8
    x9 = combine(x7, x8)
    if x == 9:
        return x9
    x10 = corner(x5, R2)
    if x == 10:
        return x10
    x11 = shoot(x10, DOWN_LEFT)
    if x == 11:
        return x11
    x12 = shoot(x10, UP_RIGHT)
    if x == 12:
        return x12
    x13 = combine(x11, x12)
    if x == 13:
        return x13
    x14 = combine(x9, x13)
    if x == 14:
        return x14
    x15 = underfill(x3, TWO, x14)
    if x == 15:
        return x15
    x16 = o_g(x15, R5)
    if x == 16:
        return x16
    x17 = rbind(corner, R3)
    if x == 17:
        return x17
    x18 = get_arg_rank_f(x16, x17, F0)
    if x == 18:
        return x18
    O = paint(x15, x18)
    return O

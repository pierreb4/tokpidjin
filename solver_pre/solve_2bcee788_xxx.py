def solve_2bcee788_one(S, I):
    return paint(replace(I, get_color_rank_t(I, F0), THREE), shift(sfilter_f(asobject(branch(hline_o(get_arg_rank_f(o_g(I, R5), size, L1)), mir_rot_t(subgrid(get_arg_rank_f(o_g(I, R5), size, F0), replace(I, get_color_rank_t(I, F0), THREE)), R0), mir_rot_t(subgrid(get_arg_rank_f(o_g(I, R5), size, F0), replace(I, get_color_rank_t(I, F0), THREE)), R2))), compose(flip, matcher(rbind(get_nth_f, F0), THREE))), add(corner(get_arg_rank_f(o_g(I, R5), size, F0), R0), multiply(shape_f(get_arg_rank_f(o_g(I, R5), size, F0)), astuple(branch(hline_o(get_arg_rank_f(o_g(I, R5), size, L1)), get_nth_t(position(get_arg_rank_f(o_g(I, R5), size, F0), get_arg_rank_f(o_g(I, R5), size, L1)), F0), ZERO), branch(hline_o(get_arg_rank_f(o_g(I, R5), size, L1)), ZERO, get_nth_t(position(get_arg_rank_f(o_g(I, R5), size, F0), get_arg_rank_f(o_g(I, R5), size, L1)), L1)))))))


def solve_2bcee788(S, I, x=0):
    x1 = get_color_rank_t(I, F0)
    if x == 1:
        return x1
    x2 = replace(I, x1, THREE)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x3, size, L1)
    if x == 4:
        return x4
    x5 = hline_o(x4)
    if x == 5:
        return x5
    x6 = get_arg_rank_f(x3, size, F0)
    if x == 6:
        return x6
    x7 = subgrid(x6, x2)
    if x == 7:
        return x7
    x8 = mir_rot_t(x7, R0)
    if x == 8:
        return x8
    x9 = mir_rot_t(x7, R2)
    if x == 9:
        return x9
    x10 = branch(x5, x8, x9)
    if x == 10:
        return x10
    x11 = asobject(x10)
    if x == 11:
        return x11
    x12 = rbind(get_nth_f, F0)
    if x == 12:
        return x12
    x13 = matcher(x12, THREE)
    if x == 13:
        return x13
    x14 = compose(flip, x13)
    if x == 14:
        return x14
    x15 = sfilter_f(x11, x14)
    if x == 15:
        return x15
    x16 = corner(x6, R0)
    if x == 16:
        return x16
    x17 = shape_f(x6)
    if x == 17:
        return x17
    x18 = position(x6, x4)
    if x == 18:
        return x18
    x19 = get_nth_t(x18, F0)
    if x == 19:
        return x19
    x20 = branch(x5, x19, ZERO)
    if x == 20:
        return x20
    x21 = get_nth_t(x18, L1)
    if x == 21:
        return x21
    x22 = branch(x5, ZERO, x21)
    if x == 22:
        return x22
    x23 = astuple(x20, x22)
    if x == 23:
        return x23
    x24 = multiply(x17, x23)
    if x == 24:
        return x24
    x25 = add(x16, x24)
    if x == 25:
        return x25
    x26 = shift(x15, x25)
    if x == 26:
        return x26
    O = paint(x2, x26)
    return O

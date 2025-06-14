def solve_b190f7f5_one(S, I):
    return fill(upscale_t(get_arg_rank_t(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t, F0), width_t(get_arg_rank_t(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t, F0))), ZERO, f_ofcolor(chain(rbind(mir_rot_t, R1), merge, rbind(repeat, width_t(get_arg_rank_t(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t, F0))))(chain(rbind(mir_rot_t, R1), merge, rbind(repeat, width_t(get_arg_rank_t(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t, F0))))(get_arg_rank_t(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t, L1))), ZERO))


def solve_b190f7f5(S, I, x=0):
    x1 = portrait_t(I)
    if x == 1:
        return x1
    x2 = branch(x1, vsplit, hsplit)
    if x == 2:
        return x2
    x3 = x2(I, TWO)
    if x == 3:
        return x3
    x4 = get_arg_rank_t(x3, numcolors_t, F0)
    if x == 4:
        return x4
    x5 = width_t(x4)
    if x == 5:
        return x5
    x6 = upscale_t(x4, x5)
    if x == 6:
        return x6
    x7 = rbind(mir_rot_t, R1)
    if x == 7:
        return x7
    x8 = rbind(repeat, x5)
    if x == 8:
        return x8
    x9 = chain(x7, merge, x8)
    if x == 9:
        return x9
    x10 = get_arg_rank_t(x3, numcolors_t, L1)
    if x == 10:
        return x10
    x11 = x9(x10)
    if x == 11:
        return x11
    x12 = x9(x11)
    if x == 12:
        return x12
    x13 = f_ofcolor(x12, ZERO)
    if x == 13:
        return x13
    O = fill(x6, ZERO, x13)
    return O

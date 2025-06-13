def solve_b190f7f5_one(S, I):
    return fill(upscale_t(get_arg_rank_t(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t, F0), width_t(get_arg_rank_t(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t, F0))), BLACK, f_ofcolor(chain(rbind(mir_rot_t, R1), merge, rbind(repeat, width_t(get_arg_rank_t(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t, F0))))(chain(rbind(mir_rot_t, R1), merge, rbind(repeat, width_t(get_arg_rank_t(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t, F0))))(get_arg_rank_t(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t, L1))), BLACK))


def solve_b190f7f5(S, I):
    x1 = portrait_t(I)
    x2 = branch(x1, vsplit, hsplit)
    x3 = x2(I, TWO)
    x4 = get_arg_rank_t(x3, numcolors_t, F0)
    x5 = width_t(x4)
    x6 = upscale_t(x4, x5)
    x7 = rbind(mir_rot_t, R1)
    x8 = rbind(repeat, x5)
    x9 = chain(x7, merge, x8)
    x10 = get_arg_rank_t(x3, numcolors_t, L1)
    x11 = x9(x10)
    x12 = x9(x11)
    x13 = f_ofcolor(x12, BLACK)
    O = fill(x6, BLACK, x13)
    return O

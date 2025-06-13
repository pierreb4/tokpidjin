def solve_f8c80d96_one(S, I):
    return replace(fill(fill(fill(I, get_color_rank_t(I, L1), chain(outbox, outbox, branch(equality(size_f(get_arg_rank_f(o_g(I, R4), width_f, L1)), BLUE), identity, outbox))(get_arg_rank_f(colorfilter(o_g(I, R4), get_color_rank_t(I, L1)), size, F0))), get_color_rank_t(I, L1), power(chain(outbox, outbox, branch(equality(size_f(get_arg_rank_f(o_g(I, R4), width_f, L1)), BLUE), identity, outbox)), TWO)(get_arg_rank_f(colorfilter(o_g(I, R4), get_color_rank_t(I, L1)), size, F0))), get_color_rank_t(I, L1), power(chain(outbox, outbox, branch(equality(size_f(get_arg_rank_f(o_g(I, R4), width_f, L1)), BLUE), identity, outbox)), THREE)(get_arg_rank_f(colorfilter(o_g(I, R4), get_color_rank_t(I, L1)), size, F0))), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)))


def solve_f8c80d96(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = o_g(I, R4)
    x3 = get_arg_rank_f(x2, width_f, L1)
    x4 = size_f(x3)
    x5 = equality(x4, BLUE)
    x6 = branch(x5, identity, outbox)
    x7 = chain(outbox, outbox, x6)
    x8 = colorfilter(x2, x1)
    x9 = get_arg_rank_f(x8, size, F0)
    x10 = x7(x9)
    x11 = fill(I, x1, x10)
    x12 = power(x7, TWO)
    x13 = x12(x9)
    x14 = fill(x11, x1, x13)
    x15 = power(x7, THREE)
    x16 = x15(x9)
    x17 = fill(x14, x1, x16)
    x18 = identity(p_g)
    x19 = rbind(get_nth_t, F0)
    x20 = c_iz_n(S, x18, x19)
    x21 = c_zo_n(S, x18, x19)
    O = replace(x17, x20, x21)
    return O

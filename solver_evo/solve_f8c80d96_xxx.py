def solve_f8c80d96_one(S, I):
    return replace(fill(fill(fill(I, get_color_rank_t(I, L1), chain(outbox, outbox, branch(equality(size_f(get_arg_rank_f(o_g(I, R4), width_f, L1)), BLUE), identity, outbox))(get_arg_rank_f(colorfilter(o_g(I, R4), get_color_rank_t(I, L1)), size, F0))), get_color_rank_t(I, L1), power(chain(outbox, outbox, branch(equality(size_f(get_arg_rank_f(o_g(I, R4), width_f, L1)), BLUE), identity, outbox)), TWO)(get_arg_rank_f(colorfilter(o_g(I, R4), get_color_rank_t(I, L1)), size, F0))), get_color_rank_t(I, L1), power(chain(outbox, outbox, branch(equality(size_f(get_arg_rank_f(o_g(I, R4), width_f, L1)), BLUE), identity, outbox)), THREE)(get_arg_rank_f(colorfilter(o_g(I, R4), get_color_rank_t(I, L1)), size, F0))), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)))


def solve_f8c80d96(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = o_g(I, R4)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x2, width_f, L1)
    if x == 3:
        return x3
    x4 = size_f(x3)
    if x == 4:
        return x4
    x5 = equality(x4, BLUE)
    if x == 5:
        return x5
    x6 = branch(x5, identity, outbox)
    if x == 6:
        return x6
    x7 = chain(outbox, outbox, x6)
    if x == 7:
        return x7
    x8 = colorfilter(x2, x1)
    if x == 8:
        return x8
    x9 = get_arg_rank_f(x8, size, F0)
    if x == 9:
        return x9
    x10 = x7(x9)
    if x == 10:
        return x10
    x11 = fill(I, x1, x10)
    if x == 11:
        return x11
    x12 = power(x7, TWO)
    if x == 12:
        return x12
    x13 = x12(x9)
    if x == 13:
        return x13
    x14 = fill(x11, x1, x13)
    if x == 14:
        return x14
    x15 = power(x7, THREE)
    if x == 15:
        return x15
    x16 = x15(x9)
    if x == 16:
        return x16
    x17 = fill(x14, x1, x16)
    if x == 17:
        return x17
    x18 = identity(p_g)
    if x == 18:
        return x18
    x19 = rbind(get_nth_t, F0)
    if x == 19:
        return x19
    x20 = c_iz_n(S, x18, x19)
    if x == 20:
        return x20
    x21 = c_zo_n(S, x18, x19)
    if x == 21:
        return x21
    O = replace(x17, x20, x21)
    return O

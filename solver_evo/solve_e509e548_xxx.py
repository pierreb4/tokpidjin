def solve_e509e548_one(S, I):
    return fill(fill(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), mfilter_f(o_g(I, R5), compose(lbind(contained, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), chain(palette_t, trim, rbind(subgrid, I))))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(o_g(I, R5), fork(equality, size, compose(decrement, fork(add, height_f, width_f)))))


def solve_e509e548(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_iz_n(S, x1, x2)
    x4 = rbind(get_nth_t, F2)
    x5 = c_zo_n(S, x1, x4)
    x6 = replace(I, x3, x5)
    x7 = rbind(get_nth_t, F1)
    x8 = c_zo_n(S, x1, x7)
    x9 = o_g(I, R5)
    x10 = lbind(contained, x3)
    x11 = rbind(subgrid, I)
    x12 = chain(palette_t, trim, x11)
    x13 = compose(x10, x12)
    x14 = mfilter_f(x9, x13)
    x15 = fill(x6, x8, x14)
    x16 = c_zo_n(S, x1, x2)
    x17 = fork(add, height_f, width_f)
    x18 = compose(decrement, x17)
    x19 = fork(equality, size, x18)
    x20 = mfilter_f(x9, x19)
    O = fill(x15, x16, x20)
    return O

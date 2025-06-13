def solve_7b6016b9_one(S, I):
    return replace(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(o_g(I, R4), compose(flip, rbind(bordering, I)))), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)))


def solve_7b6016b9(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = o_g(I, R4)
    x5 = rbind(bordering, I)
    x6 = compose(flip, x5)
    x7 = mfilter_f(x4, x6)
    x8 = fill(I, x3, x7)
    x9 = c_iz_n(S, x1, x2)
    x10 = rbind(get_nth_t, F1)
    x11 = c_zo_n(S, x1, x10)
    O = replace(x8, x9, x11)
    return O

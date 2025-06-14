def solve_7b6016b9_one(S, I):
    return replace(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(o_g(I, R4), compose(flip, rbind(bordering, I)))), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)))


def solve_7b6016b9(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R4)
    if x == 4:
        return x4
    x5 = rbind(bordering, I)
    if x == 5:
        return x5
    x6 = compose(flip, x5)
    if x == 6:
        return x6
    x7 = mfilter_f(x4, x6)
    if x == 7:
        return x7
    x8 = fill(I, x3, x7)
    if x == 8:
        return x8
    x9 = c_iz_n(S, x1, x2)
    if x == 9:
        return x9
    x10 = rbind(get_nth_t, F1)
    if x == 10:
        return x10
    x11 = c_zo_n(S, x1, x10)
    if x == 11:
        return x11
    O = replace(x8, x9, x11)
    return O

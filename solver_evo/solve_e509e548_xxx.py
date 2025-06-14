def solve_e509e548_one(S, I):
    return fill(fill(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), mfilter_f(o_g(I, R5), compose(lbind(contained, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), chain(palette_t, trim, rbind(subgrid, I))))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(o_g(I, R5), fork(equality, size, compose(decrement, fork(add, height_f, width_f)))))


def solve_e509e548(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_iz_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = rbind(get_nth_t, F2)
    if x == 4:
        return x4
    x5 = c_zo_n(S, x1, x4)
    if x == 5:
        return x5
    x6 = replace(I, x3, x5)
    if x == 6:
        return x6
    x7 = rbind(get_nth_t, F1)
    if x == 7:
        return x7
    x8 = c_zo_n(S, x1, x7)
    if x == 8:
        return x8
    x9 = o_g(I, R5)
    if x == 9:
        return x9
    x10 = lbind(contained, x3)
    if x == 10:
        return x10
    x11 = rbind(subgrid, I)
    if x == 11:
        return x11
    x12 = chain(palette_t, trim, x11)
    if x == 12:
        return x12
    x13 = compose(x10, x12)
    if x == 13:
        return x13
    x14 = mfilter_f(x9, x13)
    if x == 14:
        return x14
    x15 = fill(x6, x8, x14)
    if x == 15:
        return x15
    x16 = c_zo_n(S, x1, x2)
    if x == 16:
        return x16
    x17 = fork(add, height_f, width_f)
    if x == 17:
        return x17
    x18 = compose(decrement, x17)
    if x == 18:
        return x18
    x19 = fork(equality, size, x18)
    if x == 19:
        return x19
    x20 = mfilter_f(x9, x19)
    if x == 20:
        return x20
    O = fill(x15, x16, x20)
    return O

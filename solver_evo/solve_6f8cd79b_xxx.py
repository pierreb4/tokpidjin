def solve_6f8cd79b_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(apply(initset, asindices(I)), rbind(bordering, I)))


def solve_6f8cd79b(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = asindices(I)
    if x == 4:
        return x4
    x5 = apply(initset, x4)
    if x == 5:
        return x5
    x6 = rbind(bordering, I)
    if x == 6:
        return x6
    x7 = mfilter_f(x5, x6)
    if x == 7:
        return x7
    O = fill(I, x3, x7)
    return O

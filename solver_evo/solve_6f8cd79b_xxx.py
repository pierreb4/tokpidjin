def solve_6f8cd79b_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(apply(initset, asindices(I)), rbind(bordering, I)))


def solve_6f8cd79b(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = asindices(I)
    x5 = apply(initset, x4)
    x6 = rbind(bordering, I)
    x7 = mfilter_f(x5, x6)
    O = fill(I, x3, x7)
    return O

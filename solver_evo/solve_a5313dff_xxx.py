def solve_a5313dff_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I))))


def solve_a5313dff(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = o_g(I, R4)
    x5 = colorfilter(x4, BLACK)
    x6 = rbind(bordering, I)
    x7 = compose(flip, x6)
    x8 = mfilter_f(x5, x7)
    O = fill(I, x3, x8)
    return O

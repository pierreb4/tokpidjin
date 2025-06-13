def solve_b2862040_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(colorfilter(o_g(I, R4), BLUE), rbind(adjacent, mfilter_f(colorfilter(o_g(I, R4), BURGUNDY), compose(flip, rbind(bordering, I))))))


def solve_b2862040(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = o_g(I, R4)
    x5 = colorfilter(x4, BLUE)
    x6 = colorfilter(x4, BURGUNDY)
    x7 = rbind(bordering, I)
    x8 = compose(flip, x7)
    x9 = mfilter_f(x6, x8)
    x10 = rbind(adjacent, x9)
    x11 = mfilter_f(x5, x10)
    O = fill(I, x3, x11)
    return O

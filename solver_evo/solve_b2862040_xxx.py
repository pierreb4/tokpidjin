def solve_b2862040_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(colorfilter(o_g(I, R4), BLUE), rbind(adjacent, mfilter_f(colorfilter(o_g(I, R4), BURGUNDY), compose(flip, rbind(bordering, I))))))


def solve_b2862040(S, I, x=0):
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
    x5 = colorfilter(x4, BLUE)
    if x == 5:
        return x5
    x6 = colorfilter(x4, BURGUNDY)
    if x == 6:
        return x6
    x7 = rbind(bordering, I)
    if x == 7:
        return x7
    x8 = compose(flip, x7)
    if x == 8:
        return x8
    x9 = mfilter_f(x6, x8)
    if x == 9:
        return x9
    x10 = rbind(adjacent, x9)
    if x == 10:
        return x10
    x11 = mfilter_f(x5, x10)
    if x == 11:
        return x11
    O = fill(I, x3, x11)
    return O

def solve_b2862040_one(S, I):
    return fill(I, EIGHT, mfilter_f(colorfilter(o_g(I, R4), ONE), rbind(adjacent, mfilter_f(colorfilter(o_g(I, R4), NINE), compose(flip, rbind(bordering, I))))))


def solve_b2862040(S, I):
    x1 = o_g(I, R4)
    x2 = colorfilter(x1, ONE)
    x3 = colorfilter(x1, NINE)
    x4 = rbind(bordering, I)
    x5 = compose(flip, x4)
    x6 = mfilter_f(x3, x5)
    x7 = rbind(adjacent, x6)
    x8 = mfilter_f(x2, x7)
    O = fill(I, EIGHT, x8)
    return O

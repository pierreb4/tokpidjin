def solve_b2862040_one(S, I):
    return fill(I, EIGHT, mfilter_f(colorfilter(o_g(I, R4), ONE), rbind(adjacent, mfilter_f(colorfilter(o_g(I, R4), NINE), compose(flip, rbind(bordering, I))))))


def solve_b2862040(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ONE)
    if x == 2:
        return x2
    x3 = colorfilter(x1, NINE)
    if x == 3:
        return x3
    x4 = rbind(bordering, I)
    if x == 4:
        return x4
    x5 = compose(flip, x4)
    if x == 5:
        return x5
    x6 = mfilter_f(x3, x5)
    if x == 6:
        return x6
    x7 = rbind(adjacent, x6)
    if x == 7:
        return x7
    x8 = mfilter_f(x2, x7)
    if x == 8:
        return x8
    O = fill(I, EIGHT, x8)
    return O

def solve_a5313dff_one(S, I):
    return fill(I, ONE, mfilter_f(colorfilter(o_g(I, R4), ZERO), compose(flip, rbind(bordering, I))))


def solve_a5313dff(S, I):
    x1 = o_g(I, R4)
    x2 = colorfilter(x1, ZERO)
    x3 = rbind(bordering, I)
    x4 = compose(flip, x3)
    x5 = mfilter_f(x2, x4)
    O = fill(I, ONE, x5)
    return O

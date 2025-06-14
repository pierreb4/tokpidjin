def solve_a5313dff_one(S, I):
    return fill(I, ONE, mfilter_f(colorfilter(o_g(I, R4), ZERO), compose(flip, rbind(bordering, I))))


def solve_a5313dff(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = rbind(bordering, I)
    if x == 3:
        return x3
    x4 = compose(flip, x3)
    if x == 4:
        return x4
    x5 = mfilter_f(x2, x4)
    if x == 5:
        return x5
    O = fill(I, ONE, x5)
    return O

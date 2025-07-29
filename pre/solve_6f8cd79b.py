def solve_6f8cd79b_one(S, I):
    return fill(I, EIGHT, mfilter_f(apply(initset, asindices(I)), rbind(bordering, I)))


def solve_6f8cd79b(S, I):
    x1 = asindices(I)
    x2 = apply(initset, x1)
    x3 = rbind(bordering, I)
    x4 = mfilter_f(x2, x3)
    O = fill(I, EIGHT, x4)
    return O

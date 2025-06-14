def solve_6f8cd79b_one(S, I):
    return fill(I, EIGHT, mfilter_f(apply(initset, asindices(I)), rbind(bordering, I)))


def solve_6f8cd79b(S, I, x=0):
    x1 = asindices(I)
    if x == 1:
        return x1
    x2 = apply(initset, x1)
    if x == 2:
        return x2
    x3 = rbind(bordering, I)
    if x == 3:
        return x3
    x4 = mfilter_f(x2, x3)
    if x == 4:
        return x4
    O = fill(I, EIGHT, x4)
    return O

def solve_7b6016b9_one(S, I):
    return replace(fill(I, TWO, mfilter_f(o_g(I, R4), compose(flip, rbind(bordering, I)))), ZERO, THREE)


def solve_7b6016b9(S, I):
    x1 = o_g(I, R4)
    x2 = rbind(bordering, I)
    x3 = compose(flip, x2)
    x4 = mfilter_f(x1, x3)
    x5 = fill(I, TWO, x4)
    O = replace(x5, ZERO, THREE)
    return O

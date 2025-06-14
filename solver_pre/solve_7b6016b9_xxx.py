def solve_7b6016b9_one(S, I):
    return replace(fill(I, TWO, mfilter_f(o_g(I, R4), compose(flip, rbind(bordering, I)))), ZERO, THREE)


def solve_7b6016b9(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = rbind(bordering, I)
    if x == 2:
        return x2
    x3 = compose(flip, x2)
    if x == 3:
        return x3
    x4 = mfilter_f(x1, x3)
    if x == 4:
        return x4
    x5 = fill(I, TWO, x4)
    if x == 5:
        return x5
    O = replace(x5, ZERO, THREE)
    return O

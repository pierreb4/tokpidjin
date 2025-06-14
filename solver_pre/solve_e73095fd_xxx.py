def solve_e73095fd_one(S, I):
    return fill(I, FOUR, mfilter_f(sfilter_f(colorfilter(o_g(I, R4), ZERO), fork(equality, toindices, backdrop)), chain(matcher(size, ZERO), rbind(intersection, f_ofcolor(I, FIVE)), fork(difference, chain(lbind(mapply, dneighbors), corners, outbox), outbox))))


def solve_e73095fd(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = fork(equality, toindices, backdrop)
    if x == 3:
        return x3
    x4 = sfilter_f(x2, x3)
    if x == 4:
        return x4
    x5 = matcher(size, ZERO)
    if x == 5:
        return x5
    x6 = f_ofcolor(I, FIVE)
    if x == 6:
        return x6
    x7 = rbind(intersection, x6)
    if x == 7:
        return x7
    x8 = lbind(mapply, dneighbors)
    if x == 8:
        return x8
    x9 = chain(x8, corners, outbox)
    if x == 9:
        return x9
    x10 = fork(difference, x9, outbox)
    if x == 10:
        return x10
    x11 = chain(x5, x7, x10)
    if x == 11:
        return x11
    x12 = mfilter_f(x4, x11)
    if x == 12:
        return x12
    O = fill(I, FOUR, x12)
    return O

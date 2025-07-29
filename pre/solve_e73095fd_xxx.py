def solve_e73095fd_one(S, I):
    return fill(I, FOUR, mfilter_f(sfilter_f(colorfilter(o_g(I, R4), ZERO), fork(equality, toindices, backdrop)), chain(matcher(size, ZERO), rbind(intersection, f_ofcolor(I, FIVE)), fork(difference, chain(lbind(mapply, dneighbors), corners, outbox), outbox))))


def solve_e73095fd(S, I):
    x1 = o_g(I, R4)
    x2 = colorfilter(x1, ZERO)
    x3 = fork(equality, toindices, backdrop)
    x4 = sfilter_f(x2, x3)
    x5 = matcher(size, ZERO)
    x6 = f_ofcolor(I, FIVE)
    x7 = rbind(intersection, x6)
    x8 = lbind(mapply, dneighbors)
    x9 = chain(x8, corners, outbox)
    x10 = fork(difference, x9, outbox)
    x11 = chain(x5, x7, x10)
    x12 = mfilter_f(x4, x11)
    O = fill(I, FOUR, x12)
    return O

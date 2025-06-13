def solve_e73095fd_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), fork(equality, toindices, backdrop)), chain(matcher(size, BLACK), rbind(intersection, f_ofcolor(I, GRAY)), fork(difference, chain(lbind(mapply, dneighbors), corners, outbox), outbox))))


def solve_e73095fd(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = o_g(I, R4)
    x5 = colorfilter(x4, BLACK)
    x6 = fork(equality, toindices, backdrop)
    x7 = sfilter_f(x5, x6)
    x8 = matcher(size, BLACK)
    x9 = f_ofcolor(I, GRAY)
    x10 = rbind(intersection, x9)
    x11 = lbind(mapply, dneighbors)
    x12 = chain(x11, corners, outbox)
    x13 = fork(difference, x12, outbox)
    x14 = chain(x8, x10, x13)
    x15 = mfilter_f(x7, x14)
    O = fill(I, x3, x15)
    return O

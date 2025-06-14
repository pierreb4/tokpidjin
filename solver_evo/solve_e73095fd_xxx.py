def solve_e73095fd_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), fork(equality, toindices, backdrop)), chain(matcher(size, BLACK), rbind(intersection, f_ofcolor(I, GRAY)), fork(difference, chain(lbind(mapply, dneighbors), corners, outbox), outbox))))


def solve_e73095fd(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R4)
    if x == 4:
        return x4
    x5 = colorfilter(x4, BLACK)
    if x == 5:
        return x5
    x6 = fork(equality, toindices, backdrop)
    if x == 6:
        return x6
    x7 = sfilter_f(x5, x6)
    if x == 7:
        return x7
    x8 = matcher(size, BLACK)
    if x == 8:
        return x8
    x9 = f_ofcolor(I, GRAY)
    if x == 9:
        return x9
    x10 = rbind(intersection, x9)
    if x == 10:
        return x10
    x11 = lbind(mapply, dneighbors)
    if x == 11:
        return x11
    x12 = chain(x11, corners, outbox)
    if x == 12:
        return x12
    x13 = fork(difference, x12, outbox)
    if x == 13:
        return x13
    x14 = chain(x8, x10, x13)
    if x == 14:
        return x14
    x15 = mfilter_f(x7, x14)
    if x == 15:
        return x15
    O = fill(I, x3, x15)
    return O

def solve_6c434453_one(S, I):
    return fill(cover(I, merge_f(sizefilter(o_g(I, R5), EIGHT))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(lbind(shift, insert(UNITY, dneighbors(UNITY))), apply(rbind(corner, R0), sizefilter(o_g(I, R5), EIGHT))))


def solve_6c434453(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, EIGHT)
    if x == 2:
        return x2
    x3 = merge_f(x2)
    if x == 3:
        return x3
    x4 = cover(I, x3)
    if x == 4:
        return x4
    x5 = identity(p_g)
    if x == 5:
        return x5
    x6 = rbind(get_nth_t, F0)
    if x == 6:
        return x6
    x7 = c_zo_n(S, x5, x6)
    if x == 7:
        return x7
    x8 = dneighbors(UNITY)
    if x == 8:
        return x8
    x9 = insert(UNITY, x8)
    if x == 9:
        return x9
    x10 = lbind(shift, x9)
    if x == 10:
        return x10
    x11 = rbind(corner, R0)
    if x == 11:
        return x11
    x12 = apply(x11, x2)
    if x == 12:
        return x12
    x13 = mapply(x10, x12)
    if x == 13:
        return x13
    O = fill(x4, x7, x13)
    return O

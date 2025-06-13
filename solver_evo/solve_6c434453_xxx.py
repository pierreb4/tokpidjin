def solve_6c434453_one(S, I):
    return fill(cover(I, merge_f(sizefilter(o_g(I, R5), EIGHT))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(lbind(shift, insert(UNITY, dneighbors(UNITY))), apply(rbind(corner, R0), sizefilter(o_g(I, R5), EIGHT))))


def solve_6c434453(S, I):
    x1 = o_g(I, R5)
    x2 = sizefilter(x1, EIGHT)
    x3 = merge_f(x2)
    x4 = cover(I, x3)
    x5 = identity(p_g)
    x6 = rbind(get_nth_t, F0)
    x7 = c_zo_n(S, x5, x6)
    x8 = dneighbors(UNITY)
    x9 = insert(UNITY, x8)
    x10 = lbind(shift, x9)
    x11 = rbind(corner, R0)
    x12 = apply(x11, x2)
    x13 = mapply(x10, x12)
    O = fill(x4, x7, x13)
    return O

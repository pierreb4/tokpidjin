def solve_6c434453_one(S, I):
    return fill(cover(I, merge_f(sizefilter(o_g(I, R5), EIGHT))), TWO, mapply(lbind(shift, insert(UNITY, dneighbors(UNITY))), apply(rbind(corner, R0), sizefilter(o_g(I, R5), EIGHT))))


def solve_6c434453(S, I):
    x1 = o_g(I, R5)
    x2 = sizefilter(x1, EIGHT)
    x3 = merge_f(x2)
    x4 = cover(I, x3)
    x5 = dneighbors(UNITY)
    x6 = insert(UNITY, x5)
    x7 = lbind(shift, x6)
    x8 = rbind(corner, R0)
    x9 = apply(x8, x2)
    x10 = mapply(x7, x9)
    O = fill(x4, TWO, x10)
    return O

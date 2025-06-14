def solve_6e19193c_one(S, I):
    return fill(fill(I, get_color_rank_t(I, L1), mapply(fork(shoot, compose(rbind(get_nth_f, F0), delta), fork(subtract, compose(rbind(get_nth_f, F0), delta), chain(rbind(get_nth_f, F0), rbind(sfilter, chain(matcher(rbind(colorcount_f, get_color_rank_t(I, L1)), RED), rbind(toobject, I), dneighbors)), toindices))), o_g(I, R5))), BLACK, mapply(delta, o_g(I, R5)))


def solve_6e19193c(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, F0)
    if x == 2:
        return x2
    x3 = compose(x2, delta)
    if x == 3:
        return x3
    x4 = rbind(colorcount_f, x1)
    if x == 4:
        return x4
    x5 = matcher(x4, RED)
    if x == 5:
        return x5
    x6 = rbind(toobject, I)
    if x == 6:
        return x6
    x7 = chain(x5, x6, dneighbors)
    if x == 7:
        return x7
    x8 = rbind(sfilter, x7)
    if x == 8:
        return x8
    x9 = chain(x2, x8, toindices)
    if x == 9:
        return x9
    x10 = fork(subtract, x3, x9)
    if x == 10:
        return x10
    x11 = fork(shoot, x3, x10)
    if x == 11:
        return x11
    x12 = o_g(I, R5)
    if x == 12:
        return x12
    x13 = mapply(x11, x12)
    if x == 13:
        return x13
    x14 = fill(I, x1, x13)
    if x == 14:
        return x14
    x15 = mapply(delta, x12)
    if x == 15:
        return x15
    O = fill(x14, BLACK, x15)
    return O

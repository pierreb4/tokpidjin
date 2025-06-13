def solve_6e19193c_one(S, I):
    return fill(fill(I, get_color_rank_t(I, L1), mapply(fork(shoot, compose(rbind(get_nth_f, F0), delta), fork(subtract, compose(rbind(get_nth_f, F0), delta), chain(rbind(get_nth_f, F0), rbind(sfilter, chain(matcher(rbind(colorcount_f, get_color_rank_t(I, L1)), RED), rbind(toobject, I), dneighbors)), toindices))), o_g(I, R5))), BLACK, mapply(delta, o_g(I, R5)))


def solve_6e19193c(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = rbind(get_nth_f, F0)
    x3 = compose(x2, delta)
    x4 = rbind(colorcount_f, x1)
    x5 = matcher(x4, RED)
    x6 = rbind(toobject, I)
    x7 = chain(x5, x6, dneighbors)
    x8 = rbind(sfilter, x7)
    x9 = chain(x2, x8, toindices)
    x10 = fork(subtract, x3, x9)
    x11 = fork(shoot, x3, x10)
    x12 = o_g(I, R5)
    x13 = mapply(x11, x12)
    x14 = fill(I, x1, x13)
    x15 = mapply(delta, x12)
    O = fill(x14, BLACK, x15)
    return O

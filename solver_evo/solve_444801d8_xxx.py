def solve_444801d8_one(S, I):
    return underpaint(I, mapply(fork(recolor_i, chain(rbind(get_color_rank_f, L1), rbind(toobject, I), delta), compose(rbind(shift, UP), backdrop)), colorfilter(o_g(I, R5), BLUE)))


def solve_444801d8(S, I):
    x1 = rbind(get_color_rank_f, L1)
    x2 = rbind(toobject, I)
    x3 = chain(x1, x2, delta)
    x4 = rbind(shift, UP)
    x5 = compose(x4, backdrop)
    x6 = fork(recolor_i, x3, x5)
    x7 = o_g(I, R5)
    x8 = colorfilter(x7, BLUE)
    x9 = mapply(x6, x8)
    O = underpaint(I, x9)
    return O

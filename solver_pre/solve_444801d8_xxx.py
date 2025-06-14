def solve_444801d8_one(S, I):
    return underpaint(I, mapply(fork(recolor_i, chain(rbind(get_color_rank_f, L1), rbind(toobject, I), delta), compose(rbind(shift, UP), backdrop)), colorfilter(o_g(I, R5), ONE)))


def solve_444801d8(S, I, x=0):
    x1 = rbind(get_color_rank_f, L1)
    if x == 1:
        return x1
    x2 = rbind(toobject, I)
    if x == 2:
        return x2
    x3 = chain(x1, x2, delta)
    if x == 3:
        return x3
    x4 = rbind(shift, UP)
    if x == 4:
        return x4
    x5 = compose(x4, backdrop)
    if x == 5:
        return x5
    x6 = fork(recolor_i, x3, x5)
    if x == 6:
        return x6
    x7 = o_g(I, R5)
    if x == 7:
        return x7
    x8 = colorfilter(x7, ONE)
    if x == 8:
        return x8
    x9 = mapply(x6, x8)
    if x == 9:
        return x9
    O = underpaint(I, x9)
    return O

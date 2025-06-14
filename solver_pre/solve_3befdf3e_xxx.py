def solve_3befdf3e_one(S, I):
    return fill(underfill(switch(I, get_color_rank_t(I, L1), other_f(remove(ZERO, palette_t(I)), get_color_rank_t(I, L1))), other_f(remove(ZERO, palette_t(I)), get_color_rank_t(I, L1)), mapply(compose(backdrop, compose(rbind(get_nth_f, F0), fork(rapply, chain(initset, rbind(get_nth_f, F0), lbind(rapply, initset(compose(lbind(power, outbox), compose(width_f, inbox))))), identity))), o_g(I, R1))), ZERO, mapply(fork(intersection, compose(backdrop, compose(rbind(get_nth_f, F0), fork(rapply, chain(initset, rbind(get_nth_f, F0), lbind(rapply, initset(compose(lbind(power, outbox), compose(width_f, inbox))))), identity))), fork(mapply, compose(lbind(lbind(chain, backdrop), inbox), compose(lbind(power, outbox), compose(width_f, inbox))), chain(lbind(apply, initset), corners, compose(backdrop, compose(rbind(get_nth_f, F0), fork(rapply, chain(initset, rbind(get_nth_f, F0), lbind(rapply, initset(compose(lbind(power, outbox), compose(width_f, inbox))))), identity)))))), o_g(I, R1)))


def solve_3befdf3e(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = palette_t(I)
    if x == 2:
        return x2
    x3 = remove(ZERO, x2)
    if x == 3:
        return x3
    x4 = other_f(x3, x1)
    if x == 4:
        return x4
    x5 = switch(I, x1, x4)
    if x == 5:
        return x5
    x6 = rbind(get_nth_f, F0)
    if x == 6:
        return x6
    x7 = lbind(power, outbox)
    if x == 7:
        return x7
    x8 = compose(width_f, inbox)
    if x == 8:
        return x8
    x9 = compose(x7, x8)
    if x == 9:
        return x9
    x10 = initset(x9)
    if x == 10:
        return x10
    x11 = lbind(rapply, x10)
    if x == 11:
        return x11
    x12 = chain(initset, x6, x11)
    if x == 12:
        return x12
    x13 = fork(rapply, x12, identity)
    if x == 13:
        return x13
    x14 = compose(x6, x13)
    if x == 14:
        return x14
    x15 = compose(backdrop, x14)
    if x == 15:
        return x15
    x16 = o_g(I, R1)
    if x == 16:
        return x16
    x17 = mapply(x15, x16)
    if x == 17:
        return x17
    x18 = underfill(x5, x4, x17)
    if x == 18:
        return x18
    x19 = lbind(chain, backdrop)
    if x == 19:
        return x19
    x20 = lbind(x19, inbox)
    if x == 20:
        return x20
    x21 = compose(x20, x9)
    if x == 21:
        return x21
    x22 = lbind(apply, initset)
    if x == 22:
        return x22
    x23 = chain(x22, corners, x15)
    if x == 23:
        return x23
    x24 = fork(mapply, x21, x23)
    if x == 24:
        return x24
    x25 = fork(intersection, x15, x24)
    if x == 25:
        return x25
    x26 = mapply(x25, x16)
    if x == 26:
        return x26
    O = fill(x18, ZERO, x26)
    return O

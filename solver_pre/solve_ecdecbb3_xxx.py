def solve_ecdecbb3_one(S, I):
    return fill(fill(I, TWO, mfilter_f(apply(fork(connect, compose(center, rbind(get_nth_f, F0)), fork(add, compose(center, rbind(get_nth_f, F0)), compose(crement, fork(gravitate, rbind(get_nth_f, F0), rbind(get_nth_f, L1))))), product(colorfilter(o_g(I, R5), TWO), colorfilter(o_g(I, R5), EIGHT))), compose(lbind(greater, EIGHT), size))), EIGHT, mapply(neighbors, intersection(mfilter_f(apply(fork(connect, compose(center, rbind(get_nth_f, F0)), fork(add, compose(center, rbind(get_nth_f, F0)), compose(crement, fork(gravitate, rbind(get_nth_f, F0), rbind(get_nth_f, L1))))), product(colorfilter(o_g(I, R5), TWO), colorfilter(o_g(I, R5), EIGHT))), compose(lbind(greater, EIGHT), size)), apply(fork(add, compose(center, rbind(get_nth_f, F0)), compose(crement, fork(gravitate, rbind(get_nth_f, F0), rbind(get_nth_f, L1)))), product(colorfilter(o_g(I, R5), TWO), colorfilter(o_g(I, R5), EIGHT))))))


def solve_ecdecbb3(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = compose(center, x1)
    if x == 2:
        return x2
    x3 = rbind(get_nth_f, L1)
    if x == 3:
        return x3
    x4 = fork(gravitate, x1, x3)
    if x == 4:
        return x4
    x5 = compose(crement, x4)
    if x == 5:
        return x5
    x6 = fork(add, x2, x5)
    if x == 6:
        return x6
    x7 = fork(connect, x2, x6)
    if x == 7:
        return x7
    x8 = o_g(I, R5)
    if x == 8:
        return x8
    x9 = colorfilter(x8, TWO)
    if x == 9:
        return x9
    x10 = colorfilter(x8, EIGHT)
    if x == 10:
        return x10
    x11 = product(x9, x10)
    if x == 11:
        return x11
    x12 = apply(x7, x11)
    if x == 12:
        return x12
    x13 = lbind(greater, EIGHT)
    if x == 13:
        return x13
    x14 = compose(x13, size)
    if x == 14:
        return x14
    x15 = mfilter_f(x12, x14)
    if x == 15:
        return x15
    x16 = fill(I, TWO, x15)
    if x == 16:
        return x16
    x17 = apply(x6, x11)
    if x == 17:
        return x17
    x18 = intersection(x15, x17)
    if x == 18:
        return x18
    x19 = mapply(neighbors, x18)
    if x == 19:
        return x19
    O = fill(x16, EIGHT, x19)
    return O

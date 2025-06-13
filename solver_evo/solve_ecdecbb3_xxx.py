def solve_ecdecbb3_one(S, I):
    return fill(fill(I, RED, mfilter_f(apply(fork(connect, compose(center, rbind(get_nth_f, F0)), fork(add, compose(center, rbind(get_nth_f, F0)), compose(crement, fork(gravitate, rbind(get_nth_f, F0), rbind(get_nth_f, L1))))), product(colorfilter(o_g(I, R5), RED), colorfilter(o_g(I, R5), CYAN))), compose(lbind(greater, CYAN), size))), CYAN, mapply(neighbors, intersection(mfilter_f(apply(fork(connect, compose(center, rbind(get_nth_f, F0)), fork(add, compose(center, rbind(get_nth_f, F0)), compose(crement, fork(gravitate, rbind(get_nth_f, F0), rbind(get_nth_f, L1))))), product(colorfilter(o_g(I, R5), RED), colorfilter(o_g(I, R5), CYAN))), compose(lbind(greater, CYAN), size)), apply(fork(add, compose(center, rbind(get_nth_f, F0)), compose(crement, fork(gravitate, rbind(get_nth_f, F0), rbind(get_nth_f, L1)))), product(colorfilter(o_g(I, R5), RED), colorfilter(o_g(I, R5), CYAN))))))


def solve_ecdecbb3(S, I):
    x1 = rbind(get_nth_f, F0)
    x2 = compose(center, x1)
    x3 = rbind(get_nth_f, L1)
    x4 = fork(gravitate, x1, x3)
    x5 = compose(crement, x4)
    x6 = fork(add, x2, x5)
    x7 = fork(connect, x2, x6)
    x8 = o_g(I, R5)
    x9 = colorfilter(x8, RED)
    x10 = colorfilter(x8, CYAN)
    x11 = product(x9, x10)
    x12 = apply(x7, x11)
    x13 = lbind(greater, CYAN)
    x14 = compose(x13, size)
    x15 = mfilter_f(x12, x14)
    x16 = fill(I, RED, x15)
    x17 = apply(x6, x11)
    x18 = intersection(x15, x17)
    x19 = mapply(neighbors, x18)
    O = fill(x16, CYAN, x19)
    return O

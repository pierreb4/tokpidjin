def solve_3bdb4ada_one(S, I):
    return fill(I, ZERO, mapply(fork(sfilter, rbind(get_nth_f, F0), compose(lbind(compose, compose(even, fork(subtract, compose(rbind(get_nth_f, L1), rbind(get_nth_f, F0)), power(rbind(get_nth_f, L1), TWO)))), lbind(rbind, astuple))), pair(papply(connect, apply(compose(increment, rbind(corner, R0)), totuple(o_g(I, R5))), apply(compose(decrement, rbind(corner, R3)), totuple(o_g(I, R5)))), apply(rbind(get_nth_f, L1), apply(compose(increment, rbind(corner, R0)), totuple(o_g(I, R5)))))))


def solve_3bdb4ada(S, I):
    x1 = rbind(get_nth_f, F0)
    x2 = rbind(get_nth_f, L1)
    x3 = compose(x2, x1)
    x4 = power(x2, TWO)
    x5 = fork(subtract, x3, x4)
    x6 = compose(even, x5)
    x7 = lbind(compose, x6)
    x8 = lbind(rbind, astuple)
    x9 = compose(x7, x8)
    x10 = fork(sfilter, x1, x9)
    x11 = rbind(corner, R0)
    x12 = compose(increment, x11)
    x13 = o_g(I, R5)
    x14 = totuple(x13)
    x15 = apply(x12, x14)
    x16 = rbind(corner, R3)
    x17 = compose(decrement, x16)
    x18 = apply(x17, x14)
    x19 = papply(connect, x15, x18)
    x20 = apply(x2, x15)
    x21 = pair(x19, x20)
    x22 = mapply(x10, x21)
    O = fill(I, ZERO, x22)
    return O

def solve_3bdb4ada_one(S, I):
    return fill(I, ZERO, mapply(fork(sfilter, rbind(get_nth_f, F0), compose(lbind(compose, compose(even, fork(subtract, compose(rbind(get_nth_f, L1), rbind(get_nth_f, F0)), power(rbind(get_nth_f, L1), TWO)))), lbind(rbind, astuple))), pair(papply(connect, apply(compose(increment, rbind(corner, R0)), totuple(o_g(I, R5))), apply(compose(decrement, rbind(corner, R3)), totuple(o_g(I, R5)))), apply(rbind(get_nth_f, L1), apply(compose(increment, rbind(corner, R0)), totuple(o_g(I, R5)))))))


def solve_3bdb4ada(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, L1)
    if x == 2:
        return x2
    x3 = compose(x2, x1)
    if x == 3:
        return x3
    x4 = power(x2, TWO)
    if x == 4:
        return x4
    x5 = fork(subtract, x3, x4)
    if x == 5:
        return x5
    x6 = compose(even, x5)
    if x == 6:
        return x6
    x7 = lbind(compose, x6)
    if x == 7:
        return x7
    x8 = lbind(rbind, astuple)
    if x == 8:
        return x8
    x9 = compose(x7, x8)
    if x == 9:
        return x9
    x10 = fork(sfilter, x1, x9)
    if x == 10:
        return x10
    x11 = rbind(corner, R0)
    if x == 11:
        return x11
    x12 = compose(increment, x11)
    if x == 12:
        return x12
    x13 = o_g(I, R5)
    if x == 13:
        return x13
    x14 = totuple(x13)
    if x == 14:
        return x14
    x15 = apply(x12, x14)
    if x == 15:
        return x15
    x16 = rbind(corner, R3)
    if x == 16:
        return x16
    x17 = compose(decrement, x16)
    if x == 17:
        return x17
    x18 = apply(x17, x14)
    if x == 18:
        return x18
    x19 = papply(connect, x15, x18)
    if x == 19:
        return x19
    x20 = apply(x2, x15)
    if x == 20:
        return x20
    x21 = pair(x19, x20)
    if x == 21:
        return x21
    x22 = mapply(x10, x21)
    if x == 22:
        return x22
    O = fill(I, ZERO, x22)
    return O

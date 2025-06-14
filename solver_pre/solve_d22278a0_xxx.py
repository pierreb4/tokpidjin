def solve_d22278a0_one(S, I):
    return paint(I, mapply(fork(recolor_i, color, fork(intersection, fork(intersection, chain(lbind(sfilter, asindices(I)), lbind(compose, compose(chain(even, rbind(get_rank, F0), lbind(apply, fork(multiply, sign, identity))), fork(subtract, rbind(get_nth_f, F0), compose(center, rbind(get_nth_f, L1))))), lbind(rbind, astuple)), chain(lbind(sfilter, asindices(I)), rbind(compose, compose(lbind(rbind(get_arg_rank, L1), o_g(I, R5)), compose(lbind(compose, chain(fork(add, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), lbind(apply, fork(multiply, sign, identity)), fork(subtract, rbind(get_nth_f, F0), compose(center, rbind(get_nth_f, L1))))), lbind(lbind, astuple)))), lbind(rbind, equality))), compose(lbind(sfilter, asindices(I)), fork(lbind(fork, greater), chain(rbind(compose, compose(lbind(compose, chain(fork(add, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), lbind(apply, fork(multiply, sign, identity)), fork(subtract, rbind(get_nth_f, F0), compose(center, rbind(get_nth_f, L1))))), lbind(lbind, astuple))), lbind(lbind, rbind(get_val_rank, L1)), rbind(remove, o_g(I, R5))), compose(lbind(compose, chain(fork(add, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), lbind(apply, fork(multiply, sign, identity)), fork(subtract, rbind(get_nth_f, F0), compose(center, rbind(get_nth_f, L1))))), lbind(rbind, astuple)))))), o_g(I, R5)))


def solve_d22278a0(S, I, x=0):
    x1 = asindices(I)
    if x == 1:
        return x1
    x2 = lbind(sfilter, x1)
    if x == 2:
        return x2
    x3 = rbind(get_rank, F0)
    if x == 3:
        return x3
    x4 = fork(multiply, sign, identity)
    if x == 4:
        return x4
    x5 = lbind(apply, x4)
    if x == 5:
        return x5
    x6 = chain(even, x3, x5)
    if x == 6:
        return x6
    x7 = rbind(get_nth_f, F0)
    if x == 7:
        return x7
    x8 = rbind(get_nth_f, L1)
    if x == 8:
        return x8
    x9 = compose(center, x8)
    if x == 9:
        return x9
    x10 = fork(subtract, x7, x9)
    if x == 10:
        return x10
    x11 = compose(x6, x10)
    if x == 11:
        return x11
    x12 = lbind(compose, x11)
    if x == 12:
        return x12
    x13 = lbind(rbind, astuple)
    if x == 13:
        return x13
    x14 = chain(x2, x12, x13)
    if x == 14:
        return x14
    x15 = rbind(get_arg_rank, L1)
    if x == 15:
        return x15
    x16 = o_g(I, R5)
    if x == 16:
        return x16
    x17 = lbind(x15, x16)
    if x == 17:
        return x17
    x18 = fork(add, x7, x8)
    if x == 18:
        return x18
    x19 = chain(x18, x5, x10)
    if x == 19:
        return x19
    x20 = lbind(compose, x19)
    if x == 20:
        return x20
    x21 = lbind(lbind, astuple)
    if x == 21:
        return x21
    x22 = compose(x20, x21)
    if x == 22:
        return x22
    x23 = compose(x17, x22)
    if x == 23:
        return x23
    x24 = rbind(compose, x23)
    if x == 24:
        return x24
    x25 = lbind(rbind, equality)
    if x == 25:
        return x25
    x26 = chain(x2, x24, x25)
    if x == 26:
        return x26
    x27 = fork(intersection, x14, x26)
    if x == 27:
        return x27
    x28 = lbind(fork, greater)
    if x == 28:
        return x28
    x29 = rbind(compose, x22)
    if x == 29:
        return x29
    x30 = rbind(get_val_rank, L1)
    if x == 30:
        return x30
    x31 = lbind(lbind, x30)
    if x == 31:
        return x31
    x32 = rbind(remove, x16)
    if x == 32:
        return x32
    x33 = chain(x29, x31, x32)
    if x == 33:
        return x33
    x34 = compose(x20, x13)
    if x == 34:
        return x34
    x35 = fork(x28, x33, x34)
    if x == 35:
        return x35
    x36 = compose(x2, x35)
    if x == 36:
        return x36
    x37 = fork(intersection, x27, x36)
    if x == 37:
        return x37
    x38 = fork(recolor_i, color, x37)
    if x == 38:
        return x38
    x39 = mapply(x38, x16)
    if x == 39:
        return x39
    O = paint(I, x39)
    return O

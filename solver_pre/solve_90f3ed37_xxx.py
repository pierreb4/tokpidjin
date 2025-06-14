def solve_90f3ed37_one(S, I):
    return underfill(I, ONE, mapply(fork(rbind(get_arg_rank, F0), chain(rbind(apply, apply(tojvec, interval(TWO, NEG_ONE, NEG_ONE))), lbind(lbind, shift), compose(lbind(shift, normalize(get_nth_t(order(o_g(I, R7), rbind(col_row, R1)), F0))), rbind(corner, R0))), compose(lbind(compose, size), lbind(lbind, intersection))), remove_f(get_nth_t(order(o_g(I, R7), rbind(col_row, R1)), F0), order(o_g(I, R7), rbind(col_row, R1)))))


def solve_90f3ed37(S, I, x=0):
    x1 = rbind(get_arg_rank, F0)
    if x == 1:
        return x1
    x2 = interval(TWO, NEG_ONE, NEG_ONE)
    if x == 2:
        return x2
    x3 = apply(tojvec, x2)
    if x == 3:
        return x3
    x4 = rbind(apply, x3)
    if x == 4:
        return x4
    x5 = lbind(lbind, shift)
    if x == 5:
        return x5
    x6 = o_g(I, R7)
    if x == 6:
        return x6
    x7 = rbind(col_row, R1)
    if x == 7:
        return x7
    x8 = order(x6, x7)
    if x == 8:
        return x8
    x9 = get_nth_t(x8, F0)
    if x == 9:
        return x9
    x10 = normalize(x9)
    if x == 10:
        return x10
    x11 = lbind(shift, x10)
    if x == 11:
        return x11
    x12 = rbind(corner, R0)
    if x == 12:
        return x12
    x13 = compose(x11, x12)
    if x == 13:
        return x13
    x14 = chain(x4, x5, x13)
    if x == 14:
        return x14
    x15 = lbind(compose, size)
    if x == 15:
        return x15
    x16 = lbind(lbind, intersection)
    if x == 16:
        return x16
    x17 = compose(x15, x16)
    if x == 17:
        return x17
    x18 = fork(x1, x14, x17)
    if x == 18:
        return x18
    x19 = remove_f(x9, x8)
    if x == 19:
        return x19
    x20 = mapply(x18, x19)
    if x == 20:
        return x20
    O = underfill(I, ONE, x20)
    return O

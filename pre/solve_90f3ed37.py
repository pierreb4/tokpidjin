def solve_90f3ed37_one(S, I):
    return underfill(I, ONE, mapply(fork(rbind(get_arg_rank, F0), chain(rbind(apply, apply(tojvec, interval(TWO, NEG_ONE, NEG_ONE))), lbind(lbind, shift), compose(lbind(shift, normalize(get_nth_t(order(o_g(I, R7), rbind(col_row, R1)), F0))), rbind(corner, R0))), compose(lbind(compose, size), lbind(lbind, intersection))), remove_f(get_nth_t(order(o_g(I, R7), rbind(col_row, R1)), F0), order(o_g(I, R7), rbind(col_row, R1)))))


def solve_90f3ed37(S, I):
    x1 = rbind(get_arg_rank, F0)
    x2 = interval(TWO, NEG_ONE, NEG_ONE)
    x3 = apply(tojvec, x2)
    x4 = rbind(apply, x3)
    x5 = lbind(lbind, shift)
    x6 = o_g(I, R7)
    x7 = rbind(col_row, R1)
    x8 = order(x6, x7)
    x9 = get_nth_t(x8, F0)
    x10 = normalize(x9)
    x11 = lbind(shift, x10)
    x12 = rbind(corner, R0)
    x13 = compose(x11, x12)
    x14 = chain(x4, x5, x13)
    x15 = lbind(compose, size)
    x16 = lbind(lbind, intersection)
    x17 = compose(x15, x16)
    x18 = fork(x1, x14, x17)
    x19 = remove_f(x9, x8)
    x20 = mapply(x18, x19)
    O = underfill(I, ONE, x20)
    return O

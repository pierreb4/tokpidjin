def solve_b527c5c6_one(S, I):
    return underfill(fill(I, TWO, mapply(fork(shoot, compose(center, rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), fork(astuple, fork(add, compose(invert, fork(equality, compose(rbind(col_row, R1), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R1))), fork(equality, compose(rbind(col_row, R0), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R0))), fork(add, compose(invert, fork(equality, compose(rbind(col_row, R2), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R2))), fork(equality, compose(rbind(col_row, R3), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R3))))), o_g(I, R1))), THREE, combine_f(mapply(fork(mapply, compose(lbind(lbind, shift), fork(shoot, compose(center, rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), fork(astuple, fork(add, compose(invert, fork(equality, compose(rbind(col_row, R1), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R1))), fork(equality, compose(rbind(col_row, R0), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R0))), fork(add, compose(invert, fork(equality, compose(rbind(col_row, R2), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R2))), fork(equality, compose(rbind(col_row, R3), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R3)))))), compose(lbind(apply, toivec), fork(rbind(interval, ONE), compose(invert, chain(decrement, rbind(get_rank, L1), shape_f)), compose(increment, chain(decrement, rbind(get_rank, L1), shape_f))))), difference(o_g(I, R1), sfilter_f(o_g(I, R1), compose(vline_i, fork(shoot, compose(center, rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), fork(astuple, fork(add, compose(invert, fork(equality, compose(rbind(col_row, R1), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R1))), fork(equality, compose(rbind(col_row, R0), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R0))), fork(add, compose(invert, fork(equality, compose(rbind(col_row, R2), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R2))), fork(equality, compose(rbind(col_row, R3), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R3))))))))), mapply(fork(mapply, compose(lbind(lbind, shift), fork(shoot, compose(center, rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), fork(astuple, fork(add, compose(invert, fork(equality, compose(rbind(col_row, R1), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R1))), fork(equality, compose(rbind(col_row, R0), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R0))), fork(add, compose(invert, fork(equality, compose(rbind(col_row, R2), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R2))), fork(equality, compose(rbind(col_row, R3), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R3)))))), compose(lbind(apply, tojvec), fork(rbind(interval, ONE), compose(invert, chain(decrement, rbind(get_rank, L1), shape_f)), compose(increment, chain(decrement, rbind(get_rank, L1), shape_f))))), sfilter_f(o_g(I, R1), compose(vline_i, fork(shoot, compose(center, rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), fork(astuple, fork(add, compose(invert, fork(equality, compose(rbind(col_row, R1), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R1))), fork(equality, compose(rbind(col_row, R0), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R0))), fork(add, compose(invert, fork(equality, compose(rbind(col_row, R2), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R2))), fork(equality, compose(rbind(col_row, R3), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), rbind(col_row, R3))))))))))


def solve_b527c5c6(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = matcher(x1, TWO)
    if x == 2:
        return x2
    x3 = rbind(sfilter, x2)
    if x == 3:
        return x3
    x4 = compose(center, x3)
    if x == 4:
        return x4
    x5 = rbind(col_row, R1)
    if x == 5:
        return x5
    x6 = compose(x5, x3)
    if x == 6:
        return x6
    x7 = fork(equality, x6, x5)
    if x == 7:
        return x7
    x8 = compose(invert, x7)
    if x == 8:
        return x8
    x9 = rbind(col_row, R0)
    if x == 9:
        return x9
    x10 = compose(x9, x3)
    if x == 10:
        return x10
    x11 = fork(equality, x10, x9)
    if x == 11:
        return x11
    x12 = fork(add, x8, x11)
    if x == 12:
        return x12
    x13 = rbind(col_row, R2)
    if x == 13:
        return x13
    x14 = compose(x13, x3)
    if x == 14:
        return x14
    x15 = fork(equality, x14, x13)
    if x == 15:
        return x15
    x16 = compose(invert, x15)
    if x == 16:
        return x16
    x17 = rbind(col_row, R3)
    if x == 17:
        return x17
    x18 = compose(x17, x3)
    if x == 18:
        return x18
    x19 = fork(equality, x18, x17)
    if x == 19:
        return x19
    x20 = fork(add, x16, x19)
    if x == 20:
        return x20
    x21 = fork(astuple, x12, x20)
    if x == 21:
        return x21
    x22 = fork(shoot, x4, x21)
    if x == 22:
        return x22
    x23 = o_g(I, R1)
    if x == 23:
        return x23
    x24 = mapply(x22, x23)
    if x == 24:
        return x24
    x25 = fill(I, TWO, x24)
    if x == 25:
        return x25
    x26 = lbind(lbind, shift)
    if x == 26:
        return x26
    x27 = compose(x26, x22)
    if x == 27:
        return x27
    x28 = lbind(apply, toivec)
    if x == 28:
        return x28
    x29 = rbind(interval, ONE)
    if x == 29:
        return x29
    x30 = rbind(get_rank, L1)
    if x == 30:
        return x30
    x31 = chain(decrement, x30, shape_f)
    if x == 31:
        return x31
    x32 = compose(invert, x31)
    if x == 32:
        return x32
    x33 = compose(increment, x31)
    if x == 33:
        return x33
    x34 = fork(x29, x32, x33)
    if x == 34:
        return x34
    x35 = compose(x28, x34)
    if x == 35:
        return x35
    x36 = fork(mapply, x27, x35)
    if x == 36:
        return x36
    x37 = compose(vline_i, x22)
    if x == 37:
        return x37
    x38 = sfilter_f(x23, x37)
    if x == 38:
        return x38
    x39 = difference(x23, x38)
    if x == 39:
        return x39
    x40 = mapply(x36, x39)
    if x == 40:
        return x40
    x41 = lbind(apply, tojvec)
    if x == 41:
        return x41
    x42 = compose(x41, x34)
    if x == 42:
        return x42
    x43 = fork(mapply, x27, x42)
    if x == 43:
        return x43
    x44 = mapply(x43, x38)
    if x == 44:
        return x44
    x45 = combine_f(x40, x44)
    if x == 45:
        return x45
    O = underfill(x25, THREE, x45)
    return O

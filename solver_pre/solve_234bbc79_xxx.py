def solve_234bbc79_one(S, I):
    return paint(canvas(ZERO, astuple(THREE, decrement(width_f(get_nth_f(power(fork(astuple, fork(combine, rbind(get_nth_f, F0), fork(shift, compose(rbind(get_nth_f, F0), rbind(get_nth_f, L1)), compose(lbind(add, RIGHT), fork(subtract, compose(compose(rbind(get_nth_f, L1), fork(rbind(get_arg_rank, L1), fork(sfilter, identity, compose(lbind(matcher, compose(rbind(get_nth_f, L1), rbind(get_nth_f, L1))), rbind(col_row, R3))), chain(lbind(rbind(chain, compose(dneighbors, rbind(get_nth_f, L1))), size), lbind(rbind, intersection), toindices))), rbind(get_nth_f, F0)), chain(compose(rbind(get_nth_f, L1), fork(rbind(get_arg_rank, L1), fork(sfilter, identity, compose(lbind(matcher, compose(rbind(get_nth_f, L1), rbind(get_nth_f, L1))), rbind(col_row, R2))), chain(lbind(rbind(chain, compose(dneighbors, rbind(get_nth_f, L1))), size), lbind(rbind, intersection), toindices))), rbind(get_nth_f, F0), rbind(get_nth_f, L1)))))), fork(remove, compose(rbind(get_nth_f, F0), rbind(get_nth_f, L1)), rbind(get_nth_f, L1))), size_f(o_g(I, R1)))(astuple(initset(astuple(ZERO, DOWN_LEFT)), order(apply(fork(recolor_o, compose(rbind(other, FIVE), palette_f), identity), o_g(I, R1)), rbind(col_row, R2)))), F0))))), get_nth_f(power(fork(astuple, fork(combine, rbind(get_nth_f, F0), fork(shift, compose(rbind(get_nth_f, F0), rbind(get_nth_f, L1)), compose(lbind(add, RIGHT), fork(subtract, compose(compose(rbind(get_nth_f, L1), fork(rbind(get_arg_rank, L1), fork(sfilter, identity, compose(lbind(matcher, compose(rbind(get_nth_f, L1), rbind(get_nth_f, L1))), rbind(col_row, R3))), chain(lbind(rbind(chain, compose(dneighbors, rbind(get_nth_f, L1))), size), lbind(rbind, intersection), toindices))), rbind(get_nth_f, F0)), chain(compose(rbind(get_nth_f, L1), fork(rbind(get_arg_rank, L1), fork(sfilter, identity, compose(lbind(matcher, compose(rbind(get_nth_f, L1), rbind(get_nth_f, L1))), rbind(col_row, R2))), chain(lbind(rbind(chain, compose(dneighbors, rbind(get_nth_f, L1))), size), lbind(rbind, intersection), toindices))), rbind(get_nth_f, F0), rbind(get_nth_f, L1)))))), fork(remove, compose(rbind(get_nth_f, F0), rbind(get_nth_f, L1)), rbind(get_nth_f, L1))), size_f(o_g(I, R1)))(astuple(initset(astuple(ZERO, DOWN_LEFT)), order(apply(fork(recolor_o, compose(rbind(other, FIVE), palette_f), identity), o_g(I, R1)), rbind(col_row, R2)))), F0))


def solve_234bbc79(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, L1)
    if x == 2:
        return x2
    x3 = compose(x1, x2)
    if x == 3:
        return x3
    x4 = lbind(add, RIGHT)
    if x == 4:
        return x4
    x5 = rbind(get_arg_rank, L1)
    if x == 5:
        return x5
    x6 = compose(x2, x2)
    if x == 6:
        return x6
    x7 = lbind(matcher, x6)
    if x == 7:
        return x7
    x8 = rbind(col_row, R3)
    if x == 8:
        return x8
    x9 = compose(x7, x8)
    if x == 9:
        return x9
    x10 = fork(sfilter, identity, x9)
    if x == 10:
        return x10
    x11 = compose(dneighbors, x2)
    if x == 11:
        return x11
    x12 = rbind(chain, x11)
    if x == 12:
        return x12
    x13 = lbind(x12, size)
    if x == 13:
        return x13
    x14 = lbind(rbind, intersection)
    if x == 14:
        return x14
    x15 = chain(x13, x14, toindices)
    if x == 15:
        return x15
    x16 = fork(x5, x10, x15)
    if x == 16:
        return x16
    x17 = compose(x2, x16)
    if x == 17:
        return x17
    x18 = compose(x17, x1)
    if x == 18:
        return x18
    x19 = rbind(col_row, R2)
    if x == 19:
        return x19
    x20 = compose(x7, x19)
    if x == 20:
        return x20
    x21 = fork(sfilter, identity, x20)
    if x == 21:
        return x21
    x22 = fork(x5, x21, x15)
    if x == 22:
        return x22
    x23 = compose(x2, x22)
    if x == 23:
        return x23
    x24 = chain(x23, x1, x2)
    if x == 24:
        return x24
    x25 = fork(subtract, x18, x24)
    if x == 25:
        return x25
    x26 = compose(x4, x25)
    if x == 26:
        return x26
    x27 = fork(shift, x3, x26)
    if x == 27:
        return x27
    x28 = fork(combine, x1, x27)
    if x == 28:
        return x28
    x29 = fork(remove, x3, x2)
    if x == 29:
        return x29
    x30 = fork(astuple, x28, x29)
    if x == 30:
        return x30
    x31 = o_g(I, R1)
    if x == 31:
        return x31
    x32 = size_f(x31)
    if x == 32:
        return x32
    x33 = power(x30, x32)
    if x == 33:
        return x33
    x34 = astuple(ZERO, DOWN_LEFT)
    if x == 34:
        return x34
    x35 = initset(x34)
    if x == 35:
        return x35
    x36 = rbind(other, FIVE)
    if x == 36:
        return x36
    x37 = compose(x36, palette_f)
    if x == 37:
        return x37
    x38 = fork(recolor_o, x37, identity)
    if x == 38:
        return x38
    x39 = apply(x38, x31)
    if x == 39:
        return x39
    x40 = order(x39, x19)
    if x == 40:
        return x40
    x41 = astuple(x35, x40)
    if x == 41:
        return x41
    x42 = x33(x41)
    if x == 42:
        return x42
    x43 = get_nth_f(x42, F0)
    if x == 43:
        return x43
    x44 = width_f(x43)
    if x == 44:
        return x44
    x45 = decrement(x44)
    if x == 45:
        return x45
    x46 = astuple(THREE, x45)
    if x == 46:
        return x46
    x47 = canvas(ZERO, x46)
    if x == 47:
        return x47
    O = paint(x47, x43)
    return O

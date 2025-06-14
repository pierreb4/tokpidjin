def solve_50846271_one(S, I):
    return fill(fill(fill(I, TWO, mfilter_f(prapply(connect, f_ofcolor(I, TWO), f_ofcolor(I, TWO)), fork(both, compose(lbind(greater, SIX), size), fork(either, vline_i, hline_i)))), EIGHT, mapply(fork(combine, fork(connect, rbind(add, toivec(halve(get_val_rank_f(colorfilter(o_g(fill(I, TWO, mfilter_f(prapply(connect, f_ofcolor(I, TWO), f_ofcolor(I, TWO)), fork(both, compose(lbind(greater, SIX), size), fork(either, vline_i, hline_i)))), R4), TWO), width_f, F0)))), rbind(subtract, toivec(halve(get_val_rank_f(colorfilter(o_g(fill(I, TWO, mfilter_f(prapply(connect, f_ofcolor(I, TWO), f_ofcolor(I, TWO)), fork(both, compose(lbind(greater, SIX), size), fork(either, vline_i, hline_i)))), R4), TWO), width_f, F0))))), fork(connect, rbind(add, tojvec(halve(get_val_rank_f(colorfilter(o_g(fill(I, TWO, mfilter_f(prapply(connect, f_ofcolor(I, TWO), f_ofcolor(I, TWO)), fork(both, compose(lbind(greater, SIX), size), fork(either, vline_i, hline_i)))), R4), TWO), width_f, F0)))), rbind(subtract, tojvec(halve(get_val_rank_f(colorfilter(o_g(fill(I, TWO, mfilter_f(prapply(connect, f_ofcolor(I, TWO), f_ofcolor(I, TWO)), fork(both, compose(lbind(greater, SIX), size), fork(either, vline_i, hline_i)))), R4), TWO), width_f, F0)))))), apply(compose(rbind(rbind(get_arg_rank, F0), chain(rbind(colorcount_f, TWO), rbind(toobject, fill(I, TWO, mfilter_f(prapply(connect, f_ofcolor(I, TWO), f_ofcolor(I, TWO)), fork(both, compose(lbind(greater, SIX), size), fork(either, vline_i, hline_i))))), fork(combine, dneighbors, fork(insert, rbind(subtract, TWO_BY_ZERO), fork(insert, rbind(subtract, ZERO_BY_TWO), fork(insert, rbind(add, TWO_BY_ZERO), compose(initset, rbind(add, ZERO_BY_TWO)))))))), toindices), colorfilter(o_g(fill(I, TWO, mfilter_f(prapply(connect, f_ofcolor(I, TWO), f_ofcolor(I, TWO)), fork(both, compose(lbind(greater, SIX), size), fork(either, vline_i, hline_i)))), R4), TWO)))), TWO, f_ofcolor(I, TWO))


def solve_50846271(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = prapply(connect, x1, x1)
    if x == 2:
        return x2
    x3 = lbind(greater, SIX)
    if x == 3:
        return x3
    x4 = compose(x3, size)
    if x == 4:
        return x4
    x5 = fork(either, vline_i, hline_i)
    if x == 5:
        return x5
    x6 = fork(both, x4, x5)
    if x == 6:
        return x6
    x7 = mfilter_f(x2, x6)
    if x == 7:
        return x7
    x8 = fill(I, TWO, x7)
    if x == 8:
        return x8
    x9 = o_g(x8, R4)
    if x == 9:
        return x9
    x10 = colorfilter(x9, TWO)
    if x == 10:
        return x10
    x11 = get_val_rank_f(x10, width_f, F0)
    if x == 11:
        return x11
    x12 = halve(x11)
    if x == 12:
        return x12
    x13 = toivec(x12)
    if x == 13:
        return x13
    x14 = rbind(add, x13)
    if x == 14:
        return x14
    x15 = rbind(subtract, x13)
    if x == 15:
        return x15
    x16 = fork(connect, x14, x15)
    if x == 16:
        return x16
    x17 = tojvec(x12)
    if x == 17:
        return x17
    x18 = rbind(add, x17)
    if x == 18:
        return x18
    x19 = rbind(subtract, x17)
    if x == 19:
        return x19
    x20 = fork(connect, x18, x19)
    if x == 20:
        return x20
    x21 = fork(combine, x16, x20)
    if x == 21:
        return x21
    x22 = rbind(get_arg_rank, F0)
    if x == 22:
        return x22
    x23 = rbind(colorcount_f, TWO)
    if x == 23:
        return x23
    x24 = rbind(toobject, x8)
    if x == 24:
        return x24
    x25 = rbind(subtract, TWO_BY_ZERO)
    if x == 25:
        return x25
    x26 = rbind(subtract, ZERO_BY_TWO)
    if x == 26:
        return x26
    x27 = rbind(add, TWO_BY_ZERO)
    if x == 27:
        return x27
    x28 = rbind(add, ZERO_BY_TWO)
    if x == 28:
        return x28
    x29 = compose(initset, x28)
    if x == 29:
        return x29
    x30 = fork(insert, x27, x29)
    if x == 30:
        return x30
    x31 = fork(insert, x26, x30)
    if x == 31:
        return x31
    x32 = fork(insert, x25, x31)
    if x == 32:
        return x32
    x33 = fork(combine, dneighbors, x32)
    if x == 33:
        return x33
    x34 = chain(x23, x24, x33)
    if x == 34:
        return x34
    x35 = rbind(x22, x34)
    if x == 35:
        return x35
    x36 = compose(x35, toindices)
    if x == 36:
        return x36
    x37 = apply(x36, x10)
    if x == 37:
        return x37
    x38 = mapply(x21, x37)
    if x == 38:
        return x38
    x39 = fill(x8, EIGHT, x38)
    if x == 39:
        return x39
    O = fill(x39, TWO, x1)
    return O

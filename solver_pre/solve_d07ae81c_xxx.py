def solve_d07ae81c_one(S, I):
    return fill(fill(I, branch(equality(get_color_rank_f(toobject(neighbors(center(get_nth_f(sizefilter(o_g(I, R4), ONE), F0))), I), F0), get_nth_f(apply(color, difference(o_g(I, R4), sizefilter(o_g(I, R4), ONE))), F0)), color(get_nth_f(sizefilter(o_g(I, R4), ONE), F0)), other_f(apply(color, sizefilter(o_g(I, R4), ONE)), color(get_nth_f(sizefilter(o_g(I, R4), ONE), F0)))), intersection(f_ofcolor(I, get_nth_f(apply(color, difference(o_g(I, R4), sizefilter(o_g(I, R4), ONE))), F0)), mapply(compose(fork(combine, fork(combine, rbind(shoot, UNITY), rbind(shoot, NEG_UNITY)), fork(combine, rbind(shoot, DOWN_LEFT), rbind(shoot, UP_RIGHT))), center), sizefilter(o_g(I, R4), ONE)))), branch(equality(get_color_rank_f(toobject(neighbors(center(get_nth_f(sizefilter(o_g(I, R4), ONE), F0))), I), F0), get_nth_f(apply(color, difference(o_g(I, R4), sizefilter(o_g(I, R4), ONE))), F0)), other_f(apply(color, sizefilter(o_g(I, R4), ONE)), color(get_nth_f(sizefilter(o_g(I, R4), ONE), F0))), color(get_nth_f(sizefilter(o_g(I, R4), ONE), F0))), intersection(f_ofcolor(I, get_nth_f(apply(color, difference(o_g(I, R4), sizefilter(o_g(I, R4), ONE))), L1)), mapply(compose(fork(combine, fork(combine, rbind(shoot, UNITY), rbind(shoot, NEG_UNITY)), fork(combine, rbind(shoot, DOWN_LEFT), rbind(shoot, UP_RIGHT))), center), sizefilter(o_g(I, R4), ONE))))


def solve_d07ae81c(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = get_nth_f(x2, F0)
    if x == 3:
        return x3
    x4 = center(x3)
    if x == 4:
        return x4
    x5 = neighbors(x4)
    if x == 5:
        return x5
    x6 = toobject(x5, I)
    if x == 6:
        return x6
    x7 = get_color_rank_f(x6, F0)
    if x == 7:
        return x7
    x8 = difference(x1, x2)
    if x == 8:
        return x8
    x9 = apply(color, x8)
    if x == 9:
        return x9
    x10 = get_nth_f(x9, F0)
    if x == 10:
        return x10
    x11 = equality(x7, x10)
    if x == 11:
        return x11
    x12 = color(x3)
    if x == 12:
        return x12
    x13 = apply(color, x2)
    if x == 13:
        return x13
    x14 = other_f(x13, x12)
    if x == 14:
        return x14
    x15 = branch(x11, x12, x14)
    if x == 15:
        return x15
    x16 = f_ofcolor(I, x10)
    if x == 16:
        return x16
    x17 = rbind(shoot, UNITY)
    if x == 17:
        return x17
    x18 = rbind(shoot, NEG_UNITY)
    if x == 18:
        return x18
    x19 = fork(combine, x17, x18)
    if x == 19:
        return x19
    x20 = rbind(shoot, DOWN_LEFT)
    if x == 20:
        return x20
    x21 = rbind(shoot, UP_RIGHT)
    if x == 21:
        return x21
    x22 = fork(combine, x20, x21)
    if x == 22:
        return x22
    x23 = fork(combine, x19, x22)
    if x == 23:
        return x23
    x24 = compose(x23, center)
    if x == 24:
        return x24
    x25 = mapply(x24, x2)
    if x == 25:
        return x25
    x26 = intersection(x16, x25)
    if x == 26:
        return x26
    x27 = fill(I, x15, x26)
    if x == 27:
        return x27
    x28 = branch(x11, x14, x12)
    if x == 28:
        return x28
    x29 = get_nth_f(x9, L1)
    if x == 29:
        return x29
    x30 = f_ofcolor(I, x29)
    if x == 30:
        return x30
    x31 = intersection(x30, x25)
    if x == 31:
        return x31
    O = fill(x27, x28, x31)
    return O

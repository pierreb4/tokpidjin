def solve_995c5fa3_one(S, I):
    return hupscale(merge_t(apply(compose(rbind(canvas, UNITY), fork(add, fork(add, compose(double, matcher(compose(size, rbind(f_ofcolor, BLACK)), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), chain(power(double, TWO), double, matcher(compose(rbind(corner, R0), rbind(f_ofcolor, BLACK)), UNITY))), fork(add, compose(rbind(multiply, GREEN), matcher(compose(rbind(corner, R0), rbind(f_ofcolor, BLACK)), DOWN)), compose(power(double, TWO), matcher(compose(rbind(corner, R0), rbind(f_ofcolor, BLACK)), astuple(TWO, ONE)))))), hsplit(I, THREE))), THREE)


def solve_995c5fa3(S, I, x=0):
    x1 = rbind(canvas, UNITY)
    if x == 1:
        return x1
    x2 = rbind(f_ofcolor, BLACK)
    if x == 2:
        return x2
    x3 = compose(size, x2)
    if x == 3:
        return x3
    x4 = identity(p_g)
    if x == 4:
        return x4
    x5 = rbind(get_nth_t, F0)
    if x == 5:
        return x5
    x6 = c_iz_n(S, x4, x5)
    if x == 6:
        return x6
    x7 = matcher(x3, x6)
    if x == 7:
        return x7
    x8 = compose(double, x7)
    if x == 8:
        return x8
    x9 = power(double, TWO)
    if x == 9:
        return x9
    x10 = rbind(corner, R0)
    if x == 10:
        return x10
    x11 = compose(x10, x2)
    if x == 11:
        return x11
    x12 = matcher(x11, UNITY)
    if x == 12:
        return x12
    x13 = chain(x9, double, x12)
    if x == 13:
        return x13
    x14 = fork(add, x8, x13)
    if x == 14:
        return x14
    x15 = rbind(multiply, GREEN)
    if x == 15:
        return x15
    x16 = matcher(x11, DOWN)
    if x == 16:
        return x16
    x17 = compose(x15, x16)
    if x == 17:
        return x17
    x18 = astuple(TWO, ONE)
    if x == 18:
        return x18
    x19 = matcher(x11, x18)
    if x == 19:
        return x19
    x20 = compose(x9, x19)
    if x == 20:
        return x20
    x21 = fork(add, x17, x20)
    if x == 21:
        return x21
    x22 = fork(add, x14, x21)
    if x == 22:
        return x22
    x23 = compose(x1, x22)
    if x == 23:
        return x23
    x24 = hsplit(I, THREE)
    if x == 24:
        return x24
    x25 = apply(x23, x24)
    if x == 25:
        return x25
    x26 = merge_t(x25)
    if x == 26:
        return x26
    O = hupscale(x26, THREE)
    return O

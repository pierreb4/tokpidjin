def solve_995c5fa3_one(S, I):
    return hupscale(merge_t(apply(compose(rbind(canvas, UNITY), fork(add, fork(add, compose(double, matcher(compose(size, rbind(f_ofcolor, ZERO)), ZERO)), chain(power(double, TWO), double, matcher(compose(rbind(corner, R0), rbind(f_ofcolor, ZERO)), UNITY))), fork(add, compose(rbind(multiply, THREE), matcher(compose(rbind(corner, R0), rbind(f_ofcolor, ZERO)), DOWN)), compose(power(double, TWO), matcher(compose(rbind(corner, R0), rbind(f_ofcolor, ZERO)), astuple(TWO, ONE)))))), hsplit(I, THREE))), THREE)


def solve_995c5fa3(S, I, x=0):
    x1 = rbind(canvas, UNITY)
    if x == 1:
        return x1
    x2 = rbind(f_ofcolor, ZERO)
    if x == 2:
        return x2
    x3 = compose(size, x2)
    if x == 3:
        return x3
    x4 = matcher(x3, ZERO)
    if x == 4:
        return x4
    x5 = compose(double, x4)
    if x == 5:
        return x5
    x6 = power(double, TWO)
    if x == 6:
        return x6
    x7 = rbind(corner, R0)
    if x == 7:
        return x7
    x8 = compose(x7, x2)
    if x == 8:
        return x8
    x9 = matcher(x8, UNITY)
    if x == 9:
        return x9
    x10 = chain(x6, double, x9)
    if x == 10:
        return x10
    x11 = fork(add, x5, x10)
    if x == 11:
        return x11
    x12 = rbind(multiply, THREE)
    if x == 12:
        return x12
    x13 = matcher(x8, DOWN)
    if x == 13:
        return x13
    x14 = compose(x12, x13)
    if x == 14:
        return x14
    x15 = astuple(TWO, ONE)
    if x == 15:
        return x15
    x16 = matcher(x8, x15)
    if x == 16:
        return x16
    x17 = compose(x6, x16)
    if x == 17:
        return x17
    x18 = fork(add, x14, x17)
    if x == 18:
        return x18
    x19 = fork(add, x11, x18)
    if x == 19:
        return x19
    x20 = compose(x1, x19)
    if x == 20:
        return x20
    x21 = hsplit(I, THREE)
    if x == 21:
        return x21
    x22 = apply(x20, x21)
    if x == 22:
        return x22
    x23 = merge_t(x22)
    if x == 23:
        return x23
    O = hupscale(x23, THREE)
    return O

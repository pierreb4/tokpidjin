def solve_d43fd935_one(S, I):
    return paint(I, mapply(fork(recolor_i, color, fork(connect, center, fork(add, center, rbind(gravitate, f_ofcolor(I, GREEN))))), sfilter_f(sizefilter(o_g(I, R5), ONE), fork(either, rbind(vmatching, f_ofcolor(I, GREEN)), rbind(hmatching, f_ofcolor(I, GREEN))))))


def solve_d43fd935(S, I, x=0):
    x1 = f_ofcolor(I, GREEN)
    if x == 1:
        return x1
    x2 = rbind(gravitate, x1)
    if x == 2:
        return x2
    x3 = fork(add, center, x2)
    if x == 3:
        return x3
    x4 = fork(connect, center, x3)
    if x == 4:
        return x4
    x5 = fork(recolor_i, color, x4)
    if x == 5:
        return x5
    x6 = o_g(I, R5)
    if x == 6:
        return x6
    x7 = sizefilter(x6, ONE)
    if x == 7:
        return x7
    x8 = rbind(vmatching, x1)
    if x == 8:
        return x8
    x9 = rbind(hmatching, x1)
    if x == 9:
        return x9
    x10 = fork(either, x8, x9)
    if x == 10:
        return x10
    x11 = sfilter_f(x7, x10)
    if x == 11:
        return x11
    x12 = mapply(x5, x11)
    if x == 12:
        return x12
    O = paint(I, x12)
    return O

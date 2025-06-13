def solve_d43fd935_one(S, I):
    return paint(I, mapply(fork(recolor_i, color, fork(connect, center, fork(add, center, rbind(gravitate, f_ofcolor(I, GREEN))))), sfilter_f(sizefilter(o_g(I, R5), ONE), fork(either, rbind(vmatching, f_ofcolor(I, GREEN)), rbind(hmatching, f_ofcolor(I, GREEN))))))


def solve_d43fd935(S, I):
    x1 = f_ofcolor(I, GREEN)
    x2 = rbind(gravitate, x1)
    x3 = fork(add, center, x2)
    x4 = fork(connect, center, x3)
    x5 = fork(recolor_i, color, x4)
    x6 = o_g(I, R5)
    x7 = sizefilter(x6, ONE)
    x8 = rbind(vmatching, x1)
    x9 = rbind(hmatching, x1)
    x10 = fork(either, x8, x9)
    x11 = sfilter_f(x7, x10)
    x12 = mapply(x5, x11)
    O = paint(I, x12)
    return O

def solve_9edfc990_one(S, I):
    return paint(I, recolor_o(ONE, mfilter_f(colorfilter(o_g(I, R4), ZERO), rbind(adjacent, f_ofcolor(I, ONE)))))


def solve_9edfc990(S, I):
    x1 = o_g(I, R4)
    x2 = colorfilter(x1, ZERO)
    x3 = f_ofcolor(I, ONE)
    x4 = rbind(adjacent, x3)
    x5 = mfilter_f(x2, x4)
    x6 = recolor_o(ONE, x5)
    O = paint(I, x6)
    return O

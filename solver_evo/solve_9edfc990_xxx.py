def solve_9edfc990_one(S, I):
    return paint(I, recolor_o(BLUE, mfilter_f(colorfilter(o_g(I, R4), BLACK), rbind(adjacent, f_ofcolor(I, BLUE)))))


def solve_9edfc990(S, I):
    x1 = o_g(I, R4)
    x2 = colorfilter(x1, BLACK)
    x3 = f_ofcolor(I, BLUE)
    x4 = rbind(adjacent, x3)
    x5 = mfilter_f(x2, x4)
    x6 = recolor_o(BLUE, x5)
    O = paint(I, x6)
    return O

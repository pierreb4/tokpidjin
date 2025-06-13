def solve_178fcbfb_one(S, I):
    return paint(fill(I, RED, mapply(vfrontier, f_ofcolor(I, RED))), mapply(fork(recolor_i, color, compose(hfrontier, center)), difference(o_g(I, R5), colorfilter(o_g(I, R5), RED))))


def solve_178fcbfb(S, I):
    x1 = f_ofcolor(I, RED)
    x2 = mapply(vfrontier, x1)
    x3 = fill(I, RED, x2)
    x4 = compose(hfrontier, center)
    x5 = fork(recolor_i, color, x4)
    x6 = o_g(I, R5)
    x7 = colorfilter(x6, RED)
    x8 = difference(x6, x7)
    x9 = mapply(x5, x8)
    O = paint(x3, x9)
    return O

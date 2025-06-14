def solve_178fcbfb_one(S, I):
    return paint(fill(I, RED, mapply(vfrontier, f_ofcolor(I, RED))), mapply(fork(recolor_i, color, compose(hfrontier, center)), difference(o_g(I, R5), colorfilter(o_g(I, R5), RED))))


def solve_178fcbfb(S, I, x=0):
    x1 = f_ofcolor(I, RED)
    if x == 1:
        return x1
    x2 = mapply(vfrontier, x1)
    if x == 2:
        return x2
    x3 = fill(I, RED, x2)
    if x == 3:
        return x3
    x4 = compose(hfrontier, center)
    if x == 4:
        return x4
    x5 = fork(recolor_i, color, x4)
    if x == 5:
        return x5
    x6 = o_g(I, R5)
    if x == 6:
        return x6
    x7 = colorfilter(x6, RED)
    if x == 7:
        return x7
    x8 = difference(x6, x7)
    if x == 8:
        return x8
    x9 = mapply(x5, x8)
    if x == 9:
        return x9
    O = paint(x3, x9)
    return O

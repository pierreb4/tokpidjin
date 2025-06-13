def solve_d13f3404_one(S, I):
    return paint(canvas(ZERO, astuple(SIX, SIX)), mapply(fork(recolor_i, color, compose(rbind(shoot, UNITY), center)), o_g(I, R5)))


def solve_d13f3404(S, I):
    x1 = astuple(SIX, SIX)
    x2 = canvas(ZERO, x1)
    x3 = rbind(shoot, UNITY)
    x4 = compose(x3, center)
    x5 = fork(recolor_i, color, x4)
    x6 = o_g(I, R5)
    x7 = mapply(x5, x6)
    O = paint(x2, x7)
    return O

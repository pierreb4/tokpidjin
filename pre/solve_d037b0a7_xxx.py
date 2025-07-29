def solve_d037b0a7_one(S, I):
    return paint(I, mapply(fork(recolor_i, color, compose(rbind(shoot, DOWN), center)), o_g(I, R5)))


def solve_d037b0a7(S, I):
    x1 = rbind(shoot, DOWN)
    x2 = compose(x1, center)
    x3 = fork(recolor_i, color, x2)
    x4 = o_g(I, R5)
    x5 = mapply(x3, x4)
    O = paint(I, x5)
    return O

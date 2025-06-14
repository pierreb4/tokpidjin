def solve_d037b0a7_one(S, I):
    return paint(I, mapply(fork(recolor_i, color, compose(rbind(shoot, DOWN), center)), o_g(I, R5)))


def solve_d037b0a7(S, I, x=0):
    x1 = rbind(shoot, DOWN)
    if x == 1:
        return x1
    x2 = compose(x1, center)
    if x == 2:
        return x2
    x3 = fork(recolor_i, color, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R5)
    if x == 4:
        return x4
    x5 = mapply(x3, x4)
    if x == 5:
        return x5
    O = paint(I, x5)
    return O

def solve_d13f3404_one(S, I):
    return paint(canvas(ZERO, astuple(SIX, SIX)), mapply(fork(recolor_i, color, compose(rbind(shoot, UNITY), center)), o_g(I, R5)))


def solve_d13f3404(S, I, x=0):
    x1 = astuple(SIX, SIX)
    if x == 1:
        return x1
    x2 = canvas(ZERO, x1)
    if x == 2:
        return x2
    x3 = rbind(shoot, UNITY)
    if x == 3:
        return x3
    x4 = compose(x3, center)
    if x == 4:
        return x4
    x5 = fork(recolor_i, color, x4)
    if x == 5:
        return x5
    x6 = o_g(I, R5)
    if x == 6:
        return x6
    x7 = mapply(x5, x6)
    if x == 7:
        return x7
    O = paint(x2, x7)
    return O

def solve_feca6190_one(S, I):
    return mir_rot_t(paint(canvas(ZERO, astuple(multiply(size_f(o_g(I, R5)), FIVE), multiply(size_f(o_g(I, R5)), FIVE))), mapply(fork(recolor_i, color, compose(rbind(shoot, UNITY), center)), o_g(I, R5))), R0)


def solve_feca6190(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = size_f(x1)
    if x == 2:
        return x2
    x3 = multiply(x2, FIVE)
    if x == 3:
        return x3
    x4 = astuple(x3, x3)
    if x == 4:
        return x4
    x5 = canvas(ZERO, x4)
    if x == 5:
        return x5
    x6 = rbind(shoot, UNITY)
    if x == 6:
        return x6
    x7 = compose(x6, center)
    if x == 7:
        return x7
    x8 = fork(recolor_i, color, x7)
    if x == 8:
        return x8
    x9 = mapply(x8, x1)
    if x == 9:
        return x9
    x10 = paint(x5, x9)
    if x == 10:
        return x10
    O = mir_rot_t(x10, R0)
    return O

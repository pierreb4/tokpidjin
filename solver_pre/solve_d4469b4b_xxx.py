def solve_d4469b4b_one(S, I):
    return fill(canvas(ZERO, THREE_BY_THREE), FIVE, fork(combine, vfrontier, hfrontier)(branch(equality(other_f(palette_t(I), ZERO), TWO), RIGHT, branch(equality(other_f(palette_t(I), ZERO), ONE), UNITY, TWO_BY_TWO))))


def solve_d4469b4b(S, I, x=0):
    x1 = canvas(ZERO, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = fork(combine, vfrontier, hfrontier)
    if x == 2:
        return x2
    x3 = palette_t(I)
    if x == 3:
        return x3
    x4 = other_f(x3, ZERO)
    if x == 4:
        return x4
    x5 = equality(x4, TWO)
    if x == 5:
        return x5
    x6 = equality(x4, ONE)
    if x == 6:
        return x6
    x7 = branch(x6, UNITY, TWO_BY_TWO)
    if x == 7:
        return x7
    x8 = branch(x5, RIGHT, x7)
    if x == 8:
        return x8
    x9 = x2(x8)
    if x == 9:
        return x9
    O = fill(x1, FIVE, x9)
    return O

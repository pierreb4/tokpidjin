def solve_d4469b4b_one(S, I):
    return fill(canvas(ZERO, THREE_BY_THREE), FIVE, fork(combine, vfrontier, hfrontier)(branch(equality(other_f(palette_t(I), ZERO), TWO), RIGHT, branch(equality(other_f(palette_t(I), ZERO), ONE), UNITY, TWO_BY_TWO))))


def solve_d4469b4b(S, I):
    x1 = canvas(ZERO, THREE_BY_THREE)
    x2 = fork(combine, vfrontier, hfrontier)
    x3 = palette_t(I)
    x4 = other_f(x3, ZERO)
    x5 = equality(x4, TWO)
    x6 = equality(x4, ONE)
    x7 = branch(x6, UNITY, TWO_BY_TWO)
    x8 = branch(x5, RIGHT, x7)
    x9 = x2(x8)
    O = fill(x1, FIVE, x9)
    return O

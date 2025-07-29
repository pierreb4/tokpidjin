def solve_6e02f1e3_one(S, I):
    return fill(canvas(ZERO, THREE_BY_THREE), FIVE, connect(branch(equality(numcolors_t(I), THREE), TWO_BY_ZERO, ORIGIN), branch(equality(numcolors_t(I), TWO), TWO_BY_TWO, ZERO_BY_TWO)))


def solve_6e02f1e3(S, I):
    x1 = canvas(ZERO, THREE_BY_THREE)
    x2 = numcolors_t(I)
    x3 = equality(x2, THREE)
    x4 = branch(x3, TWO_BY_ZERO, ORIGIN)
    x5 = equality(x2, TWO)
    x6 = branch(x5, TWO_BY_TWO, ZERO_BY_TWO)
    x7 = connect(x4, x6)
    O = fill(x1, FIVE, x7)
    return O

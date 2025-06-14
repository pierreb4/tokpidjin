def solve_6e02f1e3_one(S, I):
    return fill(canvas(ZERO, THREE_BY_THREE), FIVE, connect(branch(equality(numcolors_t(I), THREE), TWO_BY_ZERO, ORIGIN), branch(equality(numcolors_t(I), TWO), TWO_BY_TWO, ZERO_BY_TWO)))


def solve_6e02f1e3(S, I, x=0):
    x1 = canvas(ZERO, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = numcolors_t(I)
    if x == 2:
        return x2
    x3 = equality(x2, THREE)
    if x == 3:
        return x3
    x4 = branch(x3, TWO_BY_ZERO, ORIGIN)
    if x == 4:
        return x4
    x5 = equality(x2, TWO)
    if x == 5:
        return x5
    x6 = branch(x5, TWO_BY_TWO, ZERO_BY_TWO)
    if x == 6:
        return x6
    x7 = connect(x4, x6)
    if x == 7:
        return x7
    O = fill(x1, FIVE, x7)
    return O

def solve_017c7c7b_one(S, I):
    return replace(vconcat(I, branch(equality(tophalf(I), bottomhalf(I)), bottomhalf(I), crop(I, TWO_BY_ZERO, THREE_BY_THREE))), ONE, TWO)


def solve_017c7c7b(S, I, x=0):
    x1 = tophalf(I)
    if x == 1:
        return x1
    x2 = bottomhalf(I)
    if x == 2:
        return x2
    x3 = equality(x1, x2)
    if x == 3:
        return x3
    x4 = crop(I, TWO_BY_ZERO, THREE_BY_THREE)
    if x == 4:
        return x4
    x5 = branch(x3, x2, x4)
    if x == 5:
        return x5
    x6 = vconcat(I, x5)
    if x == 6:
        return x6
    O = replace(x6, ONE, TWO)
    return O

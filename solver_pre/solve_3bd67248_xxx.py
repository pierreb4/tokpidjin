def solve_3bd67248_one(S, I):
    return fill(fill(I, TWO, shoot(astuple(decrement(decrement(height_t(I))), ONE), UP_RIGHT)), FOUR, shoot(astuple(decrement(height_t(I)), ONE), RIGHT))


def solve_3bd67248(S, I, x=0):
    x1 = height_t(I)
    if x == 1:
        return x1
    x2 = decrement(x1)
    if x == 2:
        return x2
    x3 = decrement(x2)
    if x == 3:
        return x3
    x4 = astuple(x3, ONE)
    if x == 4:
        return x4
    x5 = shoot(x4, UP_RIGHT)
    if x == 5:
        return x5
    x6 = fill(I, TWO, x5)
    if x == 6:
        return x6
    x7 = astuple(x2, ONE)
    if x == 7:
        return x7
    x8 = shoot(x7, RIGHT)
    if x == 8:
        return x8
    O = fill(x6, FOUR, x8)
    return O

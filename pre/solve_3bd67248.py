def solve_3bd67248_one(S, I):
    return fill(fill(I, TWO, shoot(astuple(decrement(decrement(height_t(I))), ONE), UP_RIGHT)), FOUR, shoot(astuple(decrement(height_t(I)), ONE), RIGHT))


def solve_3bd67248(S, I):
    x1 = height_t(I)
    x2 = decrement(x1)
    x3 = decrement(x2)
    x4 = astuple(x3, ONE)
    x5 = shoot(x4, UP_RIGHT)
    x6 = fill(I, TWO, x5)
    x7 = astuple(x2, ONE)
    x8 = shoot(x7, RIGHT)
    O = fill(x6, FOUR, x8)
    return O

def solve_ea786f4a_one(S, I):
    return fill(I, ZERO, combine(shoot(ORIGIN, UNITY), shoot(tojvec(decrement(width_t(I))), DOWN_LEFT)))


def solve_ea786f4a(S, I):
    x1 = shoot(ORIGIN, UNITY)
    x2 = width_t(I)
    x3 = decrement(x2)
    x4 = tojvec(x3)
    x5 = shoot(x4, DOWN_LEFT)
    x6 = combine(x1, x5)
    O = fill(I, ZERO, x6)
    return O

def solve_ea786f4a_one(S, I):
    return fill(I, ZERO, combine(shoot(ORIGIN, UNITY), shoot(tojvec(decrement(width_t(I))), DOWN_LEFT)))


def solve_ea786f4a(S, I, x=0):
    x1 = shoot(ORIGIN, UNITY)
    if x == 1:
        return x1
    x2 = width_t(I)
    if x == 2:
        return x2
    x3 = decrement(x2)
    if x == 3:
        return x3
    x4 = tojvec(x3)
    if x == 4:
        return x4
    x5 = shoot(x4, DOWN_LEFT)
    if x == 5:
        return x5
    x6 = combine(x1, x5)
    if x == 6:
        return x6
    O = fill(I, ZERO, x6)
    return O

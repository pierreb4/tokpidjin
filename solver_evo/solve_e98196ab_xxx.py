def solve_e98196ab_one(S, I):
    return paint(bottomhalf(I), merge_f(o_g(tophalf(I), R5)))


def solve_e98196ab(S, I):
    x1 = bottomhalf(I)
    x2 = tophalf(I)
    x3 = o_g(x2, R5)
    x4 = merge_f(x3)
    O = paint(x1, x4)
    return O

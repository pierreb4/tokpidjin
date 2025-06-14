def solve_e98196ab_one(S, I):
    return paint(bottomhalf(I), merge_f(o_g(tophalf(I), R5)))


def solve_e98196ab(S, I, x=0):
    x1 = bottomhalf(I)
    if x == 1:
        return x1
    x2 = tophalf(I)
    if x == 2:
        return x2
    x3 = o_g(x2, R5)
    if x == 3:
        return x3
    x4 = merge_f(x3)
    if x == 4:
        return x4
    O = paint(x1, x4)
    return O

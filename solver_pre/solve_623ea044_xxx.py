def solve_623ea044_one(S, I):
    return fill(I, color(get_nth_f(o_g(I, R5), F0)), mapply(lbind(shoot, center(get_nth_f(o_g(I, R5), F0))), combine(astuple(UNITY, NEG_UNITY), astuple(UP_RIGHT, DOWN_LEFT))))


def solve_623ea044(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = color(x2)
    if x == 3:
        return x3
    x4 = center(x2)
    if x == 4:
        return x4
    x5 = lbind(shoot, x4)
    if x == 5:
        return x5
    x6 = astuple(UNITY, NEG_UNITY)
    if x == 6:
        return x6
    x7 = astuple(UP_RIGHT, DOWN_LEFT)
    if x == 7:
        return x7
    x8 = combine(x6, x7)
    if x == 8:
        return x8
    x9 = mapply(x5, x8)
    if x == 9:
        return x9
    O = fill(I, x3, x9)
    return O

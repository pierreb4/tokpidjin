def solve_623ea044_one(S, I):
    return fill(I, color(get_nth_f(o_g(I, R5), F0)), mapply(lbind(shoot, center(get_nth_f(o_g(I, R5), F0))), combine(astuple(UNITY, NEG_UNITY), astuple(UP_RIGHT, DOWN_LEFT))))


def solve_623ea044(S, I):
    x1 = o_g(I, R5)
    x2 = get_nth_f(x1, F0)
    x3 = color(x2)
    x4 = center(x2)
    x5 = lbind(shoot, x4)
    x6 = astuple(UNITY, NEG_UNITY)
    x7 = astuple(UP_RIGHT, DOWN_LEFT)
    x8 = combine(x6, x7)
    x9 = mapply(x5, x8)
    O = fill(I, x3, x9)
    return O

def solve_7468f01a_one(S, I):
    return mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R2)


def solve_7468f01a(S, I):
    x1 = o_g(I, R3)
    x2 = get_nth_f(x1, F0)
    x3 = subgrid(x2, I)
    O = mir_rot_t(x3, R2)
    return O

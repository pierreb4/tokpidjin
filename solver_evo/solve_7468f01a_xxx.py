def solve_7468f01a_one(S, I):
    return mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R2)


def solve_7468f01a(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    O = mir_rot_t(x3, R2)
    return O

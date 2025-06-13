def solve_90c28cc7_one(S, I):
    return mir_rot_t(dedupe(mir_rot_t(dedupe(subgrid(get_nth_f(o_g(I, R1), F0), I)), R4)), R6)


def solve_90c28cc7(S, I):
    x1 = o_g(I, R1)
    x2 = get_nth_f(x1, F0)
    x3 = subgrid(x2, I)
    x4 = dedupe(x3)
    x5 = mir_rot_t(x4, R4)
    x6 = dedupe(x5)
    O = mir_rot_t(x6, R6)
    return O

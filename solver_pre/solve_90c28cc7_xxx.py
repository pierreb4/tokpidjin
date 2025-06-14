def solve_90c28cc7_one(S, I):
    return mir_rot_t(dedupe(mir_rot_t(dedupe(subgrid(get_nth_f(o_g(I, R1), F0), I)), R4)), R6)


def solve_90c28cc7(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = dedupe(x3)
    if x == 4:
        return x4
    x5 = mir_rot_t(x4, R4)
    if x == 5:
        return x5
    x6 = dedupe(x5)
    if x == 6:
        return x6
    O = mir_rot_t(x6, R6)
    return O

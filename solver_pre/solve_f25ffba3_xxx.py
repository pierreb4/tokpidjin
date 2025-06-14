def solve_f25ffba3_one(S, I):
    return vconcat(mir_rot_t(bottomhalf(I), R0), bottomhalf(I))


def solve_f25ffba3(S, I, x=0):
    x1 = bottomhalf(I)
    if x == 1:
        return x1
    x2 = mir_rot_t(x1, R0)
    if x == 2:
        return x2
    O = vconcat(x2, x1)
    return O

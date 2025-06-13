def solve_f25ffba3_one(S, I):
    return vconcat(mir_rot_t(bottomhalf(I), R0), bottomhalf(I))


def solve_f25ffba3(S, I):
    x1 = bottomhalf(I)
    x2 = mir_rot_t(x1, R0)
    O = vconcat(x2, x1)
    return O

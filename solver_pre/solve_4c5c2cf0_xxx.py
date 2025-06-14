def solve_4c5c2cf0_one(S, I):
    return paint(paint(I, shift(get_nth_f(o_g(mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R0), R3), F0), subtract(center(extract(o_g(I, R7), compose(fork(equality, identity, rbind(mir_rot_t, R4)), rbind(subgrid, I)))), center(extract(o_g(mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R0), R7), compose(fork(equality, identity, rbind(mir_rot_t, R4)), rbind(subgrid, mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R0)))))))), shift(get_nth_f(o_g(mir_rot_t(subgrid(get_nth_f(o_g(paint(I, shift(get_nth_f(o_g(mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R0), R3), F0), subtract(center(extract(o_g(I, R7), compose(fork(equality, identity, rbind(mir_rot_t, R4)), rbind(subgrid, I)))), center(extract(o_g(mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R0), R7), compose(fork(equality, identity, rbind(mir_rot_t, R4)), rbind(subgrid, mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R0)))))))), R3), F0), paint(I, shift(get_nth_f(o_g(mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R0), R3), F0), subtract(center(extract(o_g(I, R7), compose(fork(equality, identity, rbind(mir_rot_t, R4)), rbind(subgrid, I)))), center(extract(o_g(mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R0), R7), compose(fork(equality, identity, rbind(mir_rot_t, R4)), rbind(subgrid, mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R0))))))))), R2), R3), F0), subtract(center(extract(o_g(I, R7), compose(fork(equality, identity, rbind(mir_rot_t, R4)), rbind(subgrid, I)))), center(extract(o_g(mir_rot_t(subgrid(get_nth_f(o_g(paint(I, shift(get_nth_f(o_g(mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R0), R3), F0), subtract(center(extract(o_g(I, R7), compose(fork(equality, identity, rbind(mir_rot_t, R4)), rbind(subgrid, I)))), center(extract(o_g(mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R0), R7), compose(fork(equality, identity, rbind(mir_rot_t, R4)), rbind(subgrid, mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R0)))))))), R3), F0), paint(I, shift(get_nth_f(o_g(mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R0), R3), F0), subtract(center(extract(o_g(I, R7), compose(fork(equality, identity, rbind(mir_rot_t, R4)), rbind(subgrid, I)))), center(extract(o_g(mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R0), R7), compose(fork(equality, identity, rbind(mir_rot_t, R4)), rbind(subgrid, mir_rot_t(subgrid(get_nth_f(o_g(I, R3), F0), I), R0))))))))), R2), R7), matcher(color, color(extract(o_g(I, R7), compose(fork(equality, identity, rbind(mir_rot_t, R4)), rbind(subgrid, I))))))))))


def solve_4c5c2cf0(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = mir_rot_t(x3, R0)
    if x == 4:
        return x4
    x5 = o_g(x4, R3)
    if x == 5:
        return x5
    x6 = get_nth_f(x5, F0)
    if x == 6:
        return x6
    x7 = o_g(I, R7)
    if x == 7:
        return x7
    x8 = rbind(mir_rot_t, R4)
    if x == 8:
        return x8
    x9 = fork(equality, identity, x8)
    if x == 9:
        return x9
    x10 = rbind(subgrid, I)
    if x == 10:
        return x10
    x11 = compose(x9, x10)
    if x == 11:
        return x11
    x12 = extract(x7, x11)
    if x == 12:
        return x12
    x13 = center(x12)
    if x == 13:
        return x13
    x14 = o_g(x4, R7)
    if x == 14:
        return x14
    x15 = rbind(subgrid, x4)
    if x == 15:
        return x15
    x16 = compose(x9, x15)
    if x == 16:
        return x16
    x17 = extract(x14, x16)
    if x == 17:
        return x17
    x18 = center(x17)
    if x == 18:
        return x18
    x19 = subtract(x13, x18)
    if x == 19:
        return x19
    x20 = shift(x6, x19)
    if x == 20:
        return x20
    x21 = paint(I, x20)
    if x == 21:
        return x21
    x22 = o_g(x21, R3)
    if x == 22:
        return x22
    x23 = get_nth_f(x22, F0)
    if x == 23:
        return x23
    x24 = subgrid(x23, x21)
    if x == 24:
        return x24
    x25 = mir_rot_t(x24, R2)
    if x == 25:
        return x25
    x26 = o_g(x25, R3)
    if x == 26:
        return x26
    x27 = get_nth_f(x26, F0)
    if x == 27:
        return x27
    x28 = o_g(x25, R7)
    if x == 28:
        return x28
    x29 = color(x12)
    if x == 29:
        return x29
    x30 = matcher(color, x29)
    if x == 30:
        return x30
    x31 = extract(x28, x30)
    if x == 31:
        return x31
    x32 = center(x31)
    if x == 32:
        return x32
    x33 = subtract(x13, x32)
    if x == 33:
        return x33
    x34 = shift(x27, x33)
    if x == 34:
        return x34
    O = paint(x21, x34)
    return O

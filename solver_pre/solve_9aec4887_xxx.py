def solve_9aec4887_one(S, I):
    return fill(paint(subgrid(other_f(o_g(I, R3), get_arg_rank_f(o_g(I, R3), numcolors_f, L1)), I), apply(fork(astuple, chain(rbind(get_nth_f, F0), lbind(rbind(get_arg_rank, L1), normalize_o(other_f(o_g(I, R3), get_arg_rank_f(o_g(I, R3), numcolors_f, L1)))), chain(rbind(compose, initset), lbind(rbind, manhattan), initset)), identity), toindices(shift(normalize_o(get_arg_rank_f(o_g(I, R3), numcolors_f, L1)), UNITY)))), EIGHT, intersection(toindices(shift(normalize_o(get_arg_rank_f(o_g(I, R3), numcolors_f, L1)), UNITY)), fork(combine, identity, rbind(mir_rot_f, R2))(fork(connect, rbind(corner, R0), rbind(corner, R3))(toindices(shift(normalize_o(get_arg_rank_f(o_g(I, R3), numcolors_f, L1)), UNITY))))))


def solve_9aec4887(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, numcolors_f, L1)
    if x == 2:
        return x2
    x3 = other_f(x1, x2)
    if x == 3:
        return x3
    x4 = subgrid(x3, I)
    if x == 4:
        return x4
    x5 = rbind(get_nth_f, F0)
    if x == 5:
        return x5
    x6 = rbind(get_arg_rank, L1)
    if x == 6:
        return x6
    x7 = normalize_o(x3)
    if x == 7:
        return x7
    x8 = lbind(x6, x7)
    if x == 8:
        return x8
    x9 = rbind(compose, initset)
    if x == 9:
        return x9
    x10 = lbind(rbind, manhattan)
    if x == 10:
        return x10
    x11 = chain(x9, x10, initset)
    if x == 11:
        return x11
    x12 = chain(x5, x8, x11)
    if x == 12:
        return x12
    x13 = fork(astuple, x12, identity)
    if x == 13:
        return x13
    x14 = normalize_o(x2)
    if x == 14:
        return x14
    x15 = shift(x14, UNITY)
    if x == 15:
        return x15
    x16 = toindices(x15)
    if x == 16:
        return x16
    x17 = apply(x13, x16)
    if x == 17:
        return x17
    x18 = paint(x4, x17)
    if x == 18:
        return x18
    x19 = rbind(mir_rot_f, R2)
    if x == 19:
        return x19
    x20 = fork(combine, identity, x19)
    if x == 20:
        return x20
    x21 = rbind(corner, R0)
    if x == 21:
        return x21
    x22 = rbind(corner, R3)
    if x == 22:
        return x22
    x23 = fork(connect, x21, x22)
    if x == 23:
        return x23
    x24 = x23(x16)
    if x == 24:
        return x24
    x25 = x20(x24)
    if x == 25:
        return x25
    x26 = intersection(x16, x25)
    if x == 26:
        return x26
    O = fill(x18, EIGHT, x26)
    return O

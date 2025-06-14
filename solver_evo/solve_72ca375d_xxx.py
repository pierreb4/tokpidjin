def solve_72ca375d_one(S, I):
    return get_nth_t(extract(pair(apply(rbind(subgrid, I), totuple(o_g(I, R7))), papply(equality, apply(rbind(subgrid, I), totuple(o_g(I, R7))), apply(rbind(mir_rot_t, R2), apply(rbind(subgrid, I), totuple(o_g(I, R7)))))), rbind(get_nth_f, L1)), F0)


def solve_72ca375d(S, I, x=0):
    x1 = rbind(subgrid, I)
    if x == 1:
        return x1
    x2 = o_g(I, R7)
    if x == 2:
        return x2
    x3 = totuple(x2)
    if x == 3:
        return x3
    x4 = apply(x1, x3)
    if x == 4:
        return x4
    x5 = rbind(mir_rot_t, R2)
    if x == 5:
        return x5
    x6 = apply(x5, x4)
    if x == 6:
        return x6
    x7 = papply(equality, x4, x6)
    if x == 7:
        return x7
    x8 = pair(x4, x7)
    if x == 8:
        return x8
    x9 = rbind(get_nth_f, L1)
    if x == 9:
        return x9
    x10 = extract(x8, x9)
    if x == 10:
        return x10
    O = get_nth_t(x10, F0)
    return O

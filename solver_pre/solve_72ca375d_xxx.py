def solve_72ca375d_one(S, I):
    return get_nth_t(extract(pair(apply(rbind(subgrid, I), totuple(o_g(I, R7))), papply(equality, apply(rbind(subgrid, I), totuple(o_g(I, R7))), apply(rbind(mir_rot_t, R2), apply(rbind(subgrid, I), totuple(o_g(I, R7)))))), rbind(get_nth_f, L1)), F0)


def solve_72ca375d(S, I):
    x1 = rbind(subgrid, I)
    x2 = o_g(I, R7)
    x3 = totuple(x2)
    x4 = apply(x1, x3)
    x5 = rbind(mir_rot_t, R2)
    x6 = apply(x5, x4)
    x7 = papply(equality, x4, x6)
    x8 = pair(x4, x7)
    x9 = rbind(get_nth_f, L1)
    x10 = extract(x8, x9)
    O = get_nth_t(x10, F0)
    return O

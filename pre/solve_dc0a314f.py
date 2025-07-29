def solve_dc0a314f_one(S, I):
    return subgrid(f_ofcolor(I, THREE), apply(lbind(apply, rbind(get_rank, F0)), papply(pair, apply(lbind(apply, rbind(get_rank, F0)), papply(pair, replace(I, THREE, ZERO), mir_rot_t(replace(I, THREE, ZERO), R1))), mir_rot_t(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, replace(I, THREE, ZERO), mir_rot_t(replace(I, THREE, ZERO), R1))), R3))))


def solve_dc0a314f(S, I):
    x1 = f_ofcolor(I, THREE)
    x2 = rbind(get_rank, F0)
    x3 = lbind(apply, x2)
    x4 = replace(I, THREE, ZERO)
    x5 = mir_rot_t(x4, R1)
    x6 = papply(pair, x4, x5)
    x7 = apply(x3, x6)
    x8 = mir_rot_t(x7, R3)
    x9 = papply(pair, x7, x8)
    x10 = apply(x3, x9)
    O = subgrid(x1, x10)
    return O

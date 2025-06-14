def solve_dc0a314f_one(S, I):
    return subgrid(f_ofcolor(I, THREE), apply(lbind(apply, rbind(get_rank, F0)), papply(pair, apply(lbind(apply, rbind(get_rank, F0)), papply(pair, replace(I, THREE, ZERO), mir_rot_t(replace(I, THREE, ZERO), R1))), mir_rot_t(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, replace(I, THREE, ZERO), mir_rot_t(replace(I, THREE, ZERO), R1))), R3))))


def solve_dc0a314f(S, I, x=0):
    x1 = f_ofcolor(I, THREE)
    if x == 1:
        return x1
    x2 = rbind(get_rank, F0)
    if x == 2:
        return x2
    x3 = lbind(apply, x2)
    if x == 3:
        return x3
    x4 = replace(I, THREE, ZERO)
    if x == 4:
        return x4
    x5 = mir_rot_t(x4, R1)
    if x == 5:
        return x5
    x6 = papply(pair, x4, x5)
    if x == 6:
        return x6
    x7 = apply(x3, x6)
    if x == 7:
        return x7
    x8 = mir_rot_t(x7, R3)
    if x == 8:
        return x8
    x9 = papply(pair, x7, x8)
    if x == 9:
        return x9
    x10 = apply(x3, x9)
    if x == 10:
        return x10
    O = subgrid(x1, x10)
    return O

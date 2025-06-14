def solve_ff805c23_one(S, I):
    return branch(contained(c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), palette_t(subgrid(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), mir_rot_t(I, R0)))), subgrid(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), mir_rot_t(I, R2)), subgrid(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), mir_rot_t(I, R0)))


def solve_ff805c23(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_iz_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, x3)
    if x == 4:
        return x4
    x5 = mir_rot_t(I, R0)
    if x == 5:
        return x5
    x6 = subgrid(x4, x5)
    if x == 6:
        return x6
    x7 = palette_t(x6)
    if x == 7:
        return x7
    x8 = contained(x3, x7)
    if x == 8:
        return x8
    x9 = mir_rot_t(I, R2)
    if x == 9:
        return x9
    x10 = subgrid(x4, x9)
    if x == 10:
        return x10
    O = branch(x8, x10, x6)
    return O

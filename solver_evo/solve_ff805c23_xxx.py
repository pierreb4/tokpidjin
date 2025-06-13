def solve_ff805c23_one(S, I):
    return branch(contained(c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), palette_t(subgrid(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), mir_rot_t(I, R0)))), subgrid(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), mir_rot_t(I, R2)), subgrid(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), mir_rot_t(I, R0)))


def solve_ff805c23(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_iz_n(S, x1, x2)
    x4 = f_ofcolor(I, x3)
    x5 = mir_rot_t(I, R0)
    x6 = subgrid(x4, x5)
    x7 = palette_t(x6)
    x8 = contained(x3, x7)
    x9 = mir_rot_t(I, R2)
    x10 = subgrid(x4, x9)
    O = branch(x8, x10, x6)
    return O

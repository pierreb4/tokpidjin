def solve_db3e9e38_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(rbind(shoot, UP), combine(shoot(corner(f_ofcolor(I, ORANGE), R3), UP_RIGHT), shoot(corner(f_ofcolor(I, ORANGE), R3), NEG_UNITY)))), ORANGE, sfilter_f(mapply(rbind(shoot, UP), combine(shoot(corner(f_ofcolor(I, ORANGE), R3), UP_RIGHT), shoot(corner(f_ofcolor(I, ORANGE), R3), NEG_UNITY))), chain(even, rbind(subtract, get_nth_t(corner(f_ofcolor(I, ORANGE), R3), L1)), rbind(get_nth_f, L1))))


def solve_db3e9e38(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = rbind(shoot, UP)
    x5 = f_ofcolor(I, ORANGE)
    x6 = corner(x5, R3)
    x7 = shoot(x6, UP_RIGHT)
    x8 = shoot(x6, NEG_UNITY)
    x9 = combine(x7, x8)
    x10 = mapply(x4, x9)
    x11 = fill(I, x3, x10)
    x12 = get_nth_t(x6, L1)
    x13 = rbind(subtract, x12)
    x14 = rbind(get_nth_f, L1)
    x15 = chain(even, x13, x14)
    x16 = sfilter_f(x10, x15)
    O = fill(x11, ORANGE, x16)
    return O

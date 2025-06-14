def solve_db3e9e38_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(rbind(shoot, UP), combine(shoot(corner(f_ofcolor(I, ORANGE), R3), UP_RIGHT), shoot(corner(f_ofcolor(I, ORANGE), R3), NEG_UNITY)))), ORANGE, sfilter_f(mapply(rbind(shoot, UP), combine(shoot(corner(f_ofcolor(I, ORANGE), R3), UP_RIGHT), shoot(corner(f_ofcolor(I, ORANGE), R3), NEG_UNITY))), chain(even, rbind(subtract, get_nth_t(corner(f_ofcolor(I, ORANGE), R3), L1)), rbind(get_nth_f, L1))))


def solve_db3e9e38(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = rbind(shoot, UP)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, ORANGE)
    if x == 5:
        return x5
    x6 = corner(x5, R3)
    if x == 6:
        return x6
    x7 = shoot(x6, UP_RIGHT)
    if x == 7:
        return x7
    x8 = shoot(x6, NEG_UNITY)
    if x == 8:
        return x8
    x9 = combine(x7, x8)
    if x == 9:
        return x9
    x10 = mapply(x4, x9)
    if x == 10:
        return x10
    x11 = fill(I, x3, x10)
    if x == 11:
        return x11
    x12 = get_nth_t(x6, L1)
    if x == 12:
        return x12
    x13 = rbind(subtract, x12)
    if x == 13:
        return x13
    x14 = rbind(get_nth_f, L1)
    if x == 14:
        return x14
    x15 = chain(even, x13, x14)
    if x == 15:
        return x15
    x16 = sfilter_f(x10, x15)
    if x == 16:
        return x16
    O = fill(x11, ORANGE, x16)
    return O

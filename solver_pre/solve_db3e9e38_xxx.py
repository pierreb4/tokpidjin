def solve_db3e9e38_one(S, I):
    return fill(fill(I, EIGHT, mapply(rbind(shoot, UP), combine(shoot(corner(f_ofcolor(I, SEVEN), R3), UP_RIGHT), shoot(corner(f_ofcolor(I, SEVEN), R3), NEG_UNITY)))), SEVEN, sfilter_f(mapply(rbind(shoot, UP), combine(shoot(corner(f_ofcolor(I, SEVEN), R3), UP_RIGHT), shoot(corner(f_ofcolor(I, SEVEN), R3), NEG_UNITY))), chain(even, rbind(subtract, get_nth_t(corner(f_ofcolor(I, SEVEN), R3), L1)), rbind(get_nth_f, L1))))


def solve_db3e9e38(S, I):
    x1 = rbind(shoot, UP)
    x2 = f_ofcolor(I, SEVEN)
    x3 = corner(x2, R3)
    x4 = shoot(x3, UP_RIGHT)
    x5 = shoot(x3, NEG_UNITY)
    x6 = combine(x4, x5)
    x7 = mapply(x1, x6)
    x8 = fill(I, EIGHT, x7)
    x9 = get_nth_t(x3, L1)
    x10 = rbind(subtract, x9)
    x11 = rbind(get_nth_f, L1)
    x12 = chain(even, x10, x11)
    x13 = sfilter_f(x7, x12)
    O = fill(x8, SEVEN, x13)
    return O

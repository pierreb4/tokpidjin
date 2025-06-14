def solve_db3e9e38_one(S, I):
    return fill(fill(I, EIGHT, mapply(rbind(shoot, UP), combine(shoot(corner(f_ofcolor(I, SEVEN), R3), UP_RIGHT), shoot(corner(f_ofcolor(I, SEVEN), R3), NEG_UNITY)))), SEVEN, sfilter_f(mapply(rbind(shoot, UP), combine(shoot(corner(f_ofcolor(I, SEVEN), R3), UP_RIGHT), shoot(corner(f_ofcolor(I, SEVEN), R3), NEG_UNITY))), chain(even, rbind(subtract, get_nth_t(corner(f_ofcolor(I, SEVEN), R3), L1)), rbind(get_nth_f, L1))))


def solve_db3e9e38(S, I, x=0):
    x1 = rbind(shoot, UP)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, SEVEN)
    if x == 2:
        return x2
    x3 = corner(x2, R3)
    if x == 3:
        return x3
    x4 = shoot(x3, UP_RIGHT)
    if x == 4:
        return x4
    x5 = shoot(x3, NEG_UNITY)
    if x == 5:
        return x5
    x6 = combine(x4, x5)
    if x == 6:
        return x6
    x7 = mapply(x1, x6)
    if x == 7:
        return x7
    x8 = fill(I, EIGHT, x7)
    if x == 8:
        return x8
    x9 = get_nth_t(x3, L1)
    if x == 9:
        return x9
    x10 = rbind(subtract, x9)
    if x == 10:
        return x10
    x11 = rbind(get_nth_f, L1)
    if x == 11:
        return x11
    x12 = chain(even, x10, x11)
    if x == 12:
        return x12
    x13 = sfilter_f(x7, x12)
    if x == 13:
        return x13
    O = fill(x8, SEVEN, x13)
    return O

def solve_b8cdaf2b_one(S, I):
    return underfill(I, get_color_rank_t(I, L1), combine(shoot(corner(shift(f_ofcolor(I, get_color_rank_t(I, L1)), UP), R0), NEG_UNITY), shoot(corner(shift(f_ofcolor(I, get_color_rank_t(I, L1)), UP), R1), UP_RIGHT)))


def solve_b8cdaf2b(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, x1)
    if x == 2:
        return x2
    x3 = shift(x2, UP)
    if x == 3:
        return x3
    x4 = corner(x3, R0)
    if x == 4:
        return x4
    x5 = shoot(x4, NEG_UNITY)
    if x == 5:
        return x5
    x6 = corner(x3, R1)
    if x == 6:
        return x6
    x7 = shoot(x6, UP_RIGHT)
    if x == 7:
        return x7
    x8 = combine(x5, x7)
    if x == 8:
        return x8
    O = underfill(I, x1, x8)
    return O

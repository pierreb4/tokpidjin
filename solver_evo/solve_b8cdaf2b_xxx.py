def solve_b8cdaf2b_one(S, I):
    return underfill(I, get_color_rank_t(I, L1), combine(shoot(corner(shift(f_ofcolor(I, get_color_rank_t(I, L1)), UP), R0), NEG_UNITY), shoot(corner(shift(f_ofcolor(I, get_color_rank_t(I, L1)), UP), R1), UP_RIGHT)))


def solve_b8cdaf2b(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = f_ofcolor(I, x1)
    x3 = shift(x2, UP)
    x4 = corner(x3, R0)
    x5 = shoot(x4, NEG_UNITY)
    x6 = corner(x3, R1)
    x7 = shoot(x6, UP_RIGHT)
    x8 = combine(x5, x7)
    O = underfill(I, x1, x8)
    return O

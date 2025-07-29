def solve_e179c5f4_one(S, I):
    return replace(mir_rot_t(crop(merge(repeat(crop(fill(fill(I, ONE, shoot(get_nth_f(f_ofcolor(I, ONE), F0), UP_RIGHT)), ONE, shoot(corner(f_ofcolor(fill(I, ONE, shoot(get_nth_f(f_ofcolor(I, ONE), F0), UP_RIGHT)), ONE), R1), NEG_UNITY)), corner(f_ofcolor(fill(fill(I, ONE, shoot(get_nth_f(f_ofcolor(I, ONE), F0), UP_RIGHT)), ONE, shoot(corner(f_ofcolor(fill(I, ONE, shoot(get_nth_f(f_ofcolor(I, ONE), F0), UP_RIGHT)), ONE), R1), NEG_UNITY)), ONE), R0), astuple(decrement(height_t(subgrid(f_ofcolor(fill(fill(I, ONE, shoot(get_nth_f(f_ofcolor(I, ONE), F0), UP_RIGHT)), ONE, shoot(corner(f_ofcolor(fill(I, ONE, shoot(get_nth_f(f_ofcolor(I, ONE), F0), UP_RIGHT)), ONE), R1), NEG_UNITY)), ONE), fill(fill(I, ONE, shoot(get_nth_f(f_ofcolor(I, ONE), F0), UP_RIGHT)), ONE, shoot(corner(f_ofcolor(fill(I, ONE, shoot(get_nth_f(f_ofcolor(I, ONE), F0), UP_RIGHT)), ONE), R1), NEG_UNITY))))), width_t(subgrid(f_ofcolor(fill(fill(I, ONE, shoot(get_nth_f(f_ofcolor(I, ONE), F0), UP_RIGHT)), ONE, shoot(corner(f_ofcolor(fill(I, ONE, shoot(get_nth_f(f_ofcolor(I, ONE), F0), UP_RIGHT)), ONE), R1), NEG_UNITY)), ONE), fill(fill(I, ONE, shoot(get_nth_f(f_ofcolor(I, ONE), F0), UP_RIGHT)), ONE, shoot(corner(f_ofcolor(fill(I, ONE, shoot(get_nth_f(f_ofcolor(I, ONE), F0), UP_RIGHT)), ONE), R1), NEG_UNITY)))))), NINE)), ORIGIN, astuple(height_t(I), width_t(subgrid(f_ofcolor(fill(fill(I, ONE, shoot(get_nth_f(f_ofcolor(I, ONE), F0), UP_RIGHT)), ONE, shoot(corner(f_ofcolor(fill(I, ONE, shoot(get_nth_f(f_ofcolor(I, ONE), F0), UP_RIGHT)), ONE), R1), NEG_UNITY)), ONE), fill(fill(I, ONE, shoot(get_nth_f(f_ofcolor(I, ONE), F0), UP_RIGHT)), ONE, shoot(corner(f_ofcolor(fill(I, ONE, shoot(get_nth_f(f_ofcolor(I, ONE), F0), UP_RIGHT)), ONE), R1), NEG_UNITY)))))), R0), ZERO, EIGHT)


def solve_e179c5f4(S, I):
    x1 = f_ofcolor(I, ONE)
    x2 = get_nth_f(x1, F0)
    x3 = shoot(x2, UP_RIGHT)
    x4 = fill(I, ONE, x3)
    x5 = f_ofcolor(x4, ONE)
    x6 = corner(x5, R1)
    x7 = shoot(x6, NEG_UNITY)
    x8 = fill(x4, ONE, x7)
    x9 = f_ofcolor(x8, ONE)
    x10 = corner(x9, R0)
    x11 = subgrid(x9, x8)
    x12 = height_t(x11)
    x13 = decrement(x12)
    x14 = width_t(x11)
    x15 = astuple(x13, x14)
    x16 = crop(x8, x10, x15)
    x17 = repeat(x16, NINE)
    x18 = merge(x17)
    x19 = height_t(I)
    x20 = astuple(x19, x14)
    x21 = crop(x18, ORIGIN, x20)
    x22 = mir_rot_t(x21, R0)
    O = replace(x22, ZERO, EIGHT)
    return O

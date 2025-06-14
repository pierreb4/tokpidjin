def solve_e179c5f4_one(S, I):
    return replace(mir_rot_t(crop(merge(repeat(crop(fill(fill(I, BLUE, shoot(get_nth_f(f_ofcolor(I, BLUE), F0), UP_RIGHT)), BLUE, shoot(corner(f_ofcolor(fill(I, BLUE, shoot(get_nth_f(f_ofcolor(I, BLUE), F0), UP_RIGHT)), BLUE), R1), NEG_UNITY)), corner(f_ofcolor(fill(fill(I, BLUE, shoot(get_nth_f(f_ofcolor(I, BLUE), F0), UP_RIGHT)), BLUE, shoot(corner(f_ofcolor(fill(I, BLUE, shoot(get_nth_f(f_ofcolor(I, BLUE), F0), UP_RIGHT)), BLUE), R1), NEG_UNITY)), BLUE), R0), astuple(decrement(height_t(subgrid(f_ofcolor(fill(fill(I, BLUE, shoot(get_nth_f(f_ofcolor(I, BLUE), F0), UP_RIGHT)), BLUE, shoot(corner(f_ofcolor(fill(I, BLUE, shoot(get_nth_f(f_ofcolor(I, BLUE), F0), UP_RIGHT)), BLUE), R1), NEG_UNITY)), BLUE), fill(fill(I, BLUE, shoot(get_nth_f(f_ofcolor(I, BLUE), F0), UP_RIGHT)), BLUE, shoot(corner(f_ofcolor(fill(I, BLUE, shoot(get_nth_f(f_ofcolor(I, BLUE), F0), UP_RIGHT)), BLUE), R1), NEG_UNITY))))), width_t(subgrid(f_ofcolor(fill(fill(I, BLUE, shoot(get_nth_f(f_ofcolor(I, BLUE), F0), UP_RIGHT)), BLUE, shoot(corner(f_ofcolor(fill(I, BLUE, shoot(get_nth_f(f_ofcolor(I, BLUE), F0), UP_RIGHT)), BLUE), R1), NEG_UNITY)), BLUE), fill(fill(I, BLUE, shoot(get_nth_f(f_ofcolor(I, BLUE), F0), UP_RIGHT)), BLUE, shoot(corner(f_ofcolor(fill(I, BLUE, shoot(get_nth_f(f_ofcolor(I, BLUE), F0), UP_RIGHT)), BLUE), R1), NEG_UNITY)))))), BURGUNDY)), ORIGIN, astuple(height_t(I), width_t(subgrid(f_ofcolor(fill(fill(I, BLUE, shoot(get_nth_f(f_ofcolor(I, BLUE), F0), UP_RIGHT)), BLUE, shoot(corner(f_ofcolor(fill(I, BLUE, shoot(get_nth_f(f_ofcolor(I, BLUE), F0), UP_RIGHT)), BLUE), R1), NEG_UNITY)), BLUE), fill(fill(I, BLUE, shoot(get_nth_f(f_ofcolor(I, BLUE), F0), UP_RIGHT)), BLUE, shoot(corner(f_ofcolor(fill(I, BLUE, shoot(get_nth_f(f_ofcolor(I, BLUE), F0), UP_RIGHT)), BLUE), R1), NEG_UNITY)))))), R0), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)))


def solve_e179c5f4(S, I, x=0):
    x1 = f_ofcolor(I, BLUE)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = shoot(x2, UP_RIGHT)
    if x == 3:
        return x3
    x4 = fill(I, BLUE, x3)
    if x == 4:
        return x4
    x5 = f_ofcolor(x4, BLUE)
    if x == 5:
        return x5
    x6 = corner(x5, R1)
    if x == 6:
        return x6
    x7 = shoot(x6, NEG_UNITY)
    if x == 7:
        return x7
    x8 = fill(x4, BLUE, x7)
    if x == 8:
        return x8
    x9 = f_ofcolor(x8, BLUE)
    if x == 9:
        return x9
    x10 = corner(x9, R0)
    if x == 10:
        return x10
    x11 = subgrid(x9, x8)
    if x == 11:
        return x11
    x12 = height_t(x11)
    if x == 12:
        return x12
    x13 = decrement(x12)
    if x == 13:
        return x13
    x14 = width_t(x11)
    if x == 14:
        return x14
    x15 = astuple(x13, x14)
    if x == 15:
        return x15
    x16 = crop(x8, x10, x15)
    if x == 16:
        return x16
    x17 = repeat(x16, BURGUNDY)
    if x == 17:
        return x17
    x18 = merge(x17)
    if x == 18:
        return x18
    x19 = height_t(I)
    if x == 19:
        return x19
    x20 = astuple(x19, x14)
    if x == 20:
        return x20
    x21 = crop(x18, ORIGIN, x20)
    if x == 21:
        return x21
    x22 = mir_rot_t(x21, R0)
    if x == 22:
        return x22
    x23 = identity(p_g)
    if x == 23:
        return x23
    x24 = rbind(get_nth_t, F0)
    if x == 24:
        return x24
    x25 = c_iz_n(S, x23, x24)
    if x == 25:
        return x25
    x26 = c_zo_n(S, x23, x24)
    if x == 26:
        return x26
    O = replace(x22, x25, x26)
    return O

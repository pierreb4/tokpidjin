def solve_a9f96cdd_one(S, I):
    return fill(fill(fill(fill(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), shift(f_ofcolor(I, RED), NEG_UNITY)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F3)), shift(f_ofcolor(I, RED), UP_RIGHT)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), shift(f_ofcolor(I, RED), DOWN_LEFT)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), shift(f_ofcolor(I, RED), UNITY))


def solve_a9f96cdd(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_iz_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = replace(I, x3, BLACK)
    if x == 4:
        return x4
    x5 = rbind(get_nth_t, F2)
    if x == 5:
        return x5
    x6 = c_zo_n(S, x1, x5)
    if x == 6:
        return x6
    x7 = f_ofcolor(I, RED)
    if x == 7:
        return x7
    x8 = shift(x7, NEG_UNITY)
    if x == 8:
        return x8
    x9 = fill(x4, x6, x8)
    if x == 9:
        return x9
    x10 = rbind(get_nth_t, F3)
    if x == 10:
        return x10
    x11 = c_zo_n(S, x1, x10)
    if x == 11:
        return x11
    x12 = shift(x7, UP_RIGHT)
    if x == 12:
        return x12
    x13 = fill(x9, x11, x12)
    if x == 13:
        return x13
    x14 = c_zo_n(S, x1, x2)
    if x == 14:
        return x14
    x15 = shift(x7, DOWN_LEFT)
    if x == 15:
        return x15
    x16 = fill(x13, x14, x15)
    if x == 16:
        return x16
    x17 = rbind(get_nth_t, F1)
    if x == 17:
        return x17
    x18 = c_zo_n(S, x1, x17)
    if x == 18:
        return x18
    x19 = shift(x7, UNITY)
    if x == 19:
        return x19
    O = fill(x16, x18, x19)
    return O

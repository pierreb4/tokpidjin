def solve_a9f96cdd_one(S, I):
    return fill(fill(fill(fill(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), shift(f_ofcolor(I, RED), NEG_UNITY)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F3)), shift(f_ofcolor(I, RED), UP_RIGHT)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), shift(f_ofcolor(I, RED), DOWN_LEFT)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), shift(f_ofcolor(I, RED), UNITY))


def solve_a9f96cdd(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_iz_n(S, x1, x2)
    x4 = replace(I, x3, BLACK)
    x5 = rbind(get_nth_t, F2)
    x6 = c_zo_n(S, x1, x5)
    x7 = f_ofcolor(I, RED)
    x8 = shift(x7, NEG_UNITY)
    x9 = fill(x4, x6, x8)
    x10 = rbind(get_nth_t, F3)
    x11 = c_zo_n(S, x1, x10)
    x12 = shift(x7, UP_RIGHT)
    x13 = fill(x9, x11, x12)
    x14 = c_zo_n(S, x1, x2)
    x15 = shift(x7, DOWN_LEFT)
    x16 = fill(x13, x14, x15)
    x17 = rbind(get_nth_t, F1)
    x18 = c_zo_n(S, x1, x17)
    x19 = shift(x7, UNITY)
    O = fill(x16, x18, x19)
    return O

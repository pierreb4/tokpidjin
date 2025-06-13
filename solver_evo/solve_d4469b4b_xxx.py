def solve_d4469b4b_one(S, I):
    return fill(canvas(BLACK, THREE_BY_THREE), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), fork(combine, vfrontier, hfrontier)(branch(equality(other_f(palette_t(I), BLACK), c_iz_n(S, identity(p_g), rbind(get_nth_t, F1))), RIGHT, branch(equality(other_f(palette_t(I), BLACK), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), UNITY, TWO_BY_TWO))))


def solve_d4469b4b(S, I):
    x1 = canvas(BLACK, THREE_BY_THREE)
    x2 = identity(p_g)
    x3 = rbind(get_nth_t, F0)
    x4 = c_zo_n(S, x2, x3)
    x5 = fork(combine, vfrontier, hfrontier)
    x6 = palette_t(I)
    x7 = other_f(x6, BLACK)
    x8 = rbind(get_nth_t, F1)
    x9 = c_iz_n(S, x2, x8)
    x10 = equality(x7, x9)
    x11 = c_iz_n(S, x2, x3)
    x12 = equality(x7, x11)
    x13 = branch(x12, UNITY, TWO_BY_TWO)
    x14 = branch(x10, RIGHT, x13)
    x15 = x5(x14)
    O = fill(x1, x4, x15)
    return O

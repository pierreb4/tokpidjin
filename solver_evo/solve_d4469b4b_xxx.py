def solve_d4469b4b_one(S, I):
    return fill(canvas(BLACK, THREE_BY_THREE), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), fork(combine, vfrontier, hfrontier)(branch(equality(other_f(palette_t(I), BLACK), c_iz_n(S, identity(p_g), rbind(get_nth_t, F1))), RIGHT, branch(equality(other_f(palette_t(I), BLACK), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), UNITY, TWO_BY_TWO))))


def solve_d4469b4b(S, I, x=0):
    x1 = canvas(BLACK, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = identity(p_g)
    if x == 2:
        return x2
    x3 = rbind(get_nth_t, F0)
    if x == 3:
        return x3
    x4 = c_zo_n(S, x2, x3)
    if x == 4:
        return x4
    x5 = fork(combine, vfrontier, hfrontier)
    if x == 5:
        return x5
    x6 = palette_t(I)
    if x == 6:
        return x6
    x7 = other_f(x6, BLACK)
    if x == 7:
        return x7
    x8 = rbind(get_nth_t, F1)
    if x == 8:
        return x8
    x9 = c_iz_n(S, x2, x8)
    if x == 9:
        return x9
    x10 = equality(x7, x9)
    if x == 10:
        return x10
    x11 = c_iz_n(S, x2, x3)
    if x == 11:
        return x11
    x12 = equality(x7, x11)
    if x == 12:
        return x12
    x13 = branch(x12, UNITY, TWO_BY_TWO)
    if x == 13:
        return x13
    x14 = branch(x10, RIGHT, x13)
    if x == 14:
        return x14
    x15 = x5(x14)
    if x == 15:
        return x15
    O = fill(x1, x4, x15)
    return O

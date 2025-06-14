def solve_2281f1f4_one(S, I):
    return underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), remove_t(corner(f_ofcolor(I, GRAY), R1), apply(fork(astuple, power(rbind(get_nth_f, F0), TWO), power(rbind(get_nth_f, L1), TWO)), product(f_ofcolor(I, GRAY), f_ofcolor(I, GRAY)))))


def solve_2281f1f4(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, GRAY)
    if x == 4:
        return x4
    x5 = corner(x4, R1)
    if x == 5:
        return x5
    x6 = rbind(get_nth_f, F0)
    if x == 6:
        return x6
    x7 = power(x6, TWO)
    if x == 7:
        return x7
    x8 = rbind(get_nth_f, L1)
    if x == 8:
        return x8
    x9 = power(x8, TWO)
    if x == 9:
        return x9
    x10 = fork(astuple, x7, x9)
    if x == 10:
        return x10
    x11 = product(x4, x4)
    if x == 11:
        return x11
    x12 = apply(x10, x11)
    if x == 12:
        return x12
    x13 = remove_t(x5, x12)
    if x == 13:
        return x13
    O = underfill(I, x3, x13)
    return O

def solve_2281f1f4_one(S, I):
    return underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), remove_t(corner(f_ofcolor(I, GRAY), R1), apply(fork(astuple, power(rbind(get_nth_f, F0), TWO), power(rbind(get_nth_f, L1), TWO)), product(f_ofcolor(I, GRAY), f_ofcolor(I, GRAY)))))


def solve_2281f1f4(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = f_ofcolor(I, GRAY)
    x5 = corner(x4, R1)
    x6 = rbind(get_nth_f, F0)
    x7 = power(x6, TWO)
    x8 = rbind(get_nth_f, L1)
    x9 = power(x8, TWO)
    x10 = fork(astuple, x7, x9)
    x11 = product(x4, x4)
    x12 = apply(x10, x11)
    x13 = remove_t(x5, x12)
    O = underfill(I, x3, x13)
    return O

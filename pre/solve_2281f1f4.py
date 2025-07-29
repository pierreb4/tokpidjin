def solve_2281f1f4_one(S, I):
    return underfill(I, TWO, remove_t(corner(f_ofcolor(I, FIVE), R1), apply(fork(astuple, power(rbind(get_nth_f, F0), TWO), power(rbind(get_nth_f, L1), TWO)), product(f_ofcolor(I, FIVE), f_ofcolor(I, FIVE)))))


def solve_2281f1f4(S, I):
    x1 = f_ofcolor(I, FIVE)
    x2 = corner(x1, R1)
    x3 = rbind(get_nth_f, F0)
    x4 = power(x3, TWO)
    x5 = rbind(get_nth_f, L1)
    x6 = power(x5, TWO)
    x7 = fork(astuple, x4, x6)
    x8 = product(x1, x1)
    x9 = apply(x7, x8)
    x10 = remove_t(x2, x9)
    O = underfill(I, TWO, x10)
    return O

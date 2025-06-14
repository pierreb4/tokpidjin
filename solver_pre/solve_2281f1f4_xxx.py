def solve_2281f1f4_one(S, I):
    return underfill(I, TWO, remove_t(corner(f_ofcolor(I, FIVE), R1), apply(fork(astuple, power(rbind(get_nth_f, F0), TWO), power(rbind(get_nth_f, L1), TWO)), product(f_ofcolor(I, FIVE), f_ofcolor(I, FIVE)))))


def solve_2281f1f4(S, I, x=0):
    x1 = f_ofcolor(I, FIVE)
    if x == 1:
        return x1
    x2 = corner(x1, R1)
    if x == 2:
        return x2
    x3 = rbind(get_nth_f, F0)
    if x == 3:
        return x3
    x4 = power(x3, TWO)
    if x == 4:
        return x4
    x5 = rbind(get_nth_f, L1)
    if x == 5:
        return x5
    x6 = power(x5, TWO)
    if x == 6:
        return x6
    x7 = fork(astuple, x4, x6)
    if x == 7:
        return x7
    x8 = product(x1, x1)
    if x == 8:
        return x8
    x9 = apply(x7, x8)
    if x == 9:
        return x9
    x10 = remove_t(x2, x9)
    if x == 10:
        return x10
    O = underfill(I, TWO, x10)
    return O

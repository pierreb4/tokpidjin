def solve_ef135b50_one(S, I):
    return paint(I, shift(asobject(trim(fill(I, NINE, intersection(mapply(fork(connect, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), sfilter_f(product(f_ofcolor(I, TWO), f_ofcolor(I, TWO)), fork(equality, power(rbind(get_nth_f, F0), TWO), compose(rbind(get_nth_f, F0), rbind(get_nth_f, L1))))), f_ofcolor(I, ZERO))))), UNITY))


def solve_ef135b50(S, I):
    x1 = rbind(get_nth_f, F0)
    x2 = rbind(get_nth_f, L1)
    x3 = fork(connect, x1, x2)
    x4 = f_ofcolor(I, TWO)
    x5 = product(x4, x4)
    x6 = power(x1, TWO)
    x7 = compose(x1, x2)
    x8 = fork(equality, x6, x7)
    x9 = sfilter_f(x5, x8)
    x10 = mapply(x3, x9)
    x11 = f_ofcolor(I, ZERO)
    x12 = intersection(x10, x11)
    x13 = fill(I, NINE, x12)
    x14 = trim(x13)
    x15 = asobject(x14)
    x16 = shift(x15, UNITY)
    O = paint(I, x16)
    return O

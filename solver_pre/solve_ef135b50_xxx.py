def solve_ef135b50_one(S, I):
    return paint(I, shift(asobject(trim(fill(I, NINE, intersection(mapply(fork(connect, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), sfilter_f(product(f_ofcolor(I, TWO), f_ofcolor(I, TWO)), fork(equality, power(rbind(get_nth_f, F0), TWO), compose(rbind(get_nth_f, F0), rbind(get_nth_f, L1))))), f_ofcolor(I, ZERO))))), UNITY))


def solve_ef135b50(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, L1)
    if x == 2:
        return x2
    x3 = fork(connect, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, TWO)
    if x == 4:
        return x4
    x5 = product(x4, x4)
    if x == 5:
        return x5
    x6 = power(x1, TWO)
    if x == 6:
        return x6
    x7 = compose(x1, x2)
    if x == 7:
        return x7
    x8 = fork(equality, x6, x7)
    if x == 8:
        return x8
    x9 = sfilter_f(x5, x8)
    if x == 9:
        return x9
    x10 = mapply(x3, x9)
    if x == 10:
        return x10
    x11 = f_ofcolor(I, ZERO)
    if x == 11:
        return x11
    x12 = intersection(x10, x11)
    if x == 12:
        return x12
    x13 = fill(I, NINE, x12)
    if x == 13:
        return x13
    x14 = trim(x13)
    if x == 14:
        return x14
    x15 = asobject(x14)
    if x == 15:
        return x15
    x16 = shift(x15, UNITY)
    if x == 16:
        return x16
    O = paint(I, x16)
    return O

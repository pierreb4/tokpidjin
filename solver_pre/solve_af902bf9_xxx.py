def solve_af902bf9_one(S, I):
    return replace(fill(underfill(I, NEG_ONE, mfilter_f(prapply(connect, f_ofcolor(I, FOUR), f_ofcolor(I, FOUR)), fork(either, vline_i, hline_i))), TWO, mapply(compose(backdrop, inbox), o_g(underfill(I, NEG_ONE, mfilter_f(prapply(connect, f_ofcolor(I, FOUR), f_ofcolor(I, FOUR)), fork(either, vline_i, hline_i))), R1))), NEG_ONE, ZERO)


def solve_af902bf9(S, I, x=0):
    x1 = f_ofcolor(I, FOUR)
    if x == 1:
        return x1
    x2 = prapply(connect, x1, x1)
    if x == 2:
        return x2
    x3 = fork(either, vline_i, hline_i)
    if x == 3:
        return x3
    x4 = mfilter_f(x2, x3)
    if x == 4:
        return x4
    x5 = underfill(I, NEG_ONE, x4)
    if x == 5:
        return x5
    x6 = compose(backdrop, inbox)
    if x == 6:
        return x6
    x7 = o_g(x5, R1)
    if x == 7:
        return x7
    x8 = mapply(x6, x7)
    if x == 8:
        return x8
    x9 = fill(x5, TWO, x8)
    if x == 9:
        return x9
    O = replace(x9, NEG_ONE, ZERO)
    return O

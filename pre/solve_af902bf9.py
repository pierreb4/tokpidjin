def solve_af902bf9_one(S, I):
    return replace(fill(underfill(I, NEG_ONE, mfilter_f(prapply(connect, f_ofcolor(I, FOUR), f_ofcolor(I, FOUR)), fork(either, vline_i, hline_i))), TWO, mapply(compose(backdrop, inbox), o_g(underfill(I, NEG_ONE, mfilter_f(prapply(connect, f_ofcolor(I, FOUR), f_ofcolor(I, FOUR)), fork(either, vline_i, hline_i))), R1))), NEG_ONE, ZERO)


def solve_af902bf9(S, I):
    x1 = f_ofcolor(I, FOUR)
    x2 = prapply(connect, x1, x1)
    x3 = fork(either, vline_i, hline_i)
    x4 = mfilter_f(x2, x3)
    x5 = underfill(I, NEG_ONE, x4)
    x6 = compose(backdrop, inbox)
    x7 = o_g(x5, R1)
    x8 = mapply(x6, x7)
    x9 = fill(x5, TWO, x8)
    O = replace(x9, NEG_ONE, ZERO)
    return O

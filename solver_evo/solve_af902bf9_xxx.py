def solve_af902bf9_one(S, I):
    return replace(fill(underfill(I, NEG_ONE, mfilter_f(prapply(connect, f_ofcolor(I, YELLOW), f_ofcolor(I, YELLOW)), fork(either, vline_i, hline_i))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(compose(backdrop, inbox), o_g(underfill(I, NEG_ONE, mfilter_f(prapply(connect, f_ofcolor(I, YELLOW), f_ofcolor(I, YELLOW)), fork(either, vline_i, hline_i))), R1))), NEG_ONE, BLACK)


def solve_af902bf9(S, I):
    x1 = f_ofcolor(I, YELLOW)
    x2 = prapply(connect, x1, x1)
    x3 = fork(either, vline_i, hline_i)
    x4 = mfilter_f(x2, x3)
    x5 = underfill(I, NEG_ONE, x4)
    x6 = identity(p_g)
    x7 = rbind(get_nth_t, F0)
    x8 = c_zo_n(S, x6, x7)
    x9 = compose(backdrop, inbox)
    x10 = o_g(x5, R1)
    x11 = mapply(x9, x10)
    x12 = fill(x5, x8, x11)
    O = replace(x12, NEG_ONE, BLACK)
    return O

def solve_af902bf9_one(S, I):
    return replace(fill(underfill(I, NEG_ONE, mfilter_f(prapply(connect, f_ofcolor(I, YELLOW), f_ofcolor(I, YELLOW)), fork(either, vline_i, hline_i))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(compose(backdrop, inbox), o_g(underfill(I, NEG_ONE, mfilter_f(prapply(connect, f_ofcolor(I, YELLOW), f_ofcolor(I, YELLOW)), fork(either, vline_i, hline_i))), R1))), NEG_ONE, BLACK)


def solve_af902bf9(S, I, x=0):
    x1 = f_ofcolor(I, YELLOW)
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
    x6 = identity(p_g)
    if x == 6:
        return x6
    x7 = rbind(get_nth_t, F0)
    if x == 7:
        return x7
    x8 = c_zo_n(S, x6, x7)
    if x == 8:
        return x8
    x9 = compose(backdrop, inbox)
    if x == 9:
        return x9
    x10 = o_g(x5, R1)
    if x == 10:
        return x10
    x11 = mapply(x9, x10)
    if x == 11:
        return x11
    x12 = fill(x5, x8, x11)
    if x == 12:
        return x12
    O = replace(x12, NEG_ONE, BLACK)
    return O

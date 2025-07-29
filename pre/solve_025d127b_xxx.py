def solve_025d127b_one(S, I):
    return move(I, difference(merge_f(o_g(I, R5)), mapply(compose(rbind(rbind(get_arg_rank, F0), rbind(col_row, R3)), lbind(colorfilter, o_g(I, R5))), apply(color, o_g(I, R5)))), RIGHT)


def solve_025d127b(S, I):
    x1 = o_g(I, R5)
    x2 = merge_f(x1)
    x3 = rbind(get_arg_rank, F0)
    x4 = rbind(col_row, R3)
    x5 = rbind(x3, x4)
    x6 = lbind(colorfilter, x1)
    x7 = compose(x5, x6)
    x8 = apply(color, x1)
    x9 = mapply(x7, x8)
    x10 = difference(x2, x9)
    O = move(I, x10, RIGHT)
    return O

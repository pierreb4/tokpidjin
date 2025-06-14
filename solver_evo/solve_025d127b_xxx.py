def solve_025d127b_one(S, I):
    return move(I, difference(merge_f(o_g(I, R5)), mapply(compose(rbind(rbind(get_arg_rank, F0), rbind(col_row, R3)), lbind(colorfilter, o_g(I, R5))), apply(color, o_g(I, R5)))), RIGHT)


def solve_025d127b(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = rbind(get_arg_rank, F0)
    if x == 3:
        return x3
    x4 = rbind(col_row, R3)
    if x == 4:
        return x4
    x5 = rbind(x3, x4)
    if x == 5:
        return x5
    x6 = lbind(colorfilter, x1)
    if x == 6:
        return x6
    x7 = compose(x5, x6)
    if x == 7:
        return x7
    x8 = apply(color, x1)
    if x == 8:
        return x8
    x9 = mapply(x7, x8)
    if x == 9:
        return x9
    x10 = difference(x2, x9)
    if x == 10:
        return x10
    O = move(I, x10, RIGHT)
    return O

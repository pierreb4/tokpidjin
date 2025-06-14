def solve_06df4c85_one(S, I):
    return fill(paint(I, mfilter_f(apply(fork(recolor_i, color, fork(connect, compose(rbind(get_nth_f, L1), rbind(get_nth_f, F0)), power(rbind(get_nth_f, L1), TWO))), sfilter_f(product(merge_f(remove_f(get_arg_rank_f(partition(I), size, F0), difference(partition(I), colorfilter(partition(I), ZERO)))), merge_f(remove_f(get_arg_rank_f(partition(I), size, F0), difference(partition(I), colorfilter(partition(I), ZERO))))), fork(equality, power(rbind(get_nth_f, F0), TWO), compose(rbind(get_nth_f, F0), rbind(get_nth_f, L1))))), fork(either, vline_o, hline_o))), get_color_rank_t(I, F0), f_ofcolor(I, get_color_rank_t(I, F0)))


def solve_06df4c85(S, I, x=0):
    x1 = rbind(get_nth_f, L1)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, F0)
    if x == 2:
        return x2
    x3 = compose(x1, x2)
    if x == 3:
        return x3
    x4 = power(x1, TWO)
    if x == 4:
        return x4
    x5 = fork(connect, x3, x4)
    if x == 5:
        return x5
    x6 = fork(recolor_i, color, x5)
    if x == 6:
        return x6
    x7 = partition(I)
    if x == 7:
        return x7
    x8 = get_arg_rank_f(x7, size, F0)
    if x == 8:
        return x8
    x9 = colorfilter(x7, ZERO)
    if x == 9:
        return x9
    x10 = difference(x7, x9)
    if x == 10:
        return x10
    x11 = remove_f(x8, x10)
    if x == 11:
        return x11
    x12 = merge_f(x11)
    if x == 12:
        return x12
    x13 = product(x12, x12)
    if x == 13:
        return x13
    x14 = power(x2, TWO)
    if x == 14:
        return x14
    x15 = compose(x2, x1)
    if x == 15:
        return x15
    x16 = fork(equality, x14, x15)
    if x == 16:
        return x16
    x17 = sfilter_f(x13, x16)
    if x == 17:
        return x17
    x18 = apply(x6, x17)
    if x == 18:
        return x18
    x19 = fork(either, vline_o, hline_o)
    if x == 19:
        return x19
    x20 = mfilter_f(x18, x19)
    if x == 20:
        return x20
    x21 = paint(I, x20)
    if x == 21:
        return x21
    x22 = get_color_rank_t(I, F0)
    if x == 22:
        return x22
    x23 = f_ofcolor(I, x22)
    if x == 23:
        return x23
    O = fill(x21, x22, x23)
    return O

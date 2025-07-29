def solve_834ec97d_one(S, I):
    return fill(paint(fill(I, ZERO, get_nth_f(o_g(I, R5), F0)), shift(get_nth_f(o_g(I, R5), F0), DOWN)), FOUR, sfilter_f(sfilter_f(asindices(I), compose(lbind(greater, col_row(shift(get_nth_f(o_g(I, R5), F0), DOWN), R1)), rbind(get_nth_f, F0))), compose(rbind(contained, interval(subtract(col_row(shift(get_nth_f(o_g(I, R5), F0), DOWN), R2), TEN), add(col_row(shift(get_nth_f(o_g(I, R5), F0), DOWN), R2), TEN), TWO)), rbind(get_nth_f, L1))))


def solve_834ec97d(S, I):
    x1 = o_g(I, R5)
    x2 = get_nth_f(x1, F0)
    x3 = fill(I, ZERO, x2)
    x4 = shift(x2, DOWN)
    x5 = paint(x3, x4)
    x6 = asindices(I)
    x7 = col_row(x4, R1)
    x8 = lbind(greater, x7)
    x9 = rbind(get_nth_f, F0)
    x10 = compose(x8, x9)
    x11 = sfilter_f(x6, x10)
    x12 = col_row(x4, R2)
    x13 = subtract(x12, TEN)
    x14 = add(x12, TEN)
    x15 = interval(x13, x14, TWO)
    x16 = rbind(contained, x15)
    x17 = rbind(get_nth_f, L1)
    x18 = compose(x16, x17)
    x19 = sfilter_f(x11, x18)
    O = fill(x5, FOUR, x19)
    return O

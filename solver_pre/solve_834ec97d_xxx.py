def solve_834ec97d_one(S, I):
    return fill(paint(fill(I, ZERO, get_nth_f(o_g(I, R5), F0)), shift(get_nth_f(o_g(I, R5), F0), DOWN)), FOUR, sfilter_f(sfilter_f(asindices(I), compose(lbind(greater, col_row(shift(get_nth_f(o_g(I, R5), F0), DOWN), R1)), rbind(get_nth_f, F0))), compose(rbind(contained, interval(subtract(col_row(shift(get_nth_f(o_g(I, R5), F0), DOWN), R2), TEN), add(col_row(shift(get_nth_f(o_g(I, R5), F0), DOWN), R2), TEN), TWO)), rbind(get_nth_f, L1))))


def solve_834ec97d(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = fill(I, ZERO, x2)
    if x == 3:
        return x3
    x4 = shift(x2, DOWN)
    if x == 4:
        return x4
    x5 = paint(x3, x4)
    if x == 5:
        return x5
    x6 = asindices(I)
    if x == 6:
        return x6
    x7 = col_row(x4, R1)
    if x == 7:
        return x7
    x8 = lbind(greater, x7)
    if x == 8:
        return x8
    x9 = rbind(get_nth_f, F0)
    if x == 9:
        return x9
    x10 = compose(x8, x9)
    if x == 10:
        return x10
    x11 = sfilter_f(x6, x10)
    if x == 11:
        return x11
    x12 = col_row(x4, R2)
    if x == 12:
        return x12
    x13 = subtract(x12, TEN)
    if x == 13:
        return x13
    x14 = add(x12, TEN)
    if x == 14:
        return x14
    x15 = interval(x13, x14, TWO)
    if x == 15:
        return x15
    x16 = rbind(contained, x15)
    if x == 16:
        return x16
    x17 = rbind(get_nth_f, L1)
    if x == 17:
        return x17
    x18 = compose(x16, x17)
    if x == 18:
        return x18
    x19 = sfilter_f(x11, x18)
    if x == 19:
        return x19
    O = fill(x5, FOUR, x19)
    return O

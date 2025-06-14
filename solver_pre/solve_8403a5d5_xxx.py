def solve_8403a5d5_one(S, I):
    return fill(fill(fill(I, color(get_nth_f(o_g(I, R5), F0)), sfilter(asindices(I), compose(rbind(contained, interval(col_row(get_nth_f(o_g(I, R5), F0), R2), TEN, TWO)), rbind(get_nth_f, L1)))), FIVE, apply(tojvec, interval(increment(col_row(get_nth_f(o_g(I, R5), F0), R2)), TEN, FOUR))), FIVE, apply(lbind(astuple, NINE), interval(add(col_row(get_nth_f(o_g(I, R5), F0), R2), THREE), TEN, FOUR)))


def solve_8403a5d5(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = color(x2)
    if x == 3:
        return x3
    x4 = asindices(I)
    if x == 4:
        return x4
    x5 = col_row(x2, R2)
    if x == 5:
        return x5
    x6 = interval(x5, TEN, TWO)
    if x == 6:
        return x6
    x7 = rbind(contained, x6)
    if x == 7:
        return x7
    x8 = rbind(get_nth_f, L1)
    if x == 8:
        return x8
    x9 = compose(x7, x8)
    if x == 9:
        return x9
    x10 = sfilter(x4, x9)
    if x == 10:
        return x10
    x11 = fill(I, x3, x10)
    if x == 11:
        return x11
    x12 = increment(x5)
    if x == 12:
        return x12
    x13 = interval(x12, TEN, FOUR)
    if x == 13:
        return x13
    x14 = apply(tojvec, x13)
    if x == 14:
        return x14
    x15 = fill(x11, FIVE, x14)
    if x == 15:
        return x15
    x16 = lbind(astuple, NINE)
    if x == 16:
        return x16
    x17 = add(x5, THREE)
    if x == 17:
        return x17
    x18 = interval(x17, TEN, FOUR)
    if x == 18:
        return x18
    x19 = apply(x16, x18)
    if x == 19:
        return x19
    O = fill(x15, FIVE, x19)
    return O

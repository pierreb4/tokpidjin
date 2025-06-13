def solve_8403a5d5_one(S, I):
    return fill(fill(fill(I, color(get_nth_f(o_g(I, R5), F0)), sfilter(asindices(I), compose(rbind(contained, interval(col_row(get_nth_f(o_g(I, R5), F0), R2), TEN, TWO)), rbind(get_nth_f, L1)))), FIVE, apply(tojvec, interval(increment(col_row(get_nth_f(o_g(I, R5), F0), R2)), TEN, FOUR))), FIVE, apply(lbind(astuple, NINE), interval(add(col_row(get_nth_f(o_g(I, R5), F0), R2), THREE), TEN, FOUR)))


def solve_8403a5d5(S, I):
    x1 = o_g(I, R5)
    x2 = get_nth_f(x1, F0)
    x3 = color(x2)
    x4 = asindices(I)
    x5 = col_row(x2, R2)
    x6 = interval(x5, TEN, TWO)
    x7 = rbind(contained, x6)
    x8 = rbind(get_nth_f, L1)
    x9 = compose(x7, x8)
    x10 = sfilter(x4, x9)
    x11 = fill(I, x3, x10)
    x12 = increment(x5)
    x13 = interval(x12, TEN, FOUR)
    x14 = apply(tojvec, x13)
    x15 = fill(x11, FIVE, x14)
    x16 = lbind(astuple, NINE)
    x17 = add(x5, THREE)
    x18 = interval(x17, TEN, FOUR)
    x19 = apply(x16, x18)
    O = fill(x15, FIVE, x19)
    return O

def solve_5c2c9af4_one(S, I):
    return fill(I, get_color_rank_t(I, L1), shift(mapply(box, pair(apply(lbind(multiply, subtract(center(f_ofcolor(I, get_color_rank_t(I, L1))), corner(f_ofcolor(I, get_color_rank_t(I, L1)), R0))), interval(ZERO, NINE, ONE)), apply(lbind(multiply, subtract(center(f_ofcolor(I, get_color_rank_t(I, L1))), corner(f_ofcolor(I, get_color_rank_t(I, L1)), R0))), interval(ZERO, multiply(NEG_ONE, NINE), NEG_ONE)))), center(f_ofcolor(I, get_color_rank_t(I, L1)))))


def solve_5c2c9af4(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, x1)
    if x == 2:
        return x2
    x3 = center(x2)
    if x == 3:
        return x3
    x4 = corner(x2, R0)
    if x == 4:
        return x4
    x5 = subtract(x3, x4)
    if x == 5:
        return x5
    x6 = lbind(multiply, x5)
    if x == 6:
        return x6
    x7 = interval(ZERO, NINE, ONE)
    if x == 7:
        return x7
    x8 = apply(x6, x7)
    if x == 8:
        return x8
    x9 = multiply(NEG_ONE, NINE)
    if x == 9:
        return x9
    x10 = interval(ZERO, x9, NEG_ONE)
    if x == 10:
        return x10
    x11 = apply(x6, x10)
    if x == 11:
        return x11
    x12 = pair(x8, x11)
    if x == 12:
        return x12
    x13 = mapply(box, x12)
    if x == 13:
        return x13
    x14 = shift(x13, x3)
    if x == 14:
        return x14
    O = fill(I, x1, x14)
    return O

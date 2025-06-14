def solve_1f0c79e5_one(S, I):
    return paint(I, mapply(lbind(shift, recolor_i(get_color_rank_t(replace(I, RED, BLACK), L1), combine_f(f_ofcolor(I, RED), f_ofcolor(replace(I, RED, BLACK), get_color_rank_t(replace(I, RED, BLACK), L1))))), prapply(multiply, apply(compose(decrement, double), shift(f_ofcolor(I, RED), invert(corner(combine_f(f_ofcolor(I, RED), f_ofcolor(replace(I, RED, BLACK), get_color_rank_t(replace(I, RED, BLACK), L1))), R0)))), interval(ZERO, NINE, ONE))))


def solve_1f0c79e5(S, I, x=0):
    x1 = replace(I, RED, BLACK)
    if x == 1:
        return x1
    x2 = get_color_rank_t(x1, L1)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, RED)
    if x == 3:
        return x3
    x4 = f_ofcolor(x1, x2)
    if x == 4:
        return x4
    x5 = combine_f(x3, x4)
    if x == 5:
        return x5
    x6 = recolor_i(x2, x5)
    if x == 6:
        return x6
    x7 = lbind(shift, x6)
    if x == 7:
        return x7
    x8 = compose(decrement, double)
    if x == 8:
        return x8
    x9 = corner(x5, R0)
    if x == 9:
        return x9
    x10 = invert(x9)
    if x == 10:
        return x10
    x11 = shift(x3, x10)
    if x == 11:
        return x11
    x12 = apply(x8, x11)
    if x == 12:
        return x12
    x13 = interval(ZERO, NINE, ONE)
    if x == 13:
        return x13
    x14 = prapply(multiply, x12, x13)
    if x == 14:
        return x14
    x15 = mapply(x7, x14)
    if x == 15:
        return x15
    O = paint(I, x15)
    return O

def solve_56dc2b01_one(S, I):
    return move(paint(I, shift(recolor_i(EIGHT, f_ofcolor(I, TWO)), crement(multiply(sign(gravitate(f_ofcolor(I, TWO), get_nth_f(colorfilter(o_g(I, R5), THREE), F0))), branch(equality(get_nth_f(gravitate(get_nth_f(colorfilter(o_g(I, R5), THREE), F0), f_ofcolor(I, TWO)), F0), ZERO), width_f, height_f)(get_nth_f(colorfilter(o_g(I, R5), THREE), F0)))))), get_nth_f(colorfilter(o_g(I, R5), THREE), F0), gravitate(get_nth_f(colorfilter(o_g(I, R5), THREE), F0), f_ofcolor(I, TWO)))


def solve_56dc2b01(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = recolor_i(EIGHT, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = colorfilter(x3, THREE)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = gravitate(x1, x5)
    if x == 6:
        return x6
    x7 = sign(x6)
    if x == 7:
        return x7
    x8 = gravitate(x5, x1)
    if x == 8:
        return x8
    x9 = get_nth_f(x8, F0)
    if x == 9:
        return x9
    x10 = equality(x9, ZERO)
    if x == 10:
        return x10
    x11 = branch(x10, width_f, height_f)
    if x == 11:
        return x11
    x12 = x11(x5)
    if x == 12:
        return x12
    x13 = multiply(x7, x12)
    if x == 13:
        return x13
    x14 = crement(x13)
    if x == 14:
        return x14
    x15 = shift(x2, x14)
    if x == 15:
        return x15
    x16 = paint(I, x15)
    if x == 16:
        return x16
    O = move(x16, x5, x8)
    return O

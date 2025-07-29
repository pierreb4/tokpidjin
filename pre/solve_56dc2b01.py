def solve_56dc2b01_one(S, I):
    return move(paint(I, shift(recolor_i(EIGHT, f_ofcolor(I, TWO)), crement(multiply(sign(gravitate(f_ofcolor(I, TWO), get_nth_f(colorfilter(o_g(I, R5), THREE), F0))), branch(equality(get_nth_f(gravitate(get_nth_f(colorfilter(o_g(I, R5), THREE), F0), f_ofcolor(I, TWO)), F0), ZERO), width_f, height_f)(get_nth_f(colorfilter(o_g(I, R5), THREE), F0)))))), get_nth_f(colorfilter(o_g(I, R5), THREE), F0), gravitate(get_nth_f(colorfilter(o_g(I, R5), THREE), F0), f_ofcolor(I, TWO)))


def solve_56dc2b01(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = recolor_i(EIGHT, x1)
    x3 = o_g(I, R5)
    x4 = colorfilter(x3, THREE)
    x5 = get_nth_f(x4, F0)
    x6 = gravitate(x1, x5)
    x7 = sign(x6)
    x8 = gravitate(x5, x1)
    x9 = get_nth_f(x8, F0)
    x10 = equality(x9, ZERO)
    x11 = branch(x10, width_f, height_f)
    x12 = x11(x5)
    x13 = multiply(x7, x12)
    x14 = crement(x13)
    x15 = shift(x2, x14)
    x16 = paint(I, x15)
    O = move(x16, x5, x8)
    return O

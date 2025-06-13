def solve_56dc2b01_one(S, I):
    return move(paint(I, shift(recolor_i(c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), f_ofcolor(I, RED)), crement(multiply(sign(gravitate(f_ofcolor(I, RED), get_nth_f(colorfilter(o_g(I, R5), GREEN), F0))), branch(equality(get_nth_f(gravitate(get_nth_f(colorfilter(o_g(I, R5), GREEN), F0), f_ofcolor(I, RED)), F0), BLACK), width_f, height_f)(get_nth_f(colorfilter(o_g(I, R5), GREEN), F0)))))), get_nth_f(colorfilter(o_g(I, R5), GREEN), F0), gravitate(get_nth_f(colorfilter(o_g(I, R5), GREEN), F0), f_ofcolor(I, RED)))


def solve_56dc2b01(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = f_ofcolor(I, RED)
    x5 = recolor_i(x3, x4)
    x6 = o_g(I, R5)
    x7 = colorfilter(x6, GREEN)
    x8 = get_nth_f(x7, F0)
    x9 = gravitate(x4, x8)
    x10 = sign(x9)
    x11 = gravitate(x8, x4)
    x12 = get_nth_f(x11, F0)
    x13 = equality(x12, BLACK)
    x14 = branch(x13, width_f, height_f)
    x15 = x14(x8)
    x16 = multiply(x10, x15)
    x17 = crement(x16)
    x18 = shift(x5, x17)
    x19 = paint(I, x18)
    O = move(x19, x8, x11)
    return O

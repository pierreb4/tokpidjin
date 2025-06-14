def solve_56dc2b01_one(S, I):
    return move(paint(I, shift(recolor_i(c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), f_ofcolor(I, RED)), crement(multiply(sign(gravitate(f_ofcolor(I, RED), get_nth_f(colorfilter(o_g(I, R5), GREEN), F0))), branch(equality(get_nth_f(gravitate(get_nth_f(colorfilter(o_g(I, R5), GREEN), F0), f_ofcolor(I, RED)), F0), BLACK), width_f, height_f)(get_nth_f(colorfilter(o_g(I, R5), GREEN), F0)))))), get_nth_f(colorfilter(o_g(I, R5), GREEN), F0), gravitate(get_nth_f(colorfilter(o_g(I, R5), GREEN), F0), f_ofcolor(I, RED)))


def solve_56dc2b01(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, RED)
    if x == 4:
        return x4
    x5 = recolor_i(x3, x4)
    if x == 5:
        return x5
    x6 = o_g(I, R5)
    if x == 6:
        return x6
    x7 = colorfilter(x6, GREEN)
    if x == 7:
        return x7
    x8 = get_nth_f(x7, F0)
    if x == 8:
        return x8
    x9 = gravitate(x4, x8)
    if x == 9:
        return x9
    x10 = sign(x9)
    if x == 10:
        return x10
    x11 = gravitate(x8, x4)
    if x == 11:
        return x11
    x12 = get_nth_f(x11, F0)
    if x == 12:
        return x12
    x13 = equality(x12, BLACK)
    if x == 13:
        return x13
    x14 = branch(x13, width_f, height_f)
    if x == 14:
        return x14
    x15 = x14(x8)
    if x == 15:
        return x15
    x16 = multiply(x10, x15)
    if x == 16:
        return x16
    x17 = crement(x16)
    if x == 17:
        return x17
    x18 = shift(x5, x17)
    if x == 18:
        return x18
    x19 = paint(I, x18)
    if x == 19:
        return x19
    O = move(x19, x8, x11)
    return O

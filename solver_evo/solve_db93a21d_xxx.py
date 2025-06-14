def solve_db93a21d_one(S, I):
    return fill(fill(fill(underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), mapply(rbind(shoot, DOWN), f_ofcolor(I, BURGUNDY))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(outbox, colorfilter(o_g(I, R7), BURGUNDY))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(power(outbox, TWO), sfilter_f(colorfilter(o_g(I, R7), BURGUNDY), compose(rbind(greater, c_zo_n(S, identity(p_g), rbind(get_nth_t, F1))), compose(halve, width_f))))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(power(outbox, THREE), sfilter_f(colorfilter(o_g(I, R7), BURGUNDY), matcher(compose(halve, width_f), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0))))))


def solve_db93a21d(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F1)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = rbind(shoot, DOWN)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, BURGUNDY)
    if x == 5:
        return x5
    x6 = mapply(x4, x5)
    if x == 6:
        return x6
    x7 = underfill(I, x3, x6)
    if x == 7:
        return x7
    x8 = rbind(get_nth_t, F0)
    if x == 8:
        return x8
    x9 = c_zo_n(S, x1, x8)
    if x == 9:
        return x9
    x10 = o_g(I, R7)
    if x == 10:
        return x10
    x11 = colorfilter(x10, BURGUNDY)
    if x == 11:
        return x11
    x12 = mapply(outbox, x11)
    if x == 12:
        return x12
    x13 = fill(x7, x9, x12)
    if x == 13:
        return x13
    x14 = power(outbox, TWO)
    if x == 14:
        return x14
    x15 = rbind(greater, x3)
    if x == 15:
        return x15
    x16 = compose(halve, width_f)
    if x == 16:
        return x16
    x17 = compose(x15, x16)
    if x == 17:
        return x17
    x18 = sfilter_f(x11, x17)
    if x == 18:
        return x18
    x19 = mapply(x14, x18)
    if x == 19:
        return x19
    x20 = fill(x13, x9, x19)
    if x == 20:
        return x20
    x21 = power(outbox, THREE)
    if x == 21:
        return x21
    x22 = matcher(x16, x9)
    if x == 22:
        return x22
    x23 = sfilter_f(x11, x22)
    if x == 23:
        return x23
    x24 = mapply(x21, x23)
    if x == 24:
        return x24
    O = fill(x20, x9, x24)
    return O

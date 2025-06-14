def solve_db93a21d_one(S, I):
    return fill(fill(fill(underfill(I, ONE, mapply(rbind(shoot, DOWN), f_ofcolor(I, NINE))), THREE, mapply(outbox, colorfilter(o_g(I, R7), NINE))), THREE, mapply(power(outbox, TWO), sfilter_f(colorfilter(o_g(I, R7), NINE), compose(rbind(greater, ONE), compose(halve, width_f))))), THREE, mapply(power(outbox, THREE), sfilter_f(colorfilter(o_g(I, R7), NINE), matcher(compose(halve, width_f), THREE))))


def solve_db93a21d(S, I, x=0):
    x1 = rbind(shoot, DOWN)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, NINE)
    if x == 2:
        return x2
    x3 = mapply(x1, x2)
    if x == 3:
        return x3
    x4 = underfill(I, ONE, x3)
    if x == 4:
        return x4
    x5 = o_g(I, R7)
    if x == 5:
        return x5
    x6 = colorfilter(x5, NINE)
    if x == 6:
        return x6
    x7 = mapply(outbox, x6)
    if x == 7:
        return x7
    x8 = fill(x4, THREE, x7)
    if x == 8:
        return x8
    x9 = power(outbox, TWO)
    if x == 9:
        return x9
    x10 = rbind(greater, ONE)
    if x == 10:
        return x10
    x11 = compose(halve, width_f)
    if x == 11:
        return x11
    x12 = compose(x10, x11)
    if x == 12:
        return x12
    x13 = sfilter_f(x6, x12)
    if x == 13:
        return x13
    x14 = mapply(x9, x13)
    if x == 14:
        return x14
    x15 = fill(x8, THREE, x14)
    if x == 15:
        return x15
    x16 = power(outbox, THREE)
    if x == 16:
        return x16
    x17 = matcher(x11, THREE)
    if x == 17:
        return x17
    x18 = sfilter_f(x6, x17)
    if x == 18:
        return x18
    x19 = mapply(x16, x18)
    if x == 19:
        return x19
    O = fill(x15, THREE, x19)
    return O

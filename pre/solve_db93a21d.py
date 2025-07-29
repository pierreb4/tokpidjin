def solve_db93a21d_one(S, I):
    return fill(fill(fill(underfill(I, ONE, mapply(rbind(shoot, DOWN), f_ofcolor(I, NINE))), THREE, mapply(outbox, colorfilter(o_g(I, R7), NINE))), THREE, mapply(power(outbox, TWO), sfilter_f(colorfilter(o_g(I, R7), NINE), compose(rbind(greater, ONE), compose(halve, width_f))))), THREE, mapply(power(outbox, THREE), sfilter_f(colorfilter(o_g(I, R7), NINE), matcher(compose(halve, width_f), THREE))))


def solve_db93a21d(S, I):
    x1 = rbind(shoot, DOWN)
    x2 = f_ofcolor(I, NINE)
    x3 = mapply(x1, x2)
    x4 = underfill(I, ONE, x3)
    x5 = o_g(I, R7)
    x6 = colorfilter(x5, NINE)
    x7 = mapply(outbox, x6)
    x8 = fill(x4, THREE, x7)
    x9 = power(outbox, TWO)
    x10 = rbind(greater, ONE)
    x11 = compose(halve, width_f)
    x12 = compose(x10, x11)
    x13 = sfilter_f(x6, x12)
    x14 = mapply(x9, x13)
    x15 = fill(x8, THREE, x14)
    x16 = power(outbox, THREE)
    x17 = matcher(x11, THREE)
    x18 = sfilter_f(x6, x17)
    x19 = mapply(x16, x18)
    O = fill(x15, THREE, x19)
    return O

def solve_f9012d9b_one(S, I):
    return subgrid(f_ofcolor(I, ZERO), paint(I, mapply(lbind(shift, mfilter_f(o_g(I, R4), chain(flip, lbind(contained, ZERO), palette_t))), apply(rbind(multiply, astuple(vperiod(asobject(extract(vsplit(I, TWO), chain(flip, lbind(contained, ZERO), palette_t)))), hperiod(asobject(extract(hsplit(I, TWO), chain(flip, lbind(contained, ZERO), palette_t)))))), mapply(neighbors, neighbors(ORIGIN))))))


def solve_f9012d9b(S, I, x=0):
    x1 = f_ofcolor(I, ZERO)
    if x == 1:
        return x1
    x2 = o_g(I, R4)
    if x == 2:
        return x2
    x3 = lbind(contained, ZERO)
    if x == 3:
        return x3
    x4 = chain(flip, x3, palette_t)
    if x == 4:
        return x4
    x5 = mfilter_f(x2, x4)
    if x == 5:
        return x5
    x6 = lbind(shift, x5)
    if x == 6:
        return x6
    x7 = vsplit(I, TWO)
    if x == 7:
        return x7
    x8 = extract(x7, x4)
    if x == 8:
        return x8
    x9 = asobject(x8)
    if x == 9:
        return x9
    x10 = vperiod(x9)
    if x == 10:
        return x10
    x11 = hsplit(I, TWO)
    if x == 11:
        return x11
    x12 = extract(x11, x4)
    if x == 12:
        return x12
    x13 = asobject(x12)
    if x == 13:
        return x13
    x14 = hperiod(x13)
    if x == 14:
        return x14
    x15 = astuple(x10, x14)
    if x == 15:
        return x15
    x16 = rbind(multiply, x15)
    if x == 16:
        return x16
    x17 = neighbors(ORIGIN)
    if x == 17:
        return x17
    x18 = mapply(neighbors, x17)
    if x == 18:
        return x18
    x19 = apply(x16, x18)
    if x == 19:
        return x19
    x20 = mapply(x6, x19)
    if x == 20:
        return x20
    x21 = paint(I, x20)
    if x == 21:
        return x21
    O = subgrid(x1, x21)
    return O

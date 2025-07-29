def solve_f9012d9b_one(S, I):
    return subgrid(f_ofcolor(I, ZERO), paint(I, mapply(lbind(shift, mfilter_f(o_g(I, R4), chain(flip, lbind(contained, ZERO), palette_t))), apply(rbind(multiply, astuple(vperiod(asobject(extract(vsplit(I, TWO), chain(flip, lbind(contained, ZERO), palette_t)))), hperiod(asobject(extract(hsplit(I, TWO), chain(flip, lbind(contained, ZERO), palette_t)))))), mapply(neighbors, neighbors(ORIGIN))))))


def solve_f9012d9b(S, I):
    x1 = f_ofcolor(I, ZERO)
    x2 = o_g(I, R4)
    x3 = lbind(contained, ZERO)
    x4 = chain(flip, x3, palette_t)
    x5 = mfilter_f(x2, x4)
    x6 = lbind(shift, x5)
    x7 = vsplit(I, TWO)
    x8 = extract(x7, x4)
    x9 = asobject(x8)
    x10 = vperiod(x9)
    x11 = hsplit(I, TWO)
    x12 = extract(x11, x4)
    x13 = asobject(x12)
    x14 = hperiod(x13)
    x15 = astuple(x10, x14)
    x16 = rbind(multiply, x15)
    x17 = neighbors(ORIGIN)
    x18 = mapply(neighbors, x17)
    x19 = apply(x16, x18)
    x20 = mapply(x6, x19)
    x21 = paint(I, x20)
    O = subgrid(x1, x21)
    return O

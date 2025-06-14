def solve_f9012d9b_one(S, I):
    return subgrid(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), paint(I, mapply(lbind(shift, mfilter_f(o_g(I, R4), chain(flip, lbind(contained, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), palette_t))), apply(rbind(multiply, astuple(vperiod(asobject(extract(vsplit(I, TWO), chain(flip, lbind(contained, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), palette_t)))), hperiod(asobject(extract(hsplit(I, TWO), chain(flip, lbind(contained, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), palette_t)))))), mapply(neighbors, neighbors(ORIGIN))))))


def solve_f9012d9b(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_iz_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, x3)
    if x == 4:
        return x4
    x5 = o_g(I, R4)
    if x == 5:
        return x5
    x6 = lbind(contained, x3)
    if x == 6:
        return x6
    x7 = chain(flip, x6, palette_t)
    if x == 7:
        return x7
    x8 = mfilter_f(x5, x7)
    if x == 8:
        return x8
    x9 = lbind(shift, x8)
    if x == 9:
        return x9
    x10 = vsplit(I, TWO)
    if x == 10:
        return x10
    x11 = extract(x10, x7)
    if x == 11:
        return x11
    x12 = asobject(x11)
    if x == 12:
        return x12
    x13 = vperiod(x12)
    if x == 13:
        return x13
    x14 = hsplit(I, TWO)
    if x == 14:
        return x14
    x15 = extract(x14, x7)
    if x == 15:
        return x15
    x16 = asobject(x15)
    if x == 16:
        return x16
    x17 = hperiod(x16)
    if x == 17:
        return x17
    x18 = astuple(x13, x17)
    if x == 18:
        return x18
    x19 = rbind(multiply, x18)
    if x == 19:
        return x19
    x20 = neighbors(ORIGIN)
    if x == 20:
        return x20
    x21 = mapply(neighbors, x20)
    if x == 21:
        return x21
    x22 = apply(x19, x21)
    if x == 22:
        return x22
    x23 = mapply(x9, x22)
    if x == 23:
        return x23
    x24 = paint(I, x23)
    if x == 24:
        return x24
    O = subgrid(x4, x24)
    return O

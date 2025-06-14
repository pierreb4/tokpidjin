def solve_363442ee_one(S, I):
    return paint(I, mapply(compose(lbind(shift, asobject(crop(I, ORIGIN, THREE_BY_THREE))), decrement), f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))))


def solve_363442ee(S, I, x=0):
    x1 = crop(I, ORIGIN, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = asobject(x1)
    if x == 2:
        return x2
    x3 = lbind(shift, x2)
    if x == 3:
        return x3
    x4 = compose(x3, decrement)
    if x == 4:
        return x4
    x5 = identity(p_g)
    if x == 5:
        return x5
    x6 = rbind(get_nth_t, F0)
    if x == 6:
        return x6
    x7 = c_iz_n(S, x5, x6)
    if x == 7:
        return x7
    x8 = f_ofcolor(I, x7)
    if x == 8:
        return x8
    x9 = mapply(x4, x8)
    if x == 9:
        return x9
    O = paint(I, x9)
    return O

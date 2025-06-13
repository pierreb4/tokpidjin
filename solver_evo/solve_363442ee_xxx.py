def solve_363442ee_one(S, I):
    return paint(I, mapply(compose(lbind(shift, asobject(crop(I, ORIGIN, THREE_BY_THREE))), decrement), f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))))


def solve_363442ee(S, I):
    x1 = crop(I, ORIGIN, THREE_BY_THREE)
    x2 = asobject(x1)
    x3 = lbind(shift, x2)
    x4 = compose(x3, decrement)
    x5 = identity(p_g)
    x6 = rbind(get_nth_t, F0)
    x7 = c_iz_n(S, x5, x6)
    x8 = f_ofcolor(I, x7)
    x9 = mapply(x4, x8)
    O = paint(I, x9)
    return O

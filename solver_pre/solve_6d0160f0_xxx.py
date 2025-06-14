def solve_6d0160f0_one(S, I):
    return paint(paint(I, mapply(lbind(shift, recolor_i(ZERO, asindices(crop(I, ORIGIN, THREE_BY_THREE)))), product(insert(EIGHT, insert(FOUR, initset(ZERO))), insert(EIGHT, insert(FOUR, initset(ZERO)))))), shift(toobject(asindices(replace(crop(I, astuple(branch(greater(get_nth_f(get_nth_f(f_ofcolor(I, FOUR), F0), F0), SEVEN), EIGHT, branch(greater(get_nth_f(get_nth_f(f_ofcolor(I, FOUR), F0), F0), THREE), FOUR, ZERO)), branch(greater(get_nth_t(get_nth_f(f_ofcolor(I, FOUR), F0), L1), SEVEN), EIGHT, branch(greater(get_nth_t(get_nth_f(f_ofcolor(I, FOUR), F0), L1), THREE), FOUR, ZERO))), THREE_BY_THREE), FIVE, ZERO)), replace(crop(I, astuple(branch(greater(get_nth_f(get_nth_f(f_ofcolor(I, FOUR), F0), F0), SEVEN), EIGHT, branch(greater(get_nth_f(get_nth_f(f_ofcolor(I, FOUR), F0), F0), THREE), FOUR, ZERO)), branch(greater(get_nth_t(get_nth_f(f_ofcolor(I, FOUR), F0), L1), SEVEN), EIGHT, branch(greater(get_nth_t(get_nth_f(f_ofcolor(I, FOUR), F0), L1), THREE), FOUR, ZERO))), THREE_BY_THREE), FIVE, ZERO)), multiply(get_nth_f(f_ofcolor(replace(crop(I, astuple(branch(greater(get_nth_f(get_nth_f(f_ofcolor(I, FOUR), F0), F0), SEVEN), EIGHT, branch(greater(get_nth_f(get_nth_f(f_ofcolor(I, FOUR), F0), F0), THREE), FOUR, ZERO)), branch(greater(get_nth_t(get_nth_f(f_ofcolor(I, FOUR), F0), L1), SEVEN), EIGHT, branch(greater(get_nth_t(get_nth_f(f_ofcolor(I, FOUR), F0), L1), THREE), FOUR, ZERO))), THREE_BY_THREE), FIVE, ZERO), FOUR), F0), FOUR)))


def solve_6d0160f0(S, I, x=0):
    x1 = crop(I, ORIGIN, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = asindices(x1)
    if x == 2:
        return x2
    x3 = recolor_i(ZERO, x2)
    if x == 3:
        return x3
    x4 = lbind(shift, x3)
    if x == 4:
        return x4
    x5 = initset(ZERO)
    if x == 5:
        return x5
    x6 = insert(FOUR, x5)
    if x == 6:
        return x6
    x7 = insert(EIGHT, x6)
    if x == 7:
        return x7
    x8 = product(x7, x7)
    if x == 8:
        return x8
    x9 = mapply(x4, x8)
    if x == 9:
        return x9
    x10 = paint(I, x9)
    if x == 10:
        return x10
    x11 = f_ofcolor(I, FOUR)
    if x == 11:
        return x11
    x12 = get_nth_f(x11, F0)
    if x == 12:
        return x12
    x13 = get_nth_f(x12, F0)
    if x == 13:
        return x13
    x14 = greater(x13, SEVEN)
    if x == 14:
        return x14
    x15 = greater(x13, THREE)
    if x == 15:
        return x15
    x16 = branch(x15, FOUR, ZERO)
    if x == 16:
        return x16
    x17 = branch(x14, EIGHT, x16)
    if x == 17:
        return x17
    x18 = get_nth_t(x12, L1)
    if x == 18:
        return x18
    x19 = greater(x18, SEVEN)
    if x == 19:
        return x19
    x20 = greater(x18, THREE)
    if x == 20:
        return x20
    x21 = branch(x20, FOUR, ZERO)
    if x == 21:
        return x21
    x22 = branch(x19, EIGHT, x21)
    if x == 22:
        return x22
    x23 = astuple(x17, x22)
    if x == 23:
        return x23
    x24 = crop(I, x23, THREE_BY_THREE)
    if x == 24:
        return x24
    x25 = replace(x24, FIVE, ZERO)
    if x == 25:
        return x25
    x26 = asindices(x25)
    if x == 26:
        return x26
    x27 = toobject(x26, x25)
    if x == 27:
        return x27
    x28 = f_ofcolor(x25, FOUR)
    if x == 28:
        return x28
    x29 = get_nth_f(x28, F0)
    if x == 29:
        return x29
    x30 = multiply(x29, FOUR)
    if x == 30:
        return x30
    x31 = shift(x27, x30)
    if x == 31:
        return x31
    O = paint(x10, x31)
    return O

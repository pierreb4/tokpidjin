def solve_d06dbe63_one(S, I):
    return mir_rot_t(fill(mir_rot_t(fill(I, FIVE, mapply(lbind(shift, shift(combine(connect(ORIGIN, DOWN), connect(ORIGIN, ZERO_BY_TWO)), subtract(center(f_ofcolor(I, EIGHT)), TWO_BY_ZERO))), apply(lbind(multiply, astuple(NEG_TWO, TWO)), interval(ZERO, FIVE, ONE)))), R5), FIVE, shift(shift(mapply(lbind(shift, shift(combine(connect(ORIGIN, DOWN), connect(ORIGIN, ZERO_BY_TWO)), subtract(center(f_ofcolor(I, EIGHT)), TWO_BY_ZERO))), apply(lbind(multiply, astuple(NEG_TWO, TWO)), interval(ZERO, FIVE, ONE))), subtract(center(f_ofcolor(mir_rot_t(fill(I, FIVE, mapply(lbind(shift, shift(combine(connect(ORIGIN, DOWN), connect(ORIGIN, ZERO_BY_TWO)), subtract(center(f_ofcolor(I, EIGHT)), TWO_BY_ZERO))), apply(lbind(multiply, astuple(NEG_TWO, TWO)), interval(ZERO, FIVE, ONE)))), R5), EIGHT)), subtract(center(f_ofcolor(I, EIGHT)), TWO_BY_ZERO))), toivec(NEG_TWO))), R5)


def solve_d06dbe63(S, I, x=0):
    x1 = connect(ORIGIN, DOWN)
    if x == 1:
        return x1
    x2 = connect(ORIGIN, ZERO_BY_TWO)
    if x == 2:
        return x2
    x3 = combine(x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, EIGHT)
    if x == 4:
        return x4
    x5 = center(x4)
    if x == 5:
        return x5
    x6 = subtract(x5, TWO_BY_ZERO)
    if x == 6:
        return x6
    x7 = shift(x3, x6)
    if x == 7:
        return x7
    x8 = lbind(shift, x7)
    if x == 8:
        return x8
    x9 = astuple(NEG_TWO, TWO)
    if x == 9:
        return x9
    x10 = lbind(multiply, x9)
    if x == 10:
        return x10
    x11 = interval(ZERO, FIVE, ONE)
    if x == 11:
        return x11
    x12 = apply(x10, x11)
    if x == 12:
        return x12
    x13 = mapply(x8, x12)
    if x == 13:
        return x13
    x14 = fill(I, FIVE, x13)
    if x == 14:
        return x14
    x15 = mir_rot_t(x14, R5)
    if x == 15:
        return x15
    x16 = f_ofcolor(x15, EIGHT)
    if x == 16:
        return x16
    x17 = center(x16)
    if x == 17:
        return x17
    x18 = subtract(x17, x6)
    if x == 18:
        return x18
    x19 = shift(x13, x18)
    if x == 19:
        return x19
    x20 = toivec(NEG_TWO)
    if x == 20:
        return x20
    x21 = shift(x19, x20)
    if x == 21:
        return x21
    x22 = fill(x15, FIVE, x21)
    if x == 22:
        return x22
    O = mir_rot_t(x22, R5)
    return O

def solve_d06dbe63_one(S, I):
    return mir_rot_t(fill(mir_rot_t(fill(I, FIVE, mapply(lbind(shift, shift(combine(connect(ORIGIN, DOWN), connect(ORIGIN, ZERO_BY_TWO)), subtract(center(f_ofcolor(I, EIGHT)), TWO_BY_ZERO))), apply(lbind(multiply, astuple(NEG_TWO, TWO)), interval(ZERO, FIVE, ONE)))), R5), FIVE, shift(shift(mapply(lbind(shift, shift(combine(connect(ORIGIN, DOWN), connect(ORIGIN, ZERO_BY_TWO)), subtract(center(f_ofcolor(I, EIGHT)), TWO_BY_ZERO))), apply(lbind(multiply, astuple(NEG_TWO, TWO)), interval(ZERO, FIVE, ONE))), subtract(center(f_ofcolor(mir_rot_t(fill(I, FIVE, mapply(lbind(shift, shift(combine(connect(ORIGIN, DOWN), connect(ORIGIN, ZERO_BY_TWO)), subtract(center(f_ofcolor(I, EIGHT)), TWO_BY_ZERO))), apply(lbind(multiply, astuple(NEG_TWO, TWO)), interval(ZERO, FIVE, ONE)))), R5), EIGHT)), subtract(center(f_ofcolor(I, EIGHT)), TWO_BY_ZERO))), toivec(NEG_TWO))), R5)


def solve_d06dbe63(S, I):
    x1 = connect(ORIGIN, DOWN)
    x2 = connect(ORIGIN, ZERO_BY_TWO)
    x3 = combine(x1, x2)
    x4 = f_ofcolor(I, EIGHT)
    x5 = center(x4)
    x6 = subtract(x5, TWO_BY_ZERO)
    x7 = shift(x3, x6)
    x8 = lbind(shift, x7)
    x9 = astuple(NEG_TWO, TWO)
    x10 = lbind(multiply, x9)
    x11 = interval(ZERO, FIVE, ONE)
    x12 = apply(x10, x11)
    x13 = mapply(x8, x12)
    x14 = fill(I, FIVE, x13)
    x15 = mir_rot_t(x14, R5)
    x16 = f_ofcolor(x15, EIGHT)
    x17 = center(x16)
    x18 = subtract(x17, x6)
    x19 = shift(x13, x18)
    x20 = toivec(NEG_TWO)
    x21 = shift(x19, x20)
    x22 = fill(x15, FIVE, x21)
    O = mir_rot_t(x22, R5)
    return O

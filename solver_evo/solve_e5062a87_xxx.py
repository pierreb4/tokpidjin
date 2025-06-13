def solve_e5062a87_one(S, I):
    return paint(I, recolor_o(RED, merge_f(sfilter_f(apply(lbind(shift, normalize(recolor_i(BLACK, f_ofcolor(I, RED)))), occurrences(I, recolor_i(BLACK, f_ofcolor(I, RED)))), chain(flip, rbind(contained, insert(astuple(TWO, SIX), insert(astuple(FIVE, ONE), initset(astuple(ONE, THREE))))), rbind(corner, R0))))))


def solve_e5062a87(S, I):
    x1 = f_ofcolor(I, RED)
    x2 = recolor_i(BLACK, x1)
    x3 = normalize(x2)
    x4 = lbind(shift, x3)
    x5 = occurrences(I, x2)
    x6 = apply(x4, x5)
    x7 = astuple(TWO, SIX)
    x8 = astuple(FIVE, ONE)
    x9 = astuple(ONE, THREE)
    x10 = initset(x9)
    x11 = insert(x8, x10)
    x12 = insert(x7, x11)
    x13 = rbind(contained, x12)
    x14 = rbind(corner, R0)
    x15 = chain(flip, x13, x14)
    x16 = sfilter_f(x6, x15)
    x17 = merge_f(x16)
    x18 = recolor_o(RED, x17)
    O = paint(I, x18)
    return O

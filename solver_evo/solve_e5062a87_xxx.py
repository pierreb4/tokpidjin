def solve_e5062a87_one(S, I):
    return paint(I, recolor_o(RED, merge_f(sfilter_f(apply(lbind(shift, normalize(recolor_i(BLACK, f_ofcolor(I, RED)))), occurrences(I, recolor_i(BLACK, f_ofcolor(I, RED)))), chain(flip, rbind(contained, insert(astuple(TWO, SIX), insert(astuple(FIVE, ONE), initset(astuple(ONE, THREE))))), rbind(corner, R0))))))


def solve_e5062a87(S, I, x=0):
    x1 = f_ofcolor(I, RED)
    if x == 1:
        return x1
    x2 = recolor_i(BLACK, x1)
    if x == 2:
        return x2
    x3 = normalize(x2)
    if x == 3:
        return x3
    x4 = lbind(shift, x3)
    if x == 4:
        return x4
    x5 = occurrences(I, x2)
    if x == 5:
        return x5
    x6 = apply(x4, x5)
    if x == 6:
        return x6
    x7 = astuple(TWO, SIX)
    if x == 7:
        return x7
    x8 = astuple(FIVE, ONE)
    if x == 8:
        return x8
    x9 = astuple(ONE, THREE)
    if x == 9:
        return x9
    x10 = initset(x9)
    if x == 10:
        return x10
    x11 = insert(x8, x10)
    if x == 11:
        return x11
    x12 = insert(x7, x11)
    if x == 12:
        return x12
    x13 = rbind(contained, x12)
    if x == 13:
        return x13
    x14 = rbind(corner, R0)
    if x == 14:
        return x14
    x15 = chain(flip, x13, x14)
    if x == 15:
        return x15
    x16 = sfilter_f(x6, x15)
    if x == 16:
        return x16
    x17 = merge_f(x16)
    if x == 17:
        return x17
    x18 = recolor_o(RED, x17)
    if x == 18:
        return x18
    O = paint(I, x18)
    return O

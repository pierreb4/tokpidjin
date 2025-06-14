def solve_a8d7556c_one(S, I):
    return paint(fill(I, TWO, mapply(lbind(shift, upscale_f(recolor_i(ZERO, initset(ORIGIN)), TWO)), occurrences(I, upscale_f(recolor_i(ZERO, initset(ORIGIN)), TWO)))), branch(equality(index(fill(I, TWO, mapply(lbind(shift, upscale_f(recolor_i(ZERO, initset(ORIGIN)), TWO)), occurrences(I, upscale_f(recolor_i(ZERO, initset(ORIGIN)), TWO)))), astuple(EIGHT, add(SIX, SIX))), TWO), toobject(insert(add(astuple(EIGHT, add(SIX, SIX)), DOWN), initset(astuple(EIGHT, add(SIX, SIX)))), I), toobject(insert(add(astuple(EIGHT, add(SIX, SIX)), DOWN), initset(astuple(EIGHT, add(SIX, SIX)))), fill(I, TWO, mapply(lbind(shift, upscale_f(recolor_i(ZERO, initset(ORIGIN)), TWO)), occurrences(I, upscale_f(recolor_i(ZERO, initset(ORIGIN)), TWO)))))))


def solve_a8d7556c(S, I, x=0):
    x1 = initset(ORIGIN)
    if x == 1:
        return x1
    x2 = recolor_i(ZERO, x1)
    if x == 2:
        return x2
    x3 = upscale_f(x2, TWO)
    if x == 3:
        return x3
    x4 = lbind(shift, x3)
    if x == 4:
        return x4
    x5 = occurrences(I, x3)
    if x == 5:
        return x5
    x6 = mapply(x4, x5)
    if x == 6:
        return x6
    x7 = fill(I, TWO, x6)
    if x == 7:
        return x7
    x8 = add(SIX, SIX)
    if x == 8:
        return x8
    x9 = astuple(EIGHT, x8)
    if x == 9:
        return x9
    x10 = index(x7, x9)
    if x == 10:
        return x10
    x11 = equality(x10, TWO)
    if x == 11:
        return x11
    x12 = add(x9, DOWN)
    if x == 12:
        return x12
    x13 = initset(x9)
    if x == 13:
        return x13
    x14 = insert(x12, x13)
    if x == 14:
        return x14
    x15 = toobject(x14, I)
    if x == 15:
        return x15
    x16 = toobject(x14, x7)
    if x == 16:
        return x16
    x17 = branch(x11, x15, x16)
    if x == 17:
        return x17
    O = paint(x7, x17)
    return O

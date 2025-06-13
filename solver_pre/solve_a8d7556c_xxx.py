def solve_a8d7556c_one(S, I):
    return paint(fill(I, TWO, mapply(lbind(shift, upscale_f(recolor_i(ZERO, initset(ORIGIN)), TWO)), occurrences(I, upscale_f(recolor_i(ZERO, initset(ORIGIN)), TWO)))), branch(equality(index(fill(I, TWO, mapply(lbind(shift, upscale_f(recolor_i(ZERO, initset(ORIGIN)), TWO)), occurrences(I, upscale_f(recolor_i(ZERO, initset(ORIGIN)), TWO)))), astuple(EIGHT, add(SIX, SIX))), TWO), toobject(insert(add(astuple(EIGHT, add(SIX, SIX)), DOWN), initset(astuple(EIGHT, add(SIX, SIX)))), I), toobject(insert(add(astuple(EIGHT, add(SIX, SIX)), DOWN), initset(astuple(EIGHT, add(SIX, SIX)))), fill(I, TWO, mapply(lbind(shift, upscale_f(recolor_i(ZERO, initset(ORIGIN)), TWO)), occurrences(I, upscale_f(recolor_i(ZERO, initset(ORIGIN)), TWO)))))))


def solve_a8d7556c(S, I):
    x1 = initset(ORIGIN)
    x2 = recolor_i(ZERO, x1)
    x3 = upscale_f(x2, TWO)
    x4 = lbind(shift, x3)
    x5 = occurrences(I, x3)
    x6 = mapply(x4, x5)
    x7 = fill(I, TWO, x6)
    x8 = add(SIX, SIX)
    x9 = astuple(EIGHT, x8)
    x10 = index(x7, x9)
    x11 = equality(x10, TWO)
    x12 = add(x9, DOWN)
    x13 = initset(x9)
    x14 = insert(x12, x13)
    x15 = toobject(x14, I)
    x16 = toobject(x14, x7)
    x17 = branch(x11, x15, x16)
    O = paint(x7, x17)
    return O

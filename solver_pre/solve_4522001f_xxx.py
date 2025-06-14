def solve_4522001f_one(S, I):
    return branch(contained(TWO_BY_ZERO, toindices(get_nth_f(o_g(I, R1), F0))), mir_rot_t(paint(canvas(ZERO, astuple(NINE, NINE)), combine(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO), shift(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO), shape_f(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO))))), R6), branch(contained(TWO_BY_TWO, toindices(get_nth_f(o_g(I, R1), F0))), mir_rot_t(paint(canvas(ZERO, astuple(NINE, NINE)), combine(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO), shift(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO), shape_f(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO))))), R5), branch(contained(ZERO_BY_TWO, toindices(get_nth_f(o_g(I, R1), F0))), mir_rot_t(paint(canvas(ZERO, astuple(NINE, NINE)), combine(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO), shift(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO), shape_f(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO))))), R4), paint(canvas(ZERO, astuple(NINE, NINE)), combine(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO), shift(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO), shape_f(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO))))))))


def solve_4522001f(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = toindices(x2)
    if x == 3:
        return x3
    x4 = contained(TWO_BY_ZERO, x3)
    if x == 4:
        return x4
    x5 = astuple(NINE, NINE)
    if x == 5:
        return x5
    x6 = canvas(ZERO, x5)
    if x == 6:
        return x6
    x7 = astuple(THREE, ORIGIN)
    if x == 7:
        return x7
    x8 = initset(x7)
    if x == 8:
        return x8
    x9 = upscale_f(x8, TWO)
    if x == 9:
        return x9
    x10 = upscale_f(x9, TWO)
    if x == 10:
        return x10
    x11 = shape_f(x10)
    if x == 11:
        return x11
    x12 = shift(x10, x11)
    if x == 12:
        return x12
    x13 = combine(x10, x12)
    if x == 13:
        return x13
    x14 = paint(x6, x13)
    if x == 14:
        return x14
    x15 = mir_rot_t(x14, R6)
    if x == 15:
        return x15
    x16 = contained(TWO_BY_TWO, x3)
    if x == 16:
        return x16
    x17 = mir_rot_t(x14, R5)
    if x == 17:
        return x17
    x18 = contained(ZERO_BY_TWO, x3)
    if x == 18:
        return x18
    x19 = mir_rot_t(x14, R4)
    if x == 19:
        return x19
    x20 = branch(x18, x19, x14)
    if x == 20:
        return x20
    x21 = branch(x16, x17, x20)
    if x == 21:
        return x21
    O = branch(x4, x15, x21)
    return O

def solve_4522001f_one(S, I):
    return branch(contained(TWO_BY_ZERO, toindices(get_nth_f(o_g(I, R1), F0))), mir_rot_t(paint(canvas(ZERO, astuple(NINE, NINE)), combine(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO), shift(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO), shape_f(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO))))), R6), branch(contained(TWO_BY_TWO, toindices(get_nth_f(o_g(I, R1), F0))), mir_rot_t(paint(canvas(ZERO, astuple(NINE, NINE)), combine(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO), shift(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO), shape_f(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO))))), R5), branch(contained(ZERO_BY_TWO, toindices(get_nth_f(o_g(I, R1), F0))), mir_rot_t(paint(canvas(ZERO, astuple(NINE, NINE)), combine(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO), shift(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO), shape_f(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO))))), R4), paint(canvas(ZERO, astuple(NINE, NINE)), combine(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO), shift(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO), shape_f(upscale_f(upscale_f(initset(astuple(THREE, ORIGIN)), TWO), TWO))))))))


def solve_4522001f(S, I):
    x1 = o_g(I, R1)
    x2 = get_nth_f(x1, F0)
    x3 = toindices(x2)
    x4 = contained(TWO_BY_ZERO, x3)
    x5 = astuple(NINE, NINE)
    x6 = canvas(ZERO, x5)
    x7 = astuple(THREE, ORIGIN)
    x8 = initset(x7)
    x9 = upscale_f(x8, TWO)
    x10 = upscale_f(x9, TWO)
    x11 = shape_f(x10)
    x12 = shift(x10, x11)
    x13 = combine(x10, x12)
    x14 = paint(x6, x13)
    x15 = mir_rot_t(x14, R6)
    x16 = contained(TWO_BY_TWO, x3)
    x17 = mir_rot_t(x14, R5)
    x18 = contained(ZERO_BY_TWO, x3)
    x19 = mir_rot_t(x14, R4)
    x20 = branch(x18, x19, x14)
    x21 = branch(x16, x17, x20)
    O = branch(x4, x15, x21)
    return O

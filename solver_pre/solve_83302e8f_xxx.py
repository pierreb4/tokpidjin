def solve_83302e8f_one(S, I):
    return paint(paint(I, recolor_o(THREE, merge_f(sfilter_f(colorfilter(o_g(I, R4), ZERO), square_f)))), recolor_o(FOUR, merge_f(difference(colorfilter(o_g(I, R4), ZERO), sfilter_f(colorfilter(o_g(I, R4), ZERO), square_f)))))


def solve_83302e8f(S, I):
    x1 = o_g(I, R4)
    x2 = colorfilter(x1, ZERO)
    x3 = sfilter_f(x2, square_f)
    x4 = merge_f(x3)
    x5 = recolor_o(THREE, x4)
    x6 = paint(I, x5)
    x7 = difference(x2, x3)
    x8 = merge_f(x7)
    x9 = recolor_o(FOUR, x8)
    O = paint(x6, x9)
    return O

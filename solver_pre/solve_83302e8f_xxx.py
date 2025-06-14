def solve_83302e8f_one(S, I):
    return paint(paint(I, recolor_o(THREE, merge_f(sfilter_f(colorfilter(o_g(I, R4), ZERO), square_f)))), recolor_o(FOUR, merge_f(difference(colorfilter(o_g(I, R4), ZERO), sfilter_f(colorfilter(o_g(I, R4), ZERO), square_f)))))


def solve_83302e8f(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = sfilter_f(x2, square_f)
    if x == 3:
        return x3
    x4 = merge_f(x3)
    if x == 4:
        return x4
    x5 = recolor_o(THREE, x4)
    if x == 5:
        return x5
    x6 = paint(I, x5)
    if x == 6:
        return x6
    x7 = difference(x2, x3)
    if x == 7:
        return x7
    x8 = merge_f(x7)
    if x == 8:
        return x8
    x9 = recolor_o(FOUR, x8)
    if x == 9:
        return x9
    O = paint(x6, x9)
    return O

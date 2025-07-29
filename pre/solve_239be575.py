def solve_239be575_one(S, I):
    return canvas(branch(greater(size_f(sfilter_f(o_g(I, R3), compose(lbind(contained, TWO), palette_f))), ONE), ZERO, EIGHT), UNITY)


def solve_239be575(S, I):
    x1 = o_g(I, R3)
    x2 = lbind(contained, TWO)
    x3 = compose(x2, palette_f)
    x4 = sfilter_f(x1, x3)
    x5 = size_f(x4)
    x6 = greater(x5, ONE)
    x7 = branch(x6, ZERO, EIGHT)
    O = canvas(x7, UNITY)
    return O

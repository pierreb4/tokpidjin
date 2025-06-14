def solve_239be575_one(S, I):
    return canvas(branch(greater(size_f(sfilter_f(o_g(I, R3), compose(lbind(contained, TWO), palette_f))), ONE), ZERO, EIGHT), UNITY)


def solve_239be575(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = lbind(contained, TWO)
    if x == 2:
        return x2
    x3 = compose(x2, palette_f)
    if x == 3:
        return x3
    x4 = sfilter_f(x1, x3)
    if x == 4:
        return x4
    x5 = size_f(x4)
    if x == 5:
        return x5
    x6 = greater(x5, ONE)
    if x == 6:
        return x6
    x7 = branch(x6, ZERO, EIGHT)
    if x == 7:
        return x7
    O = canvas(x7, UNITY)
    return O

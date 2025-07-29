def solve_67385a82_one(S, I):
    return fill(I, EIGHT, merge_f(difference(colorfilter(o_g(I, R4), THREE), sizefilter(colorfilter(o_g(I, R4), THREE), ONE))))


def solve_67385a82(S, I):
    x1 = o_g(I, R4)
    x2 = colorfilter(x1, THREE)
    x3 = sizefilter(x2, ONE)
    x4 = difference(x2, x3)
    x5 = merge_f(x4)
    O = fill(I, EIGHT, x5)
    return O

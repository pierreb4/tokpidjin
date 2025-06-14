def solve_67385a82_one(S, I):
    return fill(I, EIGHT, merge_f(difference(colorfilter(o_g(I, R4), THREE), sizefilter(colorfilter(o_g(I, R4), THREE), ONE))))


def solve_67385a82(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, THREE)
    if x == 2:
        return x2
    x3 = sizefilter(x2, ONE)
    if x == 3:
        return x3
    x4 = difference(x2, x3)
    if x == 4:
        return x4
    x5 = merge_f(x4)
    if x == 5:
        return x5
    O = fill(I, EIGHT, x5)
    return O

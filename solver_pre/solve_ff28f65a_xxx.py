def solve_ff28f65a_one(S, I):
    return merge_t(hsplit(fill(canvas(ZERO, astuple(ONE, NINE)), ONE, apply(tojvec, interval(ZERO, double(size_f(o_g(I, R5))), TWO))), THREE))


def solve_ff28f65a(S, I, x=0):
    x1 = astuple(ONE, NINE)
    if x == 1:
        return x1
    x2 = canvas(ZERO, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = size_f(x3)
    if x == 4:
        return x4
    x5 = double(x4)
    if x == 5:
        return x5
    x6 = interval(ZERO, x5, TWO)
    if x == 6:
        return x6
    x7 = apply(tojvec, x6)
    if x == 7:
        return x7
    x8 = fill(x2, ONE, x7)
    if x == 8:
        return x8
    x9 = hsplit(x8, THREE)
    if x == 9:
        return x9
    O = merge_t(x9)
    return O

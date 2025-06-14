def solve_8eb1be9a_one(S, I):
    return paint(I, mapply(lbind(shift, get_nth_f(o_g(I, R7), F0)), apply(toivec, apply(rbind(multiply, height_f(get_nth_f(o_g(I, R7), F0))), interval(NEG_TWO, FOUR, ONE)))))


def solve_8eb1be9a(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = lbind(shift, x2)
    if x == 3:
        return x3
    x4 = height_f(x2)
    if x == 4:
        return x4
    x5 = rbind(multiply, x4)
    if x == 5:
        return x5
    x6 = interval(NEG_TWO, FOUR, ONE)
    if x == 6:
        return x6
    x7 = apply(x5, x6)
    if x == 7:
        return x7
    x8 = apply(toivec, x7)
    if x == 8:
        return x8
    x9 = mapply(x3, x8)
    if x == 9:
        return x9
    O = paint(I, x9)
    return O

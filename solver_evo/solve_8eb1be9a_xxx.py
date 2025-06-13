def solve_8eb1be9a_one(S, I):
    return paint(I, mapply(lbind(shift, get_nth_f(o_g(I, R7), F0)), apply(toivec, apply(rbind(multiply, height_f(get_nth_f(o_g(I, R7), F0))), interval(NEG_TWO, FOUR, ONE)))))


def solve_8eb1be9a(S, I):
    x1 = o_g(I, R7)
    x2 = get_nth_f(x1, F0)
    x3 = lbind(shift, x2)
    x4 = height_f(x2)
    x5 = rbind(multiply, x4)
    x6 = interval(NEG_TWO, FOUR, ONE)
    x7 = apply(x5, x6)
    x8 = apply(toivec, x7)
    x9 = mapply(x3, x8)
    O = paint(I, x9)
    return O

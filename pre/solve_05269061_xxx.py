def solve_05269061_one(S, I):
    return paint(paint(paint(I, mapply(lbind(shift, merge_f(o_g(I, R7))), apply(rbind(multiply, THREE), mapply(neighbors, neighbors(ORIGIN))))), shift(mapply(lbind(shift, merge_f(o_g(I, R7))), apply(rbind(multiply, THREE), mapply(neighbors, neighbors(ORIGIN)))), UP_RIGHT)), shift(mapply(lbind(shift, merge_f(o_g(I, R7))), apply(rbind(multiply, THREE), mapply(neighbors, neighbors(ORIGIN)))), DOWN_LEFT))


def solve_05269061(S, I):
    x1 = o_g(I, R7)
    x2 = merge_f(x1)
    x3 = lbind(shift, x2)
    x4 = rbind(multiply, THREE)
    x5 = neighbors(ORIGIN)
    x6 = mapply(neighbors, x5)
    x7 = apply(x4, x6)
    x8 = mapply(x3, x7)
    x9 = paint(I, x8)
    x10 = shift(x8, UP_RIGHT)
    x11 = paint(x9, x10)
    x12 = shift(x8, DOWN_LEFT)
    O = paint(x11, x12)
    return O

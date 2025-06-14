def solve_05269061_one(S, I):
    return paint(paint(paint(I, mapply(lbind(shift, merge_f(o_g(I, R7))), apply(rbind(multiply, THREE), mapply(neighbors, neighbors(ORIGIN))))), shift(mapply(lbind(shift, merge_f(o_g(I, R7))), apply(rbind(multiply, THREE), mapply(neighbors, neighbors(ORIGIN)))), UP_RIGHT)), shift(mapply(lbind(shift, merge_f(o_g(I, R7))), apply(rbind(multiply, THREE), mapply(neighbors, neighbors(ORIGIN)))), DOWN_LEFT))


def solve_05269061(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = lbind(shift, x2)
    if x == 3:
        return x3
    x4 = rbind(multiply, THREE)
    if x == 4:
        return x4
    x5 = neighbors(ORIGIN)
    if x == 5:
        return x5
    x6 = mapply(neighbors, x5)
    if x == 6:
        return x6
    x7 = apply(x4, x6)
    if x == 7:
        return x7
    x8 = mapply(x3, x7)
    if x == 8:
        return x8
    x9 = paint(I, x8)
    if x == 9:
        return x9
    x10 = shift(x8, UP_RIGHT)
    if x == 10:
        return x10
    x11 = paint(x9, x10)
    if x == 11:
        return x11
    x12 = shift(x8, DOWN_LEFT)
    if x == 12:
        return x12
    O = paint(x11, x12)
    return O

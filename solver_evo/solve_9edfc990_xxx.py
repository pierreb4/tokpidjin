def solve_9edfc990_one(S, I):
    return paint(I, recolor_o(BLUE, mfilter_f(colorfilter(o_g(I, R4), BLACK), rbind(adjacent, f_ofcolor(I, BLUE)))))


def solve_9edfc990(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, BLACK)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, BLUE)
    if x == 3:
        return x3
    x4 = rbind(adjacent, x3)
    if x == 4:
        return x4
    x5 = mfilter_f(x2, x4)
    if x == 5:
        return x5
    x6 = recolor_o(BLUE, x5)
    if x == 6:
        return x6
    O = paint(I, x6)
    return O

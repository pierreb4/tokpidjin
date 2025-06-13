def solve_d9f24cd1_one(S, I):
    return fill(fill(underfill(I, RED, mfilter_f(prapply(connect, f_ofcolor(I, RED), f_ofcolor(I, GRAY)), vline_i)), RED, mapply(rbind(shoot, UP), shift(apply(rbind(corner, R1), sfilter_f(o_g(underfill(I, RED, mfilter_f(prapply(connect, f_ofcolor(I, RED), f_ofcolor(I, GRAY)), vline_i)), R1), matcher(numcolors_f, RED))), UNITY))), RED, mapply(vfrontier, mapply(toindices, colorfilter(difference(o_g(underfill(I, RED, mfilter_f(prapply(connect, f_ofcolor(I, RED), f_ofcolor(I, GRAY)), vline_i)), R1), sfilter_f(o_g(underfill(I, RED, mfilter_f(prapply(connect, f_ofcolor(I, RED), f_ofcolor(I, GRAY)), vline_i)), R1), matcher(numcolors_f, RED))), RED))))


def solve_d9f24cd1(S, I):
    x1 = f_ofcolor(I, RED)
    x2 = f_ofcolor(I, GRAY)
    x3 = prapply(connect, x1, x2)
    x4 = mfilter_f(x3, vline_i)
    x5 = underfill(I, RED, x4)
    x6 = rbind(shoot, UP)
    x7 = rbind(corner, R1)
    x8 = o_g(x5, R1)
    x9 = matcher(numcolors_f, RED)
    x10 = sfilter_f(x8, x9)
    x11 = apply(x7, x10)
    x12 = shift(x11, UNITY)
    x13 = mapply(x6, x12)
    x14 = fill(x5, RED, x13)
    x15 = difference(x8, x10)
    x16 = colorfilter(x15, RED)
    x17 = mapply(toindices, x16)
    x18 = mapply(vfrontier, x17)
    O = fill(x14, RED, x18)
    return O

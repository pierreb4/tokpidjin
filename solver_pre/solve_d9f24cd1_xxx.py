def solve_d9f24cd1_one(S, I):
    return fill(fill(underfill(I, TWO, mfilter_f(prapply(connect, f_ofcolor(I, TWO), f_ofcolor(I, FIVE)), vline_i)), TWO, mapply(rbind(shoot, UP), shift(apply(rbind(corner, R1), sfilter_f(o_g(underfill(I, TWO, mfilter_f(prapply(connect, f_ofcolor(I, TWO), f_ofcolor(I, FIVE)), vline_i)), R1), matcher(numcolors_f, TWO))), UNITY))), TWO, mapply(vfrontier, mapply(toindices, colorfilter(difference(o_g(underfill(I, TWO, mfilter_f(prapply(connect, f_ofcolor(I, TWO), f_ofcolor(I, FIVE)), vline_i)), R1), sfilter_f(o_g(underfill(I, TWO, mfilter_f(prapply(connect, f_ofcolor(I, TWO), f_ofcolor(I, FIVE)), vline_i)), R1), matcher(numcolors_f, TWO))), TWO))))


def solve_d9f24cd1(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, FIVE)
    if x == 2:
        return x2
    x3 = prapply(connect, x1, x2)
    if x == 3:
        return x3
    x4 = mfilter_f(x3, vline_i)
    if x == 4:
        return x4
    x5 = underfill(I, TWO, x4)
    if x == 5:
        return x5
    x6 = rbind(shoot, UP)
    if x == 6:
        return x6
    x7 = rbind(corner, R1)
    if x == 7:
        return x7
    x8 = o_g(x5, R1)
    if x == 8:
        return x8
    x9 = matcher(numcolors_f, TWO)
    if x == 9:
        return x9
    x10 = sfilter_f(x8, x9)
    if x == 10:
        return x10
    x11 = apply(x7, x10)
    if x == 11:
        return x11
    x12 = shift(x11, UNITY)
    if x == 12:
        return x12
    x13 = mapply(x6, x12)
    if x == 13:
        return x13
    x14 = fill(x5, TWO, x13)
    if x == 14:
        return x14
    x15 = difference(x8, x10)
    if x == 15:
        return x15
    x16 = colorfilter(x15, TWO)
    if x == 16:
        return x16
    x17 = mapply(toindices, x16)
    if x == 17:
        return x17
    x18 = mapply(vfrontier, x17)
    if x == 18:
        return x18
    O = fill(x14, TWO, x18)
    return O

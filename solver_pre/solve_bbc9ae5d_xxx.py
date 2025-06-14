def solve_bbc9ae5d_one(S, I):
    return fill(vupscale(I, halve(width_t(I))), other_f(palette_t(I), ZERO), mapply(rbind(shoot, UNITY), f_ofcolor(vupscale(I, halve(width_t(I))), other_f(palette_t(I), ZERO))))


def solve_bbc9ae5d(S, I, x=0):
    x1 = width_t(I)
    if x == 1:
        return x1
    x2 = halve(x1)
    if x == 2:
        return x2
    x3 = vupscale(I, x2)
    if x == 3:
        return x3
    x4 = palette_t(I)
    if x == 4:
        return x4
    x5 = other_f(x4, ZERO)
    if x == 5:
        return x5
    x6 = rbind(shoot, UNITY)
    if x == 6:
        return x6
    x7 = f_ofcolor(x3, x5)
    if x == 7:
        return x7
    x8 = mapply(x6, x7)
    if x == 8:
        return x8
    O = fill(x3, x5, x8)
    return O

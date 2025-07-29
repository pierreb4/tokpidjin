def solve_bbc9ae5d_one(S, I):
    return fill(vupscale(I, halve(width_t(I))), other_f(palette_t(I), ZERO), mapply(rbind(shoot, UNITY), f_ofcolor(vupscale(I, halve(width_t(I))), other_f(palette_t(I), ZERO))))


def solve_bbc9ae5d(S, I):
    x1 = width_t(I)
    x2 = halve(x1)
    x3 = vupscale(I, x2)
    x4 = palette_t(I)
    x5 = other_f(x4, ZERO)
    x6 = rbind(shoot, UNITY)
    x7 = f_ofcolor(x3, x5)
    x8 = mapply(x6, x7)
    O = fill(x3, x5, x8)
    return O

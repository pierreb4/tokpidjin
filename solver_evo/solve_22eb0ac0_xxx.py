def solve_22eb0ac0_one(S, I):
    return paint(I, mfilter_f(apply(fork(recolor_i, color, backdrop), fgpartition(I)), hline_o))


def solve_22eb0ac0(S, I, x=0):
    x1 = fork(recolor_i, color, backdrop)
    if x == 1:
        return x1
    x2 = fgpartition(I)
    if x == 2:
        return x2
    x3 = apply(x1, x2)
    if x == 3:
        return x3
    x4 = mfilter_f(x3, hline_o)
    if x == 4:
        return x4
    O = paint(I, x4)
    return O

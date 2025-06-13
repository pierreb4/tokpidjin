def solve_22eb0ac0_one(S, I):
    return paint(I, mfilter_f(apply(fork(recolor_i, color, backdrop), fgpartition(I)), hline_o))


def solve_22eb0ac0(S, I):
    x1 = fork(recolor_i, color, backdrop)
    x2 = fgpartition(I)
    x3 = apply(x1, x2)
    x4 = mfilter_f(x3, hline_o)
    O = paint(I, x4)
    return O

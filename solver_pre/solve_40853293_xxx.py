def solve_40853293_one(S, I):
    return paint(paint(I, mfilter(apply(fork(recolor_i, color, backdrop), partition(I)), hline_i)), mfilter(apply(fork(recolor_i, color, backdrop), partition(I)), vline_i))


def solve_40853293(S, I):
    x1 = fork(recolor_i, color, backdrop)
    x2 = partition(I)
    x3 = apply(x1, x2)
    x4 = mfilter(x3, hline_i)
    x5 = paint(I, x4)
    x6 = mfilter(x3, vline_i)
    O = paint(x5, x6)
    return O

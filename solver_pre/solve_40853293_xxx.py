def solve_40853293_one(S, I):
    return paint(paint(I, mfilter(apply(fork(recolor_i, color, backdrop), partition(I)), hline_i)), mfilter(apply(fork(recolor_i, color, backdrop), partition(I)), vline_i))


def solve_40853293(S, I, x=0):
    x1 = fork(recolor_i, color, backdrop)
    if x == 1:
        return x1
    x2 = partition(I)
    if x == 2:
        return x2
    x3 = apply(x1, x2)
    if x == 3:
        return x3
    x4 = mfilter(x3, hline_i)
    if x == 4:
        return x4
    x5 = paint(I, x4)
    if x == 5:
        return x5
    x6 = mfilter(x3, vline_i)
    if x == 6:
        return x6
    O = paint(x5, x6)
    return O

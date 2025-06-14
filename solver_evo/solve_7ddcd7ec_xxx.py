def solve_7ddcd7ec_one(S, I):
    return fill(I, color(get_nth_f(difference(o_g(I, R5), sizefilter(o_g(I, R5), ONE)), F0)), mapply(fork(shoot, center, lbind(position, get_nth_f(difference(o_g(I, R5), sizefilter(o_g(I, R5), ONE)), F0))), sizefilter(o_g(I, R5), ONE)))


def solve_7ddcd7ec(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = difference(x1, x2)
    if x == 3:
        return x3
    x4 = get_nth_f(x3, F0)
    if x == 4:
        return x4
    x5 = color(x4)
    if x == 5:
        return x5
    x6 = lbind(position, x4)
    if x == 6:
        return x6
    x7 = fork(shoot, center, x6)
    if x == 7:
        return x7
    x8 = mapply(x7, x2)
    if x == 8:
        return x8
    O = fill(I, x5, x8)
    return O

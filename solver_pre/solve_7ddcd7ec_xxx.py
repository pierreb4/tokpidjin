def solve_7ddcd7ec_one(S, I):
    return fill(I, color(get_nth_f(difference(o_g(I, R5), sizefilter(o_g(I, R5), ONE)), F0)), mapply(fork(shoot, center, lbind(position, get_nth_f(difference(o_g(I, R5), sizefilter(o_g(I, R5), ONE)), F0))), sizefilter(o_g(I, R5), ONE)))


def solve_7ddcd7ec(S, I):
    x1 = o_g(I, R5)
    x2 = sizefilter(x1, ONE)
    x3 = difference(x1, x2)
    x4 = get_nth_f(x3, F0)
    x5 = color(x4)
    x6 = lbind(position, x4)
    x7 = fork(shoot, center, x6)
    x8 = mapply(x7, x2)
    O = fill(I, x5, x8)
    return O

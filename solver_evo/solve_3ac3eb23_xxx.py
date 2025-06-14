def solve_3ac3eb23_one(S, I):
    return vconcat(get_nth_f(vsplit(paint(I, mapply(fork(recolor_i, color, chain(ineighbors, rbind(get_nth_f, L1), rbind(get_nth_f, F0))), o_g(I, R5))), THREE), F0), vconcat(get_nth_f(vsplit(paint(I, mapply(fork(recolor_i, color, chain(ineighbors, rbind(get_nth_f, L1), rbind(get_nth_f, F0))), o_g(I, R5))), THREE), F0), get_nth_f(vsplit(paint(I, mapply(fork(recolor_i, color, chain(ineighbors, rbind(get_nth_f, L1), rbind(get_nth_f, F0))), o_g(I, R5))), THREE), F0)))


def solve_3ac3eb23(S, I, x=0):
    x1 = rbind(get_nth_f, L1)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, F0)
    if x == 2:
        return x2
    x3 = chain(ineighbors, x1, x2)
    if x == 3:
        return x3
    x4 = fork(recolor_i, color, x3)
    if x == 4:
        return x4
    x5 = o_g(I, R5)
    if x == 5:
        return x5
    x6 = mapply(x4, x5)
    if x == 6:
        return x6
    x7 = paint(I, x6)
    if x == 7:
        return x7
    x8 = vsplit(x7, THREE)
    if x == 8:
        return x8
    x9 = get_nth_f(x8, F0)
    if x == 9:
        return x9
    x10 = vconcat(x9, x9)
    if x == 10:
        return x10
    O = vconcat(x9, x10)
    return O

def solve_3ac3eb23_one(S, I):
    return vconcat(get_nth_f(vsplit(paint(I, mapply(fork(recolor_i, color, chain(ineighbors, rbind(get_nth_f, L1), rbind(get_nth_f, F0))), o_g(I, R5))), THREE), F0), vconcat(get_nth_f(vsplit(paint(I, mapply(fork(recolor_i, color, chain(ineighbors, rbind(get_nth_f, L1), rbind(get_nth_f, F0))), o_g(I, R5))), THREE), F0), get_nth_f(vsplit(paint(I, mapply(fork(recolor_i, color, chain(ineighbors, rbind(get_nth_f, L1), rbind(get_nth_f, F0))), o_g(I, R5))), THREE), F0)))


def solve_3ac3eb23(S, I):
    x1 = rbind(get_nth_f, L1)
    x2 = rbind(get_nth_f, F0)
    x3 = chain(ineighbors, x1, x2)
    x4 = fork(recolor_i, color, x3)
    x5 = o_g(I, R5)
    x6 = mapply(x4, x5)
    x7 = paint(I, x6)
    x8 = vsplit(x7, THREE)
    x9 = get_nth_f(x8, F0)
    x10 = vconcat(x9, x9)
    O = vconcat(x9, x10)
    return O

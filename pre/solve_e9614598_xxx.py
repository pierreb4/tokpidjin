def solve_e9614598_one(S, I):
    return fill(I, THREE, insert(halve(fork(add, rbind(get_nth_f, F0), rbind(get_nth_f, L1))(f_ofcolor(I, ONE))), dneighbors(halve(fork(add, rbind(get_nth_f, F0), rbind(get_nth_f, L1))(f_ofcolor(I, ONE))))))


def solve_e9614598(S, I):
    x1 = rbind(get_nth_f, F0)
    x2 = rbind(get_nth_f, L1)
    x3 = fork(add, x1, x2)
    x4 = f_ofcolor(I, ONE)
    x5 = x3(x4)
    x6 = halve(x5)
    x7 = dneighbors(x6)
    x8 = insert(x6, x7)
    O = fill(I, THREE, x8)
    return O

def solve_e9614598_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), insert(halve(fork(add, rbind(get_nth_f, F0), rbind(get_nth_f, L1))(f_ofcolor(I, BLUE))), dneighbors(halve(fork(add, rbind(get_nth_f, F0), rbind(get_nth_f, L1))(f_ofcolor(I, BLUE))))))


def solve_e9614598(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = rbind(get_nth_f, F0)
    x5 = rbind(get_nth_f, L1)
    x6 = fork(add, x4, x5)
    x7 = f_ofcolor(I, BLUE)
    x8 = x6(x7)
    x9 = halve(x8)
    x10 = dneighbors(x9)
    x11 = insert(x9, x10)
    O = fill(I, x3, x11)
    return O

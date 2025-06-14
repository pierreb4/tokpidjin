def solve_e9614598_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), insert(halve(fork(add, rbind(get_nth_f, F0), rbind(get_nth_f, L1))(f_ofcolor(I, BLUE))), dneighbors(halve(fork(add, rbind(get_nth_f, F0), rbind(get_nth_f, L1))(f_ofcolor(I, BLUE))))))


def solve_e9614598(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = rbind(get_nth_f, F0)
    if x == 4:
        return x4
    x5 = rbind(get_nth_f, L1)
    if x == 5:
        return x5
    x6 = fork(add, x4, x5)
    if x == 6:
        return x6
    x7 = f_ofcolor(I, BLUE)
    if x == 7:
        return x7
    x8 = x6(x7)
    if x == 8:
        return x8
    x9 = halve(x8)
    if x == 9:
        return x9
    x10 = dneighbors(x9)
    if x == 10:
        return x10
    x11 = insert(x9, x10)
    if x == 11:
        return x11
    O = fill(I, x3, x11)
    return O

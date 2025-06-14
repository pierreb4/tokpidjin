def solve_e9614598_one(S, I):
    return fill(I, THREE, insert(halve(fork(add, rbind(get_nth_f, F0), rbind(get_nth_f, L1))(f_ofcolor(I, ONE))), dneighbors(halve(fork(add, rbind(get_nth_f, F0), rbind(get_nth_f, L1))(f_ofcolor(I, ONE))))))


def solve_e9614598(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, L1)
    if x == 2:
        return x2
    x3 = fork(add, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, ONE)
    if x == 4:
        return x4
    x5 = x3(x4)
    if x == 5:
        return x5
    x6 = halve(x5)
    if x == 6:
        return x6
    x7 = dneighbors(x6)
    if x == 7:
        return x7
    x8 = insert(x6, x7)
    if x == 8:
        return x8
    O = fill(I, THREE, x8)
    return O

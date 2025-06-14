def solve_ce9e57f2_one(S, I):
    return switch(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(fork(connect, rbind(corner, R0), centerofmass), o_g(I, R5))), EIGHT, TWO)


def solve_ce9e57f2(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = rbind(corner, R0)
    if x == 4:
        return x4
    x5 = fork(connect, x4, centerofmass)
    if x == 5:
        return x5
    x6 = o_g(I, R5)
    if x == 6:
        return x6
    x7 = mapply(x5, x6)
    if x == 7:
        return x7
    x8 = fill(I, x3, x7)
    if x == 8:
        return x8
    O = switch(x8, EIGHT, TWO)
    return O

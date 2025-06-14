def solve_ce9e57f2_one(S, I):
    return switch(fill(I, EIGHT, mapply(fork(connect, rbind(corner, R0), centerofmass), o_g(I, R5))), EIGHT, TWO)


def solve_ce9e57f2(S, I, x=0):
    x1 = rbind(corner, R0)
    if x == 1:
        return x1
    x2 = fork(connect, x1, centerofmass)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = mapply(x2, x3)
    if x == 4:
        return x4
    x5 = fill(I, EIGHT, x4)
    if x == 5:
        return x5
    O = switch(x5, EIGHT, TWO)
    return O

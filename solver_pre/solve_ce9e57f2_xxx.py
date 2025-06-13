def solve_ce9e57f2_one(S, I):
    return switch(fill(I, EIGHT, mapply(fork(connect, rbind(corner, R0), centerofmass), o_g(I, R5))), EIGHT, TWO)


def solve_ce9e57f2(S, I):
    x1 = rbind(corner, R0)
    x2 = fork(connect, x1, centerofmass)
    x3 = o_g(I, R5)
    x4 = mapply(x2, x3)
    x5 = fill(I, EIGHT, x4)
    O = switch(x5, EIGHT, TWO)
    return O

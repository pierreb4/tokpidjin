def solve_137eaa0f_one(S, I):
    return paint(canvas(BLACK, THREE_BY_THREE), shift(mapply(fork(shift, identity, chain(invert, center, rbind(sfilter, matcher(rbind(get_nth_f, F0), GRAY)))), o_g(I, R3)), UNITY))


def solve_137eaa0f(S, I):
    x1 = canvas(BLACK, THREE_BY_THREE)
    x2 = rbind(get_nth_f, F0)
    x3 = matcher(x2, GRAY)
    x4 = rbind(sfilter, x3)
    x5 = chain(invert, center, x4)
    x6 = fork(shift, identity, x5)
    x7 = o_g(I, R3)
    x8 = mapply(x6, x7)
    x9 = shift(x8, UNITY)
    O = paint(x1, x9)
    return O

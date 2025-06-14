def solve_137eaa0f_one(S, I):
    return paint(canvas(BLACK, THREE_BY_THREE), shift(mapply(fork(shift, identity, chain(invert, center, rbind(sfilter, matcher(rbind(get_nth_f, F0), GRAY)))), o_g(I, R3)), UNITY))


def solve_137eaa0f(S, I, x=0):
    x1 = canvas(BLACK, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, F0)
    if x == 2:
        return x2
    x3 = matcher(x2, GRAY)
    if x == 3:
        return x3
    x4 = rbind(sfilter, x3)
    if x == 4:
        return x4
    x5 = chain(invert, center, x4)
    if x == 5:
        return x5
    x6 = fork(shift, identity, x5)
    if x == 6:
        return x6
    x7 = o_g(I, R3)
    if x == 7:
        return x7
    x8 = mapply(x6, x7)
    if x == 8:
        return x8
    x9 = shift(x8, UNITY)
    if x == 9:
        return x9
    O = paint(x1, x9)
    return O

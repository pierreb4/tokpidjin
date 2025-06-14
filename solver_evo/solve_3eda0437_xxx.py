def solve_3eda0437_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), get_arg_rank_f(mapply(chain(fork(apply, lbind(lbind, shift), lbind(occurrences, I)), asobject, lbind(canvas, BLACK)), prapply(astuple, interval(TWO, TEN, ONE), interval(TWO, TEN, ONE))), size, F0))


def solve_3eda0437(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = lbind(lbind, shift)
    if x == 4:
        return x4
    x5 = lbind(occurrences, I)
    if x == 5:
        return x5
    x6 = fork(apply, x4, x5)
    if x == 6:
        return x6
    x7 = lbind(canvas, BLACK)
    if x == 7:
        return x7
    x8 = chain(x6, asobject, x7)
    if x == 8:
        return x8
    x9 = interval(TWO, TEN, ONE)
    if x == 9:
        return x9
    x10 = prapply(astuple, x9, x9)
    if x == 10:
        return x10
    x11 = mapply(x8, x10)
    if x == 11:
        return x11
    x12 = get_arg_rank_f(x11, size, F0)
    if x == 12:
        return x12
    O = fill(I, x3, x12)
    return O

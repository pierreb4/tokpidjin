def solve_3eda0437_one(S, I):
    return fill(I, SIX, get_arg_rank_f(mapply(chain(fork(apply, lbind(lbind, shift), lbind(occurrences, I)), asobject, lbind(canvas, ZERO)), prapply(astuple, interval(TWO, TEN, ONE), interval(TWO, TEN, ONE))), size, F0))


def solve_3eda0437(S, I, x=0):
    x1 = lbind(lbind, shift)
    if x == 1:
        return x1
    x2 = lbind(occurrences, I)
    if x == 2:
        return x2
    x3 = fork(apply, x1, x2)
    if x == 3:
        return x3
    x4 = lbind(canvas, ZERO)
    if x == 4:
        return x4
    x5 = chain(x3, asobject, x4)
    if x == 5:
        return x5
    x6 = interval(TWO, TEN, ONE)
    if x == 6:
        return x6
    x7 = prapply(astuple, x6, x6)
    if x == 7:
        return x7
    x8 = mapply(x5, x7)
    if x == 8:
        return x8
    x9 = get_arg_rank_f(x8, size, F0)
    if x == 9:
        return x9
    O = fill(I, SIX, x9)
    return O

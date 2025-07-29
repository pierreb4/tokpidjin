def solve_3eda0437_one(S, I):
    return fill(I, SIX, get_arg_rank_f(mapply(chain(fork(apply, lbind(lbind, shift), lbind(occurrences, I)), asobject, lbind(canvas, ZERO)), prapply(astuple, interval(TWO, TEN, ONE), interval(TWO, TEN, ONE))), size, F0))


def solve_3eda0437(S, I):
    x1 = lbind(lbind, shift)
    x2 = lbind(occurrences, I)
    x3 = fork(apply, x1, x2)
    x4 = lbind(canvas, ZERO)
    x5 = chain(x3, asobject, x4)
    x6 = interval(TWO, TEN, ONE)
    x7 = prapply(astuple, x6, x6)
    x8 = mapply(x5, x7)
    x9 = get_arg_rank_f(x8, size, F0)
    O = fill(I, SIX, x9)
    return O

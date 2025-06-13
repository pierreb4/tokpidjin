def solve_3eda0437_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), get_arg_rank_f(mapply(chain(fork(apply, lbind(lbind, shift), lbind(occurrences, I)), asobject, lbind(canvas, BLACK)), prapply(astuple, interval(TWO, TEN, ONE), interval(TWO, TEN, ONE))), size, F0))


def solve_3eda0437(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = lbind(lbind, shift)
    x5 = lbind(occurrences, I)
    x6 = fork(apply, x4, x5)
    x7 = lbind(canvas, BLACK)
    x8 = chain(x6, asobject, x7)
    x9 = interval(TWO, TEN, ONE)
    x10 = prapply(astuple, x9, x9)
    x11 = mapply(x8, x10)
    x12 = get_arg_rank_f(x11, size, F0)
    O = fill(I, x3, x12)
    return O

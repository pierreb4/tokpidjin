def solve_5bd6f4ac_one(S, I):
    return crop(I, tojvec(SIX), THREE_BY_THREE)


def solve_5bd6f4ac(S, I):
    x1 = tojvec(SIX)
    O = crop(I, x1, THREE_BY_THREE)
    return O

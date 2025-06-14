def solve_5bd6f4ac_one(S, I):
    return crop(I, tojvec(SIX), THREE_BY_THREE)


def solve_5bd6f4ac(S, I, x=0):
    x1 = tojvec(SIX)
    if x == 1:
        return x1
    O = crop(I, x1, THREE_BY_THREE)
    return O

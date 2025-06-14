def solve_25ff71a9_one(S, I):
    return move(I, get_nth_f(o_g(I, R7), F0), DOWN)


def solve_25ff71a9(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    O = move(I, x2, DOWN)
    return O

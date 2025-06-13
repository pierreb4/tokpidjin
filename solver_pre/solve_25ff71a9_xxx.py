def solve_25ff71a9_one(S, I):
    return move(I, get_nth_f(o_g(I, R7), F0), DOWN)


def solve_25ff71a9(S, I):
    x1 = o_g(I, R7)
    x2 = get_nth_f(x1, F0)
    O = move(I, x2, DOWN)
    return O

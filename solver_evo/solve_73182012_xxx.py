def solve_73182012_one(S, I):
    return tophalf(lefthalf(subgrid(get_nth_f(o_g(I, R3), F0), I)))


def solve_73182012(S, I):
    x1 = o_g(I, R3)
    x2 = get_nth_f(x1, F0)
    x3 = subgrid(x2, I)
    x4 = lefthalf(x3)
    O = tophalf(x4)
    return O

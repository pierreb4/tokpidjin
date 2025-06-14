def solve_2013d3e2_one(S, I):
    return tophalf(lefthalf(subgrid(get_nth_f(o_g(I, R3), F0), I)))


def solve_2013d3e2(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = lefthalf(x3)
    if x == 4:
        return x4
    O = tophalf(x4)
    return O

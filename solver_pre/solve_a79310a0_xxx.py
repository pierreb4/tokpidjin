def solve_a79310a0_one(S, I):
    return replace(move(I, get_nth_f(o_g(I, R5), F0), DOWN), EIGHT, TWO)


def solve_a79310a0(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = move(I, x2, DOWN)
    if x == 3:
        return x3
    O = replace(x3, EIGHT, TWO)
    return O

def solve_a79310a0_one(S, I):
    return replace(move(I, get_nth_f(o_g(I, R5), F0), DOWN), EIGHT, TWO)


def solve_a79310a0(S, I):
    x1 = o_g(I, R5)
    x2 = get_nth_f(x1, F0)
    x3 = move(I, x2, DOWN)
    O = replace(x3, EIGHT, TWO)
    return O

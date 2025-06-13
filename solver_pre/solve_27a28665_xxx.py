def solve_27a28665_one(S, I):
    return canvas(branch(equality(get_val_rank_f(o_g(I, R4), size, F0), FIVE), SIX, branch(equality(get_val_rank_f(o_g(I, R4), size, F0), FOUR), THREE, branch(equality(get_val_rank_f(o_g(I, R4), size, F0), ONE), TWO, ONE))), UNITY)


def solve_27a28665(S, I):
    x1 = o_g(I, R4)
    x2 = get_val_rank_f(x1, size, F0)
    x3 = equality(x2, FIVE)
    x4 = equality(x2, FOUR)
    x5 = equality(x2, ONE)
    x6 = branch(x5, TWO, ONE)
    x7 = branch(x4, THREE, x6)
    x8 = branch(x3, SIX, x7)
    O = canvas(x8, UNITY)
    return O

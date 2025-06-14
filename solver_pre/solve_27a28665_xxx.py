def solve_27a28665_one(S, I):
    return canvas(branch(equality(get_val_rank_f(o_g(I, R4), size, F0), FIVE), SIX, branch(equality(get_val_rank_f(o_g(I, R4), size, F0), FOUR), THREE, branch(equality(get_val_rank_f(o_g(I, R4), size, F0), ONE), TWO, ONE))), UNITY)


def solve_27a28665(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = get_val_rank_f(x1, size, F0)
    if x == 2:
        return x2
    x3 = equality(x2, FIVE)
    if x == 3:
        return x3
    x4 = equality(x2, FOUR)
    if x == 4:
        return x4
    x5 = equality(x2, ONE)
    if x == 5:
        return x5
    x6 = branch(x5, TWO, ONE)
    if x == 6:
        return x6
    x7 = branch(x4, THREE, x6)
    if x == 7:
        return x7
    x8 = branch(x3, SIX, x7)
    if x == 8:
        return x8
    O = canvas(x8, UNITY)
    return O

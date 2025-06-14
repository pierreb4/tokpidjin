def solve_6b9890af_one(S, I):
    return paint(subgrid(f_ofcolor(I, TWO), I), shift(normalize(upscale_f(get_arg_rank_f(o_g(I, R7), size, L1), divide(width_t(subgrid(f_ofcolor(I, TWO), I)), THREE))), UNITY))


def solve_6b9890af(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = subgrid(x1, I)
    if x == 2:
        return x2
    x3 = o_g(I, R7)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x3, size, L1)
    if x == 4:
        return x4
    x5 = width_t(x2)
    if x == 5:
        return x5
    x6 = divide(x5, THREE)
    if x == 6:
        return x6
    x7 = upscale_f(x4, x6)
    if x == 7:
        return x7
    x8 = normalize(x7)
    if x == 8:
        return x8
    x9 = shift(x8, UNITY)
    if x == 9:
        return x9
    O = paint(x2, x9)
    return O

def solve_6b9890af_one(S, I):
    return paint(subgrid(f_ofcolor(I, TWO), I), shift(normalize(upscale_f(get_arg_rank_f(o_g(I, R7), size, L1), divide(width_t(subgrid(f_ofcolor(I, TWO), I)), THREE))), UNITY))


def solve_6b9890af(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = subgrid(x1, I)
    x3 = o_g(I, R7)
    x4 = get_arg_rank_f(x3, size, L1)
    x5 = width_t(x2)
    x6 = divide(x5, THREE)
    x7 = upscale_f(x4, x6)
    x8 = normalize(x7)
    x9 = shift(x8, UNITY)
    O = paint(x2, x9)
    return O

def solve_09629e4f_one(S, I):
    return fill(paint(I, upscale_f(normalize(get_arg_rank(o_g(I, R3), numcolors_f, L1)), FOUR)), FIVE, f_ofcolor(I, FIVE))


def solve_09629e4f(S, I):
    x1 = o_g(I, R3)
    x2 = get_arg_rank(x1, numcolors_f, L1)
    x3 = normalize(x2)
    x4 = upscale_f(x3, FOUR)
    x5 = paint(I, x4)
    x6 = f_ofcolor(I, FIVE)
    O = fill(x5, FIVE, x6)
    return O

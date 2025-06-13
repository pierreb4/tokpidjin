def solve_f25fbde4_one(S, I):
    return upscale_t(subgrid(get_nth_f(o_g(I, R7), F0), I), TWO)


def solve_f25fbde4(S, I):
    x1 = o_g(I, R7)
    x2 = get_nth_f(x1, F0)
    x3 = subgrid(x2, I)
    O = upscale_t(x3, TWO)
    return O

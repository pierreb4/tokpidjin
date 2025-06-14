def solve_445eab21_one(S, I):
    return canvas(color(get_arg_rank_f(o_g(I, R5), fork(multiply, height_f, width_f), F0)), TWO_BY_TWO)


def solve_445eab21(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = fork(multiply, height_f, width_f)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x1, x2, F0)
    if x == 3:
        return x3
    x4 = color(x3)
    if x == 4:
        return x4
    O = canvas(x4, TWO_BY_TWO)
    return O

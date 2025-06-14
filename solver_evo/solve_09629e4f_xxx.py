def solve_09629e4f_one(S, I):
    return fill(paint(I, upscale_f(normalize(get_arg_rank(o_g(I, R3), numcolors_f, L1)), FOUR)), GRAY, f_ofcolor(I, GRAY))


def solve_09629e4f(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = get_arg_rank(x1, numcolors_f, L1)
    if x == 2:
        return x2
    x3 = normalize(x2)
    if x == 3:
        return x3
    x4 = upscale_f(x3, FOUR)
    if x == 4:
        return x4
    x5 = paint(I, x4)
    if x == 5:
        return x5
    x6 = f_ofcolor(I, GRAY)
    if x == 6:
        return x6
    O = fill(x5, GRAY, x6)
    return O

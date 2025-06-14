def solve_d9fac9be_one(S, I):
    return canvas(other_f(remove(ZERO, palette_t(I)), color(get_arg_rank_f(o_g(I, R5), size, F0))), UNITY)


def solve_d9fac9be(S, I, x=0):
    x1 = palette_t(I)
    if x == 1:
        return x1
    x2 = remove(ZERO, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x3, size, F0)
    if x == 4:
        return x4
    x5 = color(x4)
    if x == 5:
        return x5
    x6 = other_f(x2, x5)
    if x == 6:
        return x6
    O = canvas(x6, UNITY)
    return O

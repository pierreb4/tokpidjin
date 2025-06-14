def solve_9565186b_one(S, I):
    return paint(canvas(FIVE, shape_t(I)), get_arg_rank_f(o_g(I, R4), size, F0))


def solve_9565186b(S, I, x=0):
    x1 = shape_t(I)
    if x == 1:
        return x1
    x2 = canvas(FIVE, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R4)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x3, size, F0)
    if x == 4:
        return x4
    O = paint(x2, x4)
    return O

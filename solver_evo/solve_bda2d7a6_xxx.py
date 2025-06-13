def solve_bda2d7a6_one(S, I):
    return paint(I, mpapply(recolor_o, apply(color, order(partition(I), size)), combine_t(repeat(get_nth_t(order(partition(I), size), L1), BLUE), remove_f(get_nth_t(order(partition(I), size), L1), order(partition(I), size)))))


def solve_bda2d7a6(S, I):
    x1 = partition(I)
    x2 = order(x1, size)
    x3 = apply(color, x2)
    x4 = get_nth_t(x2, L1)
    x5 = repeat(x4, BLUE)
    x6 = remove_f(x4, x2)
    x7 = combine_t(x5, x6)
    x8 = mpapply(recolor_o, x3, x7)
    O = paint(I, x8)
    return O

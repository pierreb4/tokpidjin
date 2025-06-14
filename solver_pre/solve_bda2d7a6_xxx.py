def solve_bda2d7a6_one(S, I):
    return paint(I, mpapply(recolor_o, apply(color, order(partition(I), size)), combine_t(repeat(get_nth_t(order(partition(I), size), L1), ONE), remove_f(get_nth_t(order(partition(I), size), L1), order(partition(I), size)))))


def solve_bda2d7a6(S, I, x=0):
    x1 = partition(I)
    if x == 1:
        return x1
    x2 = order(x1, size)
    if x == 2:
        return x2
    x3 = apply(color, x2)
    if x == 3:
        return x3
    x4 = get_nth_t(x2, L1)
    if x == 4:
        return x4
    x5 = repeat(x4, ONE)
    if x == 5:
        return x5
    x6 = remove_f(x4, x2)
    if x == 6:
        return x6
    x7 = combine_t(x5, x6)
    if x == 7:
        return x7
    x8 = mpapply(recolor_o, x3, x7)
    if x == 8:
        return x8
    O = paint(I, x8)
    return O

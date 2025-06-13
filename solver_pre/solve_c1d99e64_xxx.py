def solve_c1d99e64_one(S, I):
    return fill(I, TWO, merge_f(frontiers(I)))


def solve_c1d99e64(S, I):
    x1 = frontiers(I)
    x2 = merge_f(x1)
    O = fill(I, TWO, x2)
    return O

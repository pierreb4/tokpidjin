def solve_c1d99e64_one(S, I):
    return fill(I, TWO, merge_f(frontiers(I)))


def solve_c1d99e64(S, I, x=0):
    x1 = frontiers(I)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    O = fill(I, TWO, x2)
    return O

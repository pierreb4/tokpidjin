def solve_ce22a75a_one(S, I):
    return fill(I, ONE, mapply(backdrop, apply(outbox, o_g(I, R5))))


def solve_ce22a75a(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = apply(outbox, x1)
    if x == 2:
        return x2
    x3 = mapply(backdrop, x2)
    if x == 3:
        return x3
    O = fill(I, ONE, x3)
    return O

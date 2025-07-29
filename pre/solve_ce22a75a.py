def solve_ce22a75a_one(S, I):
    return fill(I, ONE, mapply(backdrop, apply(outbox, o_g(I, R5))))


def solve_ce22a75a(S, I):
    x1 = o_g(I, R5)
    x2 = apply(outbox, x1)
    x3 = mapply(backdrop, x2)
    O = fill(I, ONE, x3)
    return O

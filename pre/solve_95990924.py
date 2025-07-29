def solve_95990924_one(S, I):
    return fill(fill(fill(fill(I, ONE, apply(rbind(corner, R0), apply(outbox, o_g(I, R5)))), TWO, apply(rbind(corner, R1), apply(outbox, o_g(I, R5)))), THREE, apply(rbind(corner, R2), apply(outbox, o_g(I, R5)))), FOUR, apply(rbind(corner, R3), apply(outbox, o_g(I, R5))))


def solve_95990924(S, I):
    x1 = rbind(corner, R0)
    x2 = o_g(I, R5)
    x3 = apply(outbox, x2)
    x4 = apply(x1, x3)
    x5 = fill(I, ONE, x4)
    x6 = rbind(corner, R1)
    x7 = apply(x6, x3)
    x8 = fill(x5, TWO, x7)
    x9 = rbind(corner, R2)
    x10 = apply(x9, x3)
    x11 = fill(x8, THREE, x10)
    x12 = rbind(corner, R3)
    x13 = apply(x12, x3)
    O = fill(x11, FOUR, x13)
    return O

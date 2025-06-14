def solve_95990924_one(S, I):
    return fill(fill(fill(fill(I, ONE, apply(rbind(corner, R0), apply(outbox, o_g(I, R5)))), TWO, apply(rbind(corner, R1), apply(outbox, o_g(I, R5)))), THREE, apply(rbind(corner, R2), apply(outbox, o_g(I, R5)))), FOUR, apply(rbind(corner, R3), apply(outbox, o_g(I, R5))))


def solve_95990924(S, I, x=0):
    x1 = rbind(corner, R0)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = apply(outbox, x2)
    if x == 3:
        return x3
    x4 = apply(x1, x3)
    if x == 4:
        return x4
    x5 = fill(I, ONE, x4)
    if x == 5:
        return x5
    x6 = rbind(corner, R1)
    if x == 6:
        return x6
    x7 = apply(x6, x3)
    if x == 7:
        return x7
    x8 = fill(x5, TWO, x7)
    if x == 8:
        return x8
    x9 = rbind(corner, R2)
    if x == 9:
        return x9
    x10 = apply(x9, x3)
    if x == 10:
        return x10
    x11 = fill(x8, THREE, x10)
    if x == 11:
        return x11
    x12 = rbind(corner, R3)
    if x == 12:
        return x12
    x13 = apply(x12, x3)
    if x == 13:
        return x13
    O = fill(x11, FOUR, x13)
    return O

def solve_95990924_one(S, I):
    return fill(fill(fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), apply(rbind(corner, R0), apply(outbox, o_g(I, R5)))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), apply(rbind(corner, R1), apply(outbox, o_g(I, R5)))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), apply(rbind(corner, R2), apply(outbox, o_g(I, R5)))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F3)), apply(rbind(corner, R3), apply(outbox, o_g(I, R5))))


def solve_95990924(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = rbind(corner, R0)
    if x == 4:
        return x4
    x5 = o_g(I, R5)
    if x == 5:
        return x5
    x6 = apply(outbox, x5)
    if x == 6:
        return x6
    x7 = apply(x4, x6)
    if x == 7:
        return x7
    x8 = fill(I, x3, x7)
    if x == 8:
        return x8
    x9 = rbind(get_nth_t, F1)
    if x == 9:
        return x9
    x10 = c_zo_n(S, x1, x9)
    if x == 10:
        return x10
    x11 = rbind(corner, R1)
    if x == 11:
        return x11
    x12 = apply(x11, x6)
    if x == 12:
        return x12
    x13 = fill(x8, x10, x12)
    if x == 13:
        return x13
    x14 = rbind(get_nth_t, F2)
    if x == 14:
        return x14
    x15 = c_zo_n(S, x1, x14)
    if x == 15:
        return x15
    x16 = rbind(corner, R2)
    if x == 16:
        return x16
    x17 = apply(x16, x6)
    if x == 17:
        return x17
    x18 = fill(x13, x15, x17)
    if x == 18:
        return x18
    x19 = rbind(get_nth_t, F3)
    if x == 19:
        return x19
    x20 = c_zo_n(S, x1, x19)
    if x == 20:
        return x20
    x21 = rbind(corner, R3)
    if x == 21:
        return x21
    x22 = apply(x21, x6)
    if x == 22:
        return x22
    O = fill(x18, x20, x22)
    return O

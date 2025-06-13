def solve_95990924_one(S, I):
    return fill(fill(fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), apply(rbind(corner, R0), apply(outbox, o_g(I, R5)))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), apply(rbind(corner, R1), apply(outbox, o_g(I, R5)))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), apply(rbind(corner, R2), apply(outbox, o_g(I, R5)))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F3)), apply(rbind(corner, R3), apply(outbox, o_g(I, R5))))


def solve_95990924(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = rbind(corner, R0)
    x5 = o_g(I, R5)
    x6 = apply(outbox, x5)
    x7 = apply(x4, x6)
    x8 = fill(I, x3, x7)
    x9 = rbind(get_nth_t, F1)
    x10 = c_zo_n(S, x1, x9)
    x11 = rbind(corner, R1)
    x12 = apply(x11, x6)
    x13 = fill(x8, x10, x12)
    x14 = rbind(get_nth_t, F2)
    x15 = c_zo_n(S, x1, x14)
    x16 = rbind(corner, R2)
    x17 = apply(x16, x6)
    x18 = fill(x13, x15, x17)
    x19 = rbind(get_nth_t, F3)
    x20 = c_zo_n(S, x1, x19)
    x21 = rbind(corner, R3)
    x22 = apply(x21, x6)
    O = fill(x18, x20, x22)
    return O

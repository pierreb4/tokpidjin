def solve_54d82841_one(S, I):
    return fill(I, FOUR, apply(lbind(astuple, decrement(height_t(I))), apply(compose(rbind(get_nth_f, L1), center), o_g(I, R5))))


def solve_54d82841(S, I):
    x1 = height_t(I)
    x2 = decrement(x1)
    x3 = lbind(astuple, x2)
    x4 = rbind(get_nth_f, L1)
    x5 = compose(x4, center)
    x6 = o_g(I, R5)
    x7 = apply(x5, x6)
    x8 = apply(x3, x7)
    O = fill(I, FOUR, x8)
    return O

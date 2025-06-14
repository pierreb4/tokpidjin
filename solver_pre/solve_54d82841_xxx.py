def solve_54d82841_one(S, I):
    return fill(I, FOUR, apply(lbind(astuple, decrement(height_t(I))), apply(compose(rbind(get_nth_f, L1), center), o_g(I, R5))))


def solve_54d82841(S, I, x=0):
    x1 = height_t(I)
    if x == 1:
        return x1
    x2 = decrement(x1)
    if x == 2:
        return x2
    x3 = lbind(astuple, x2)
    if x == 3:
        return x3
    x4 = rbind(get_nth_f, L1)
    if x == 4:
        return x4
    x5 = compose(x4, center)
    if x == 5:
        return x5
    x6 = o_g(I, R5)
    if x == 6:
        return x6
    x7 = apply(x5, x6)
    if x == 7:
        return x7
    x8 = apply(x3, x7)
    if x == 8:
        return x8
    O = fill(I, FOUR, x8)
    return O

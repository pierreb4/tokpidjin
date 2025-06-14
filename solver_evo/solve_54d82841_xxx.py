def solve_54d82841_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), apply(lbind(astuple, decrement(height_t(I))), apply(compose(rbind(get_nth_f, L1), center), o_g(I, R5))))


def solve_54d82841(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = height_t(I)
    if x == 4:
        return x4
    x5 = decrement(x4)
    if x == 5:
        return x5
    x6 = lbind(astuple, x5)
    if x == 6:
        return x6
    x7 = rbind(get_nth_f, L1)
    if x == 7:
        return x7
    x8 = compose(x7, center)
    if x == 8:
        return x8
    x9 = o_g(I, R5)
    if x == 9:
        return x9
    x10 = apply(x8, x9)
    if x == 10:
        return x10
    x11 = apply(x6, x10)
    if x == 11:
        return x11
    O = fill(I, x3, x11)
    return O

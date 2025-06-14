def solve_bb43febb_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(compose(backdrop, inbox), colorfilter(o_g(I, R4), GRAY)))


def solve_bb43febb(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = compose(backdrop, inbox)
    if x == 4:
        return x4
    x5 = o_g(I, R4)
    if x == 5:
        return x5
    x6 = colorfilter(x5, GRAY)
    if x == 6:
        return x6
    x7 = mapply(x4, x6)
    if x == 7:
        return x7
    O = fill(I, x3, x7)
    return O

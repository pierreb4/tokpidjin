def solve_50cb2852_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(compose(backdrop, inbox), o_g(I, R5)))


def solve_50cb2852(S, I, x=0):
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
    x5 = o_g(I, R5)
    if x == 5:
        return x5
    x6 = mapply(x4, x5)
    if x == 6:
        return x6
    O = fill(I, x3, x6)
    return O

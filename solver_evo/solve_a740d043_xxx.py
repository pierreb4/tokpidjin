def solve_a740d043_one(S, I):
    return replace(subgrid(merge_f(o_g(I, R7)), I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)))


def solve_a740d043(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = identity(p_g)
    if x == 4:
        return x4
    x5 = rbind(get_nth_t, F0)
    if x == 5:
        return x5
    x6 = c_iz_n(S, x4, x5)
    if x == 6:
        return x6
    x7 = c_zo_n(S, x4, x5)
    if x == 7:
        return x7
    O = replace(x3, x6, x7)
    return O

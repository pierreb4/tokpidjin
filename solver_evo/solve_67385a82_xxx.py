def solve_67385a82_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), merge_f(difference(colorfilter(o_g(I, R4), GREEN), sizefilter(colorfilter(o_g(I, R4), GREEN), ONE))))


def solve_67385a82(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R4)
    if x == 4:
        return x4
    x5 = colorfilter(x4, GREEN)
    if x == 5:
        return x5
    x6 = sizefilter(x5, ONE)
    if x == 6:
        return x6
    x7 = difference(x5, x6)
    if x == 7:
        return x7
    x8 = merge_f(x7)
    if x == 8:
        return x8
    O = fill(I, x3, x8)
    return O

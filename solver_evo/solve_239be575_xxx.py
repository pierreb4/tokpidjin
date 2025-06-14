def solve_239be575_one(S, I):
    return canvas(branch(greater(size_f(sfilter_f(o_g(I, R3), compose(lbind(contained, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), palette_f))), ONE), BLACK, CYAN), UNITY)


def solve_239be575(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = identity(p_g)
    if x == 2:
        return x2
    x3 = rbind(get_nth_t, F0)
    if x == 3:
        return x3
    x4 = c_iz_n(S, x2, x3)
    if x == 4:
        return x4
    x5 = lbind(contained, x4)
    if x == 5:
        return x5
    x6 = compose(x5, palette_f)
    if x == 6:
        return x6
    x7 = sfilter_f(x1, x6)
    if x == 7:
        return x7
    x8 = size_f(x7)
    if x == 8:
        return x8
    x9 = greater(x8, ONE)
    if x == 9:
        return x9
    x10 = branch(x9, BLACK, CYAN)
    if x == 10:
        return x10
    O = canvas(x10, UNITY)
    return O

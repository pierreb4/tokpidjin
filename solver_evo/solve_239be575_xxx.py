def solve_239be575_one(S, I):
    return canvas(branch(greater(size_f(sfilter_f(o_g(I, R3), compose(lbind(contained, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), palette_f))), ONE), BLACK, CYAN), UNITY)


def solve_239be575(S, I):
    x1 = o_g(I, R3)
    x2 = identity(p_g)
    x3 = rbind(get_nth_t, F0)
    x4 = c_iz_n(S, x2, x3)
    x5 = lbind(contained, x4)
    x6 = compose(x5, palette_f)
    x7 = sfilter_f(x1, x6)
    x8 = size_f(x7)
    x9 = greater(x8, ONE)
    x10 = branch(x9, BLACK, CYAN)
    O = canvas(x10, UNITY)
    return O

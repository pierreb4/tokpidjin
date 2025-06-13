def solve_5117e062_one(S, I):
    return replace(subgrid(extract(o_g(I, R3), matcher(numcolors_f, RED)), I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)), get_color_rank_f(extract(o_g(I, R3), matcher(numcolors_f, RED)), F0))


def solve_5117e062(S, I):
    x1 = o_g(I, R3)
    x2 = matcher(numcolors_f, RED)
    x3 = extract(x1, x2)
    x4 = subgrid(x3, I)
    x5 = identity(p_g)
    x6 = rbind(get_nth_t, F1)
    x7 = c_iz_n(S, x5, x6)
    x8 = get_color_rank_f(x3, F0)
    O = replace(x4, x7, x8)
    return O

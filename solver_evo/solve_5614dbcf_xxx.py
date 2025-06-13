def solve_5614dbcf_one(S, I):
    return downscale(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), THREE)


def solve_5614dbcf(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_iz_n(S, x1, x2)
    x4 = replace(I, x3, BLACK)
    O = downscale(x4, THREE)
    return O

def solve_5614dbcf_one(S, I):
    return downscale(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), THREE)


def solve_5614dbcf(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_iz_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = replace(I, x3, BLACK)
    if x == 4:
        return x4
    O = downscale(x4, THREE)
    return O

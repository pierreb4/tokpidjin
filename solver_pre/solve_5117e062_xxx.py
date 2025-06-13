def solve_5117e062_one(S, I):
    return replace(subgrid(extract(o_g(I, R3), matcher(numcolors_f, TWO)), I), EIGHT, get_color_rank_f(extract(o_g(I, R3), matcher(numcolors_f, TWO)), F0))


def solve_5117e062(S, I):
    x1 = o_g(I, R3)
    x2 = matcher(numcolors_f, TWO)
    x3 = extract(x1, x2)
    x4 = subgrid(x3, I)
    x5 = get_color_rank_f(x3, F0)
    O = replace(x4, EIGHT, x5)
    return O

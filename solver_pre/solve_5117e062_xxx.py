def solve_5117e062_one(S, I):
    return replace(subgrid(extract(o_g(I, R3), matcher(numcolors_f, TWO)), I), EIGHT, get_color_rank_f(extract(o_g(I, R3), matcher(numcolors_f, TWO)), F0))


def solve_5117e062(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = matcher(numcolors_f, TWO)
    if x == 2:
        return x2
    x3 = extract(x1, x2)
    if x == 3:
        return x3
    x4 = subgrid(x3, I)
    if x == 4:
        return x4
    x5 = get_color_rank_f(x3, F0)
    if x == 5:
        return x5
    O = replace(x4, EIGHT, x5)
    return O

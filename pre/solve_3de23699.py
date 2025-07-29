def solve_3de23699_one(S, I):
    return replace(trim(subgrid(get_nth_f(sizefilter(fgpartition(I), FOUR), F0), I)), color(get_nth_f(difference(fgpartition(I), sizefilter(fgpartition(I), FOUR)), F0)), color(get_nth_f(sizefilter(fgpartition(I), FOUR), F0)))


def solve_3de23699(S, I):
    x1 = fgpartition(I)
    x2 = sizefilter(x1, FOUR)
    x3 = get_nth_f(x2, F0)
    x4 = subgrid(x3, I)
    x5 = trim(x4)
    x6 = difference(x1, x2)
    x7 = get_nth_f(x6, F0)
    x8 = color(x7)
    x9 = color(x3)
    O = replace(x5, x8, x9)
    return O

def solve_3de23699_one(S, I):
    return replace(trim(subgrid(get_nth_f(sizefilter(fgpartition(I), FOUR), F0), I)), color(get_nth_f(difference(fgpartition(I), sizefilter(fgpartition(I), FOUR)), F0)), color(get_nth_f(sizefilter(fgpartition(I), FOUR), F0)))


def solve_3de23699(S, I, x=0):
    x1 = fgpartition(I)
    if x == 1:
        return x1
    x2 = sizefilter(x1, FOUR)
    if x == 2:
        return x2
    x3 = get_nth_f(x2, F0)
    if x == 3:
        return x3
    x4 = subgrid(x3, I)
    if x == 4:
        return x4
    x5 = trim(x4)
    if x == 5:
        return x5
    x6 = difference(x1, x2)
    if x == 6:
        return x6
    x7 = get_nth_f(x6, F0)
    if x == 7:
        return x7
    x8 = color(x7)
    if x == 8:
        return x8
    x9 = color(x3)
    if x == 9:
        return x9
    O = replace(x5, x8, x9)
    return O

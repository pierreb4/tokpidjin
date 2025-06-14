def solve_88a62173_one(S, I):
    return get_common_rank_t(combine_t(astuple(tophalf(lefthalf(I)), tophalf(righthalf(I))), astuple(bottomhalf(lefthalf(I)), bottomhalf(righthalf(I)))), L1)


def solve_88a62173(S, I, x=0):
    x1 = lefthalf(I)
    if x == 1:
        return x1
    x2 = tophalf(x1)
    if x == 2:
        return x2
    x3 = righthalf(I)
    if x == 3:
        return x3
    x4 = tophalf(x3)
    if x == 4:
        return x4
    x5 = astuple(x2, x4)
    if x == 5:
        return x5
    x6 = bottomhalf(x1)
    if x == 6:
        return x6
    x7 = bottomhalf(x3)
    if x == 7:
        return x7
    x8 = astuple(x6, x7)
    if x == 8:
        return x8
    x9 = combine_t(x5, x8)
    if x == 9:
        return x9
    O = get_common_rank_t(x9, L1)
    return O

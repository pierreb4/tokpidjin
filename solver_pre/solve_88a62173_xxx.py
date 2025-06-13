def solve_88a62173_one(S, I):
    return get_common_rank_t(combine_t(astuple(tophalf(lefthalf(I)), tophalf(righthalf(I))), astuple(bottomhalf(lefthalf(I)), bottomhalf(righthalf(I)))), L1)


def solve_88a62173(S, I):
    x1 = lefthalf(I)
    x2 = tophalf(x1)
    x3 = righthalf(I)
    x4 = tophalf(x3)
    x5 = astuple(x2, x4)
    x6 = bottomhalf(x1)
    x7 = bottomhalf(x3)
    x8 = astuple(x6, x7)
    x9 = combine_t(x5, x8)
    O = get_common_rank_t(x9, L1)
    return O

def solve(S, I, C):
    return move(I, merge_f(sizefilter(replace(I, FIVE, BLACK), ONE)), TWO_BY_ZERO)
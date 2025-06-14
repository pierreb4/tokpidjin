def solve_7f4411dc_one(S, I):
    return fill(I, BLACK, sfilter_f(f_ofcolor(I, get_color_rank_t(I, L1)), compose(chain(rbind(greater, RED), size, rbind(difference, f_ofcolor(I, get_color_rank_t(I, L1)))), dneighbors)))


def solve_7f4411dc(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, x1)
    if x == 2:
        return x2
    x3 = rbind(greater, RED)
    if x == 3:
        return x3
    x4 = rbind(difference, x2)
    if x == 4:
        return x4
    x5 = chain(x3, size, x4)
    if x == 5:
        return x5
    x6 = compose(x5, dneighbors)
    if x == 6:
        return x6
    x7 = sfilter_f(x2, x6)
    if x == 7:
        return x7
    O = fill(I, BLACK, x7)
    return O

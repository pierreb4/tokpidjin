def solve_7f4411dc_one(S, I):
    return fill(I, ZERO, sfilter_f(f_ofcolor(I, get_color_rank_t(I, L1)), compose(chain(rbind(greater, TWO), size, rbind(difference, f_ofcolor(I, get_color_rank_t(I, L1)))), dneighbors)))


def solve_7f4411dc(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = f_ofcolor(I, x1)
    x3 = rbind(greater, TWO)
    x4 = rbind(difference, x2)
    x5 = chain(x3, size, x4)
    x6 = compose(x5, dneighbors)
    x7 = sfilter_f(x2, x6)
    O = fill(I, ZERO, x7)
    return O

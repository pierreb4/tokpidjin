def solve_7e0986d6_one(S, I):
    return fill(replace(I, get_color_rank_t(I, L1), BLACK), get_color_rank_t(replace(I, get_color_rank_t(I, L1), BLACK), L1), sfilter_f(f_ofcolor(I, get_color_rank_t(I, L1)), chain(chain(positive, decrement, rbind(colorcount_f, get_color_rank_t(replace(I, get_color_rank_t(I, L1), BLACK), L1))), rbind(toobject, replace(I, get_color_rank_t(I, L1), BLACK)), dneighbors)))


def solve_7e0986d6(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = replace(I, x1, BLACK)
    x3 = get_color_rank_t(x2, L1)
    x4 = f_ofcolor(I, x1)
    x5 = rbind(colorcount_f, x3)
    x6 = chain(positive, decrement, x5)
    x7 = rbind(toobject, x2)
    x8 = chain(x6, x7, dneighbors)
    x9 = sfilter_f(x4, x8)
    O = fill(x2, x3, x9)
    return O

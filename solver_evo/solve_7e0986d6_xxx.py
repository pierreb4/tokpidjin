def solve_7e0986d6_one(S, I):
    return fill(replace(I, get_color_rank_t(I, L1), BLACK), get_color_rank_t(replace(I, get_color_rank_t(I, L1), BLACK), L1), sfilter_f(f_ofcolor(I, get_color_rank_t(I, L1)), chain(chain(positive, decrement, rbind(colorcount_f, get_color_rank_t(replace(I, get_color_rank_t(I, L1), BLACK), L1))), rbind(toobject, replace(I, get_color_rank_t(I, L1), BLACK)), dneighbors)))


def solve_7e0986d6(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = replace(I, x1, BLACK)
    if x == 2:
        return x2
    x3 = get_color_rank_t(x2, L1)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, x1)
    if x == 4:
        return x4
    x5 = rbind(colorcount_f, x3)
    if x == 5:
        return x5
    x6 = chain(positive, decrement, x5)
    if x == 6:
        return x6
    x7 = rbind(toobject, x2)
    if x == 7:
        return x7
    x8 = chain(x6, x7, dneighbors)
    if x == 8:
        return x8
    x9 = sfilter_f(x4, x8)
    if x == 9:
        return x9
    O = fill(x2, x3, x9)
    return O

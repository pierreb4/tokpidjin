def solve_b782dc8a_one(S, I):
    return fill(fill(I, get_color_rank_t(I, L1), sfilter_f(toindices(mfilter_f(colorfilter(o_g(I, R4), ZERO), rbind(adjacent, f_ofcolor(I, get_color_rank_f(toobject(dneighbors(get_nth_f(f_ofcolor(I, get_color_rank_t(I, L1)), F0)), I), F0))))), chain(even, rbind(manhattan, f_ofcolor(I, get_color_rank_t(I, L1))), initset))), get_color_rank_f(toobject(dneighbors(get_nth_f(f_ofcolor(I, get_color_rank_t(I, L1)), F0)), I), F0), difference(toindices(mfilter_f(colorfilter(o_g(I, R4), ZERO), rbind(adjacent, f_ofcolor(I, get_color_rank_f(toobject(dneighbors(get_nth_f(f_ofcolor(I, get_color_rank_t(I, L1)), F0)), I), F0))))), sfilter_f(toindices(mfilter_f(colorfilter(o_g(I, R4), ZERO), rbind(adjacent, f_ofcolor(I, get_color_rank_f(toobject(dneighbors(get_nth_f(f_ofcolor(I, get_color_rank_t(I, L1)), F0)), I), F0))))), chain(even, rbind(manhattan, f_ofcolor(I, get_color_rank_t(I, L1))), initset))))


def solve_b782dc8a(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = o_g(I, R4)
    x3 = colorfilter(x2, ZERO)
    x4 = f_ofcolor(I, x1)
    x5 = get_nth_f(x4, F0)
    x6 = dneighbors(x5)
    x7 = toobject(x6, I)
    x8 = get_color_rank_f(x7, F0)
    x9 = f_ofcolor(I, x8)
    x10 = rbind(adjacent, x9)
    x11 = mfilter_f(x3, x10)
    x12 = toindices(x11)
    x13 = rbind(manhattan, x4)
    x14 = chain(even, x13, initset)
    x15 = sfilter_f(x12, x14)
    x16 = fill(I, x1, x15)
    x17 = difference(x12, x15)
    O = fill(x16, x8, x17)
    return O

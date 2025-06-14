def solve_b782dc8a_one(S, I):
    return fill(fill(I, get_color_rank_t(I, L1), sfilter_f(toindices(mfilter_f(colorfilter(o_g(I, R4), BLACK), rbind(adjacent, f_ofcolor(I, get_color_rank_f(toobject(dneighbors(get_nth_f(f_ofcolor(I, get_color_rank_t(I, L1)), F0)), I), F0))))), chain(even, rbind(manhattan, f_ofcolor(I, get_color_rank_t(I, L1))), initset))), get_color_rank_f(toobject(dneighbors(get_nth_f(f_ofcolor(I, get_color_rank_t(I, L1)), F0)), I), F0), difference(toindices(mfilter_f(colorfilter(o_g(I, R4), BLACK), rbind(adjacent, f_ofcolor(I, get_color_rank_f(toobject(dneighbors(get_nth_f(f_ofcolor(I, get_color_rank_t(I, L1)), F0)), I), F0))))), sfilter_f(toindices(mfilter_f(colorfilter(o_g(I, R4), BLACK), rbind(adjacent, f_ofcolor(I, get_color_rank_f(toobject(dneighbors(get_nth_f(f_ofcolor(I, get_color_rank_t(I, L1)), F0)), I), F0))))), chain(even, rbind(manhattan, f_ofcolor(I, get_color_rank_t(I, L1))), initset))))


def solve_b782dc8a(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = o_g(I, R4)
    if x == 2:
        return x2
    x3 = colorfilter(x2, BLACK)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, x1)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = dneighbors(x5)
    if x == 6:
        return x6
    x7 = toobject(x6, I)
    if x == 7:
        return x7
    x8 = get_color_rank_f(x7, F0)
    if x == 8:
        return x8
    x9 = f_ofcolor(I, x8)
    if x == 9:
        return x9
    x10 = rbind(adjacent, x9)
    if x == 10:
        return x10
    x11 = mfilter_f(x3, x10)
    if x == 11:
        return x11
    x12 = toindices(x11)
    if x == 12:
        return x12
    x13 = rbind(manhattan, x4)
    if x == 13:
        return x13
    x14 = chain(even, x13, initset)
    if x == 14:
        return x14
    x15 = sfilter_f(x12, x14)
    if x == 15:
        return x15
    x16 = fill(I, x1, x15)
    if x == 16:
        return x16
    x17 = difference(x12, x15)
    if x == 17:
        return x17
    O = fill(x16, x8, x17)
    return O

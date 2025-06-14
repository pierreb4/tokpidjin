def solve_5daaa586_one(S, I):
    return fill(subgrid(outbox(extract(colorfilter(o_g(I, R4), ZERO), compose(flip, rbind(bordering, I)))), I), color(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), ZERO), compose(flip, rbind(bordering, I)))), I)), size, F0)), branch(greater(size_f(mfilter_f(prapply(connect, toindices(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), ZERO), compose(flip, rbind(bordering, I)))), I)), size, F0)), toindices(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), ZERO), compose(flip, rbind(bordering, I)))), I)), size, F0))), vline_i)), size_f(mfilter_f(prapply(connect, toindices(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), ZERO), compose(flip, rbind(bordering, I)))), I)), size, F0)), toindices(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), ZERO), compose(flip, rbind(bordering, I)))), I)), size, F0))), hline_i))), mfilter_f(prapply(connect, toindices(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), ZERO), compose(flip, rbind(bordering, I)))), I)), size, F0)), toindices(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), ZERO), compose(flip, rbind(bordering, I)))), I)), size, F0))), vline_i), mfilter_f(prapply(connect, toindices(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), ZERO), compose(flip, rbind(bordering, I)))), I)), size, F0)), toindices(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), ZERO), compose(flip, rbind(bordering, I)))), I)), size, F0))), hline_i)))


def solve_5daaa586(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = rbind(bordering, I)
    if x == 3:
        return x3
    x4 = compose(flip, x3)
    if x == 4:
        return x4
    x5 = extract(x2, x4)
    if x == 5:
        return x5
    x6 = outbox(x5)
    if x == 6:
        return x6
    x7 = subgrid(x6, I)
    if x == 7:
        return x7
    x8 = fgpartition(x7)
    if x == 8:
        return x8
    x9 = get_arg_rank_f(x8, size, F0)
    if x == 9:
        return x9
    x10 = color(x9)
    if x == 10:
        return x10
    x11 = toindices(x9)
    if x == 11:
        return x11
    x12 = prapply(connect, x11, x11)
    if x == 12:
        return x12
    x13 = mfilter_f(x12, vline_i)
    if x == 13:
        return x13
    x14 = size_f(x13)
    if x == 14:
        return x14
    x15 = mfilter_f(x12, hline_i)
    if x == 15:
        return x15
    x16 = size_f(x15)
    if x == 16:
        return x16
    x17 = greater(x14, x16)
    if x == 17:
        return x17
    x18 = branch(x17, x13, x15)
    if x == 18:
        return x18
    O = fill(x7, x10, x18)
    return O

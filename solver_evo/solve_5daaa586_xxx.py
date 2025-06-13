def solve_5daaa586_one(S, I):
    return fill(subgrid(outbox(extract(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I)))), I), color(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I)))), I)), size, F0)), branch(greater(size_f(mfilter_f(prapply(connect, toindices(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I)))), I)), size, F0)), toindices(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I)))), I)), size, F0))), vline_i)), size_f(mfilter_f(prapply(connect, toindices(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I)))), I)), size, F0)), toindices(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I)))), I)), size, F0))), hline_i))), mfilter_f(prapply(connect, toindices(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I)))), I)), size, F0)), toindices(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I)))), I)), size, F0))), vline_i), mfilter_f(prapply(connect, toindices(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I)))), I)), size, F0)), toindices(get_arg_rank_f(fgpartition(subgrid(outbox(extract(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I)))), I)), size, F0))), hline_i)))


def solve_5daaa586(S, I):
    x1 = o_g(I, R4)
    x2 = colorfilter(x1, BLACK)
    x3 = rbind(bordering, I)
    x4 = compose(flip, x3)
    x5 = extract(x2, x4)
    x6 = outbox(x5)
    x7 = subgrid(x6, I)
    x8 = fgpartition(x7)
    x9 = get_arg_rank_f(x8, size, F0)
    x10 = color(x9)
    x11 = toindices(x9)
    x12 = prapply(connect, x11, x11)
    x13 = mfilter_f(x12, vline_i)
    x14 = size_f(x13)
    x15 = mfilter_f(x12, hline_i)
    x16 = size_f(x15)
    x17 = greater(x14, x16)
    x18 = branch(x17, x13, x15)
    O = fill(x7, x10, x18)
    return O

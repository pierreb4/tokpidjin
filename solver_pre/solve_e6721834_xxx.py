def solve_e6721834_one(S, I):
    return paint(get_nth_f(order(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t), F0), mfilter_f(apply(fork(shift, identity, fork(subtract, chain(rbind(get_nth_f, F0), lbind(occurrences, get_nth_f(order(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t), F0)), rbind(sfilter, compose(flip, matcher(rbind(get_nth_f, F0), get_color_rank_f(merge_f(o_g(get_nth_t(order(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t), L1), R1)), F0))))), compose(rbind(corner, R0), rbind(sfilter, compose(flip, matcher(rbind(get_nth_f, F0), get_color_rank_f(merge_f(o_g(get_nth_t(order(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t), L1), R1)), F0))))))), sfilter_f(o_g(get_nth_t(order(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t), L1), R1), chain(positive, size, compose(lbind(occurrences, get_nth_f(order(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t), F0)), rbind(sfilter, compose(flip, matcher(rbind(get_nth_f, F0), get_color_rank_f(merge_f(o_g(get_nth_t(order(branch(portrait_t(I), vsplit, hsplit)(I, TWO), numcolors_t), L1), R1)), F0)))))))), chain(positive, decrement, compose(decrement, width_f))))


def solve_e6721834(S, I, x=0):
    x1 = portrait_t(I)
    if x == 1:
        return x1
    x2 = branch(x1, vsplit, hsplit)
    if x == 2:
        return x2
    x3 = x2(I, TWO)
    if x == 3:
        return x3
    x4 = order(x3, numcolors_t)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = rbind(get_nth_f, F0)
    if x == 6:
        return x6
    x7 = lbind(occurrences, x5)
    if x == 7:
        return x7
    x8 = get_nth_t(x4, L1)
    if x == 8:
        return x8
    x9 = o_g(x8, R1)
    if x == 9:
        return x9
    x10 = merge_f(x9)
    if x == 10:
        return x10
    x11 = get_color_rank_f(x10, F0)
    if x == 11:
        return x11
    x12 = matcher(x6, x11)
    if x == 12:
        return x12
    x13 = compose(flip, x12)
    if x == 13:
        return x13
    x14 = rbind(sfilter, x13)
    if x == 14:
        return x14
    x15 = chain(x6, x7, x14)
    if x == 15:
        return x15
    x16 = rbind(corner, R0)
    if x == 16:
        return x16
    x17 = compose(x16, x14)
    if x == 17:
        return x17
    x18 = fork(subtract, x15, x17)
    if x == 18:
        return x18
    x19 = fork(shift, identity, x18)
    if x == 19:
        return x19
    x20 = compose(x7, x14)
    if x == 20:
        return x20
    x21 = chain(positive, size, x20)
    if x == 21:
        return x21
    x22 = sfilter_f(x9, x21)
    if x == 22:
        return x22
    x23 = apply(x19, x22)
    if x == 23:
        return x23
    x24 = compose(decrement, width_f)
    if x == 24:
        return x24
    x25 = chain(positive, decrement, x24)
    if x == 25:
        return x25
    x26 = mfilter_f(x23, x25)
    if x == 26:
        return x26
    O = paint(x5, x26)
    return O

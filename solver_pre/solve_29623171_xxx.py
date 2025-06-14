def solve_29623171_one(S, I):
    return fill(fill(I, get_color_rank_t(I, L1), mfilter_f(apply(fork(product, compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)), rbind(get_nth_f, F0)), compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)), rbind(get_nth_f, L1))), product(interval(ZERO, NINE, FOUR), interval(ZERO, NINE, FOUR))), matcher(compose(rbind(colorcount_f, get_color_rank_t(I, L1)), rbind(toobject, I)), get_val_rank_f(apply(fork(product, compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)), rbind(get_nth_f, F0)), compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)), rbind(get_nth_f, L1))), product(interval(ZERO, NINE, FOUR), interval(ZERO, NINE, FOUR))), compose(rbind(colorcount_f, get_color_rank_t(I, L1)), rbind(toobject, I)), F0)))), ZERO, mfilter_f(apply(fork(product, compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)), rbind(get_nth_f, F0)), compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)), rbind(get_nth_f, L1))), product(interval(ZERO, NINE, FOUR), interval(ZERO, NINE, FOUR))), compose(flip, matcher(compose(rbind(colorcount_f, get_color_rank_t(I, L1)), rbind(toobject, I)), get_val_rank_f(apply(fork(product, compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)), rbind(get_nth_f, F0)), compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)), rbind(get_nth_f, L1))), product(interval(ZERO, NINE, FOUR), interval(ZERO, NINE, FOUR))), compose(rbind(colorcount_f, get_color_rank_t(I, L1)), rbind(toobject, I)), F0)))))


def solve_29623171(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = rbind(interval, ONE)
    if x == 2:
        return x2
    x3 = rbind(add, THREE)
    if x == 3:
        return x3
    x4 = fork(x2, identity, x3)
    if x == 4:
        return x4
    x5 = rbind(get_nth_f, F0)
    if x == 5:
        return x5
    x6 = compose(x4, x5)
    if x == 6:
        return x6
    x7 = rbind(get_nth_f, L1)
    if x == 7:
        return x7
    x8 = compose(x4, x7)
    if x == 8:
        return x8
    x9 = fork(product, x6, x8)
    if x == 9:
        return x9
    x10 = interval(ZERO, NINE, FOUR)
    if x == 10:
        return x10
    x11 = product(x10, x10)
    if x == 11:
        return x11
    x12 = apply(x9, x11)
    if x == 12:
        return x12
    x13 = rbind(colorcount_f, x1)
    if x == 13:
        return x13
    x14 = rbind(toobject, I)
    if x == 14:
        return x14
    x15 = compose(x13, x14)
    if x == 15:
        return x15
    x16 = get_val_rank_f(x12, x15, F0)
    if x == 16:
        return x16
    x17 = matcher(x15, x16)
    if x == 17:
        return x17
    x18 = mfilter_f(x12, x17)
    if x == 18:
        return x18
    x19 = fill(I, x1, x18)
    if x == 19:
        return x19
    x20 = compose(flip, x17)
    if x == 20:
        return x20
    x21 = mfilter_f(x12, x20)
    if x == 21:
        return x21
    O = fill(x19, ZERO, x21)
    return O

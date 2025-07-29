def solve_29623171_one(S, I):
    return fill(fill(I, get_color_rank_t(I, L1), mfilter_f(apply(fork(product, compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)), rbind(get_nth_f, F0)), compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)), rbind(get_nth_f, L1))), product(interval(ZERO, NINE, FOUR), interval(ZERO, NINE, FOUR))), matcher(compose(rbind(colorcount_f, get_color_rank_t(I, L1)), rbind(toobject, I)), get_val_rank_f(apply(fork(product, compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)), rbind(get_nth_f, F0)), compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)), rbind(get_nth_f, L1))), product(interval(ZERO, NINE, FOUR), interval(ZERO, NINE, FOUR))), compose(rbind(colorcount_f, get_color_rank_t(I, L1)), rbind(toobject, I)), F0)))), ZERO, mfilter_f(apply(fork(product, compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)), rbind(get_nth_f, F0)), compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)), rbind(get_nth_f, L1))), product(interval(ZERO, NINE, FOUR), interval(ZERO, NINE, FOUR))), compose(flip, matcher(compose(rbind(colorcount_f, get_color_rank_t(I, L1)), rbind(toobject, I)), get_val_rank_f(apply(fork(product, compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)), rbind(get_nth_f, F0)), compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)), rbind(get_nth_f, L1))), product(interval(ZERO, NINE, FOUR), interval(ZERO, NINE, FOUR))), compose(rbind(colorcount_f, get_color_rank_t(I, L1)), rbind(toobject, I)), F0)))))


def solve_29623171(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = rbind(interval, ONE)
    x3 = rbind(add, THREE)
    x4 = fork(x2, identity, x3)
    x5 = rbind(get_nth_f, F0)
    x6 = compose(x4, x5)
    x7 = rbind(get_nth_f, L1)
    x8 = compose(x4, x7)
    x9 = fork(product, x6, x8)
    x10 = interval(ZERO, NINE, FOUR)
    x11 = product(x10, x10)
    x12 = apply(x9, x11)
    x13 = rbind(colorcount_f, x1)
    x14 = rbind(toobject, I)
    x15 = compose(x13, x14)
    x16 = get_val_rank_f(x12, x15, F0)
    x17 = matcher(x15, x16)
    x18 = mfilter_f(x12, x17)
    x19 = fill(I, x1, x18)
    x20 = compose(flip, x17)
    x21 = mfilter_f(x12, x20)
    O = fill(x19, ZERO, x21)
    return O

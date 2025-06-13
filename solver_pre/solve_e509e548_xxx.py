def solve_e509e548_one(S, I):
    return fill(fill(replace(I, THREE, SIX), TWO, mfilter_f(o_g(I, R5), compose(lbind(contained, THREE), chain(palette_t, trim, rbind(subgrid, I))))), ONE, mfilter_f(o_g(I, R5), fork(equality, size, compose(decrement, fork(add, height_f, width_f)))))


def solve_e509e548(S, I):
    x1 = replace(I, THREE, SIX)
    x2 = o_g(I, R5)
    x3 = lbind(contained, THREE)
    x4 = rbind(subgrid, I)
    x5 = chain(palette_t, trim, x4)
    x6 = compose(x3, x5)
    x7 = mfilter_f(x2, x6)
    x8 = fill(x1, TWO, x7)
    x9 = fork(add, height_f, width_f)
    x10 = compose(decrement, x9)
    x11 = fork(equality, size, x10)
    x12 = mfilter_f(x2, x11)
    O = fill(x8, ONE, x12)
    return O

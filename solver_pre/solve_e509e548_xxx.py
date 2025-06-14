def solve_e509e548_one(S, I):
    return fill(fill(replace(I, THREE, SIX), TWO, mfilter_f(o_g(I, R5), compose(lbind(contained, THREE), chain(palette_t, trim, rbind(subgrid, I))))), ONE, mfilter_f(o_g(I, R5), fork(equality, size, compose(decrement, fork(add, height_f, width_f)))))


def solve_e509e548(S, I, x=0):
    x1 = replace(I, THREE, SIX)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = lbind(contained, THREE)
    if x == 3:
        return x3
    x4 = rbind(subgrid, I)
    if x == 4:
        return x4
    x5 = chain(palette_t, trim, x4)
    if x == 5:
        return x5
    x6 = compose(x3, x5)
    if x == 6:
        return x6
    x7 = mfilter_f(x2, x6)
    if x == 7:
        return x7
    x8 = fill(x1, TWO, x7)
    if x == 8:
        return x8
    x9 = fork(add, height_f, width_f)
    if x == 9:
        return x9
    x10 = compose(decrement, x9)
    if x == 10:
        return x10
    x11 = fork(equality, size, x10)
    if x == 11:
        return x11
    x12 = mfilter_f(x2, x11)
    if x == 12:
        return x12
    O = fill(x8, ONE, x12)
    return O

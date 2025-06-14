def solve_c444b776_one(S, I):
    return paint(I, mapply(compose(lbind(shift, normalize(toobject(backdrop(get_arg_rank_f(colorfilter(o_g(I, R4), ZERO), size, L1)), I))), rbind(corner, R0)), colorfilter(o_g(I, R4), ZERO)))


def solve_c444b776(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x2, size, L1)
    if x == 3:
        return x3
    x4 = backdrop(x3)
    if x == 4:
        return x4
    x5 = toobject(x4, I)
    if x == 5:
        return x5
    x6 = normalize(x5)
    if x == 6:
        return x6
    x7 = lbind(shift, x6)
    if x == 7:
        return x7
    x8 = rbind(corner, R0)
    if x == 8:
        return x8
    x9 = compose(x7, x8)
    if x == 9:
        return x9
    x10 = mapply(x9, x2)
    if x == 10:
        return x10
    O = paint(I, x10)
    return O

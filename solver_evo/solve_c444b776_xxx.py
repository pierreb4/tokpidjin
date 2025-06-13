def solve_c444b776_one(S, I):
    return paint(I, mapply(compose(lbind(shift, normalize(toobject(backdrop(get_arg_rank_f(colorfilter(o_g(I, R4), BLACK), size, L1)), I))), rbind(corner, R0)), colorfilter(o_g(I, R4), BLACK)))


def solve_c444b776(S, I):
    x1 = o_g(I, R4)
    x2 = colorfilter(x1, BLACK)
    x3 = get_arg_rank_f(x2, size, L1)
    x4 = backdrop(x3)
    x5 = toobject(x4, I)
    x6 = normalize(x5)
    x7 = lbind(shift, x6)
    x8 = rbind(corner, R0)
    x9 = compose(x7, x8)
    x10 = mapply(x9, x2)
    O = paint(I, x10)
    return O

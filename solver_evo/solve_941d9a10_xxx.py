def solve_941d9a10_one(S, I):
    return fill(fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), compose(lbind(extract, apply(toindices, colorfilter(o_g(I, R4), BLACK))), lbind(lbind, contained))(ORIGIN)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), compose(lbind(extract, apply(toindices, colorfilter(o_g(I, R4), BLACK))), lbind(lbind, contained))(decrement(shape_t(I)))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), compose(lbind(extract, apply(toindices, colorfilter(o_g(I, R4), BLACK))), lbind(lbind, contained))(astuple(FIVE, FIVE)))


def solve_941d9a10(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = o_g(I, R4)
    x5 = colorfilter(x4, BLACK)
    x6 = apply(toindices, x5)
    x7 = lbind(extract, x6)
    x8 = lbind(lbind, contained)
    x9 = compose(x7, x8)
    x10 = x9(ORIGIN)
    x11 = fill(I, x3, x10)
    x12 = rbind(get_nth_t, F2)
    x13 = c_zo_n(S, x1, x12)
    x14 = shape_t(I)
    x15 = decrement(x14)
    x16 = x9(x15)
    x17 = fill(x11, x13, x16)
    x18 = rbind(get_nth_t, F1)
    x19 = c_zo_n(S, x1, x18)
    x20 = astuple(FIVE, FIVE)
    x21 = x9(x20)
    O = fill(x17, x19, x21)
    return O

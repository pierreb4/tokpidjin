def solve_941d9a10_one(S, I):
    return fill(fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), compose(lbind(extract, apply(toindices, colorfilter(o_g(I, R4), BLACK))), lbind(lbind, contained))(ORIGIN)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), compose(lbind(extract, apply(toindices, colorfilter(o_g(I, R4), BLACK))), lbind(lbind, contained))(decrement(shape_t(I)))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), compose(lbind(extract, apply(toindices, colorfilter(o_g(I, R4), BLACK))), lbind(lbind, contained))(astuple(FIVE, FIVE)))


def solve_941d9a10(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R4)
    if x == 4:
        return x4
    x5 = colorfilter(x4, BLACK)
    if x == 5:
        return x5
    x6 = apply(toindices, x5)
    if x == 6:
        return x6
    x7 = lbind(extract, x6)
    if x == 7:
        return x7
    x8 = lbind(lbind, contained)
    if x == 8:
        return x8
    x9 = compose(x7, x8)
    if x == 9:
        return x9
    x10 = x9(ORIGIN)
    if x == 10:
        return x10
    x11 = fill(I, x3, x10)
    if x == 11:
        return x11
    x12 = rbind(get_nth_t, F2)
    if x == 12:
        return x12
    x13 = c_zo_n(S, x1, x12)
    if x == 13:
        return x13
    x14 = shape_t(I)
    if x == 14:
        return x14
    x15 = decrement(x14)
    if x == 15:
        return x15
    x16 = x9(x15)
    if x == 16:
        return x16
    x17 = fill(x11, x13, x16)
    if x == 17:
        return x17
    x18 = rbind(get_nth_t, F1)
    if x == 18:
        return x18
    x19 = c_zo_n(S, x1, x18)
    if x == 19:
        return x19
    x20 = astuple(FIVE, FIVE)
    if x == 20:
        return x20
    x21 = x9(x20)
    if x == 21:
        return x21
    O = fill(x17, x19, x21)
    return O

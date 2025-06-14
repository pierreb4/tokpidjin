def solve_539a4f51_one(S, I):
    return paint(canvas(index(I, ORIGIN), multiply(UNITY, TEN)), asobject(vconcat(hconcat(crop(I, ORIGIN, branch(positive(colorcount_t(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), decrement(shape_t(I)), shape_t(I))), vupscale(crop(crop(I, ORIGIN, branch(positive(colorcount_t(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), decrement(shape_t(I)), shape_t(I))), ORIGIN, astuple(ONE, width_t(crop(I, ORIGIN, branch(positive(colorcount_t(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), decrement(shape_t(I)), shape_t(I)))))), width_t(crop(I, ORIGIN, branch(positive(colorcount_t(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), decrement(shape_t(I)), shape_t(I)))))), hconcat(mir_rot_t(vupscale(crop(crop(I, ORIGIN, branch(positive(colorcount_t(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), decrement(shape_t(I)), shape_t(I))), ORIGIN, astuple(ONE, width_t(crop(I, ORIGIN, branch(positive(colorcount_t(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), decrement(shape_t(I)), shape_t(I)))))), width_t(crop(I, ORIGIN, branch(positive(colorcount_t(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), decrement(shape_t(I)), shape_t(I))))), R1), crop(I, ORIGIN, branch(positive(colorcount_t(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), decrement(shape_t(I)), shape_t(I)))))))


def solve_539a4f51(S, I, x=0):
    x1 = index(I, ORIGIN)
    if x == 1:
        return x1
    x2 = multiply(UNITY, TEN)
    if x == 2:
        return x2
    x3 = canvas(x1, x2)
    if x == 3:
        return x3
    x4 = identity(p_g)
    if x == 4:
        return x4
    x5 = rbind(get_nth_t, F0)
    if x == 5:
        return x5
    x6 = c_iz_n(S, x4, x5)
    if x == 6:
        return x6
    x7 = colorcount_t(I, x6)
    if x == 7:
        return x7
    x8 = positive(x7)
    if x == 8:
        return x8
    x9 = shape_t(I)
    if x == 9:
        return x9
    x10 = decrement(x9)
    if x == 10:
        return x10
    x11 = branch(x8, x10, x9)
    if x == 11:
        return x11
    x12 = crop(I, ORIGIN, x11)
    if x == 12:
        return x12
    x13 = width_t(x12)
    if x == 13:
        return x13
    x14 = astuple(ONE, x13)
    if x == 14:
        return x14
    x15 = crop(x12, ORIGIN, x14)
    if x == 15:
        return x15
    x16 = vupscale(x15, x13)
    if x == 16:
        return x16
    x17 = hconcat(x12, x16)
    if x == 17:
        return x17
    x18 = mir_rot_t(x16, R1)
    if x == 18:
        return x18
    x19 = hconcat(x18, x12)
    if x == 19:
        return x19
    x20 = vconcat(x17, x19)
    if x == 20:
        return x20
    x21 = asobject(x20)
    if x == 21:
        return x21
    O = paint(x3, x21)
    return O

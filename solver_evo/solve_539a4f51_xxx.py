def solve_539a4f51_one(S, I):
    return paint(canvas(index(I, ORIGIN), multiply(UNITY, TEN)), asobject(vconcat(hconcat(crop(I, ORIGIN, branch(positive(colorcount_t(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), decrement(shape_t(I)), shape_t(I))), vupscale(crop(crop(I, ORIGIN, branch(positive(colorcount_t(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), decrement(shape_t(I)), shape_t(I))), ORIGIN, astuple(ONE, width_t(crop(I, ORIGIN, branch(positive(colorcount_t(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), decrement(shape_t(I)), shape_t(I)))))), width_t(crop(I, ORIGIN, branch(positive(colorcount_t(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), decrement(shape_t(I)), shape_t(I)))))), hconcat(mir_rot_t(vupscale(crop(crop(I, ORIGIN, branch(positive(colorcount_t(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), decrement(shape_t(I)), shape_t(I))), ORIGIN, astuple(ONE, width_t(crop(I, ORIGIN, branch(positive(colorcount_t(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), decrement(shape_t(I)), shape_t(I)))))), width_t(crop(I, ORIGIN, branch(positive(colorcount_t(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), decrement(shape_t(I)), shape_t(I))))), R1), crop(I, ORIGIN, branch(positive(colorcount_t(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), decrement(shape_t(I)), shape_t(I)))))))


def solve_539a4f51(S, I):
    x1 = index(I, ORIGIN)
    x2 = multiply(UNITY, TEN)
    x3 = canvas(x1, x2)
    x4 = identity(p_g)
    x5 = rbind(get_nth_t, F0)
    x6 = c_iz_n(S, x4, x5)
    x7 = colorcount_t(I, x6)
    x8 = positive(x7)
    x9 = shape_t(I)
    x10 = decrement(x9)
    x11 = branch(x8, x10, x9)
    x12 = crop(I, ORIGIN, x11)
    x13 = width_t(x12)
    x14 = astuple(ONE, x13)
    x15 = crop(x12, ORIGIN, x14)
    x16 = vupscale(x15, x13)
    x17 = hconcat(x12, x16)
    x18 = mir_rot_t(x16, R1)
    x19 = hconcat(x18, x12)
    x20 = vconcat(x17, x19)
    x21 = asobject(x20)
    O = paint(x3, x21)
    return O

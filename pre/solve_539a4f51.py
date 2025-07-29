def solve_539a4f51_one(S, I):
    return paint(canvas(index(I, ORIGIN), multiply(UNITY, TEN)), asobject(vconcat(hconcat(crop(I, ORIGIN, branch(positive(colorcount_t(I, ZERO)), decrement(shape_t(I)), shape_t(I))), vupscale(crop(crop(I, ORIGIN, branch(positive(colorcount_t(I, ZERO)), decrement(shape_t(I)), shape_t(I))), ORIGIN, astuple(ONE, width_t(crop(I, ORIGIN, branch(positive(colorcount_t(I, ZERO)), decrement(shape_t(I)), shape_t(I)))))), width_t(crop(I, ORIGIN, branch(positive(colorcount_t(I, ZERO)), decrement(shape_t(I)), shape_t(I)))))), hconcat(mir_rot_t(vupscale(crop(crop(I, ORIGIN, branch(positive(colorcount_t(I, ZERO)), decrement(shape_t(I)), shape_t(I))), ORIGIN, astuple(ONE, width_t(crop(I, ORIGIN, branch(positive(colorcount_t(I, ZERO)), decrement(shape_t(I)), shape_t(I)))))), width_t(crop(I, ORIGIN, branch(positive(colorcount_t(I, ZERO)), decrement(shape_t(I)), shape_t(I))))), R1), crop(I, ORIGIN, branch(positive(colorcount_t(I, ZERO)), decrement(shape_t(I)), shape_t(I)))))))


def solve_539a4f51(S, I):
    x1 = index(I, ORIGIN)
    x2 = multiply(UNITY, TEN)
    x3 = canvas(x1, x2)
    x4 = colorcount_t(I, ZERO)
    x5 = positive(x4)
    x6 = shape_t(I)
    x7 = decrement(x6)
    x8 = branch(x5, x7, x6)
    x9 = crop(I, ORIGIN, x8)
    x10 = width_t(x9)
    x11 = astuple(ONE, x10)
    x12 = crop(x9, ORIGIN, x11)
    x13 = vupscale(x12, x10)
    x14 = hconcat(x9, x13)
    x15 = mir_rot_t(x13, R1)
    x16 = hconcat(x15, x9)
    x17 = vconcat(x14, x16)
    x18 = asobject(x17)
    O = paint(x3, x18)
    return O

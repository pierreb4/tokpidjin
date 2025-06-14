def solve_539a4f51_one(S, I):
    return paint(canvas(index(I, ORIGIN), multiply(UNITY, TEN)), asobject(vconcat(hconcat(crop(I, ORIGIN, branch(positive(colorcount_t(I, ZERO)), decrement(shape_t(I)), shape_t(I))), vupscale(crop(crop(I, ORIGIN, branch(positive(colorcount_t(I, ZERO)), decrement(shape_t(I)), shape_t(I))), ORIGIN, astuple(ONE, width_t(crop(I, ORIGIN, branch(positive(colorcount_t(I, ZERO)), decrement(shape_t(I)), shape_t(I)))))), width_t(crop(I, ORIGIN, branch(positive(colorcount_t(I, ZERO)), decrement(shape_t(I)), shape_t(I)))))), hconcat(mir_rot_t(vupscale(crop(crop(I, ORIGIN, branch(positive(colorcount_t(I, ZERO)), decrement(shape_t(I)), shape_t(I))), ORIGIN, astuple(ONE, width_t(crop(I, ORIGIN, branch(positive(colorcount_t(I, ZERO)), decrement(shape_t(I)), shape_t(I)))))), width_t(crop(I, ORIGIN, branch(positive(colorcount_t(I, ZERO)), decrement(shape_t(I)), shape_t(I))))), R1), crop(I, ORIGIN, branch(positive(colorcount_t(I, ZERO)), decrement(shape_t(I)), shape_t(I)))))))


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
    x4 = colorcount_t(I, ZERO)
    if x == 4:
        return x4
    x5 = positive(x4)
    if x == 5:
        return x5
    x6 = shape_t(I)
    if x == 6:
        return x6
    x7 = decrement(x6)
    if x == 7:
        return x7
    x8 = branch(x5, x7, x6)
    if x == 8:
        return x8
    x9 = crop(I, ORIGIN, x8)
    if x == 9:
        return x9
    x10 = width_t(x9)
    if x == 10:
        return x10
    x11 = astuple(ONE, x10)
    if x == 11:
        return x11
    x12 = crop(x9, ORIGIN, x11)
    if x == 12:
        return x12
    x13 = vupscale(x12, x10)
    if x == 13:
        return x13
    x14 = hconcat(x9, x13)
    if x == 14:
        return x14
    x15 = mir_rot_t(x13, R1)
    if x == 15:
        return x15
    x16 = hconcat(x15, x9)
    if x == 16:
        return x16
    x17 = vconcat(x14, x16)
    if x == 17:
        return x17
    x18 = asobject(x17)
    if x == 18:
        return x18
    O = paint(x3, x18)
    return O

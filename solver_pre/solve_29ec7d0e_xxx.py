def solve_29ec7d0e_one(S, I):
    return paint(I, mapply(lbind(shift, merge(difference(partition(I), colorfilter(partition(I), ZERO)))), apply(lbind(multiply, astuple(vperiod(asobject(crop(I, tojvec(decrement(height_t(I))), astuple(height_t(I), ONE)))), hperiod(asobject(crop(I, toivec(decrement(width_t(I))), astuple(ONE, width_t(I))))))), mapply(neighbors, neighbors(ORIGIN)))))


def solve_29ec7d0e(S, I, x=0):
    x1 = partition(I)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = difference(x1, x2)
    if x == 3:
        return x3
    x4 = merge(x3)
    if x == 4:
        return x4
    x5 = lbind(shift, x4)
    if x == 5:
        return x5
    x6 = height_t(I)
    if x == 6:
        return x6
    x7 = decrement(x6)
    if x == 7:
        return x7
    x8 = tojvec(x7)
    if x == 8:
        return x8
    x9 = astuple(x6, ONE)
    if x == 9:
        return x9
    x10 = crop(I, x8, x9)
    if x == 10:
        return x10
    x11 = asobject(x10)
    if x == 11:
        return x11
    x12 = vperiod(x11)
    if x == 12:
        return x12
    x13 = width_t(I)
    if x == 13:
        return x13
    x14 = decrement(x13)
    if x == 14:
        return x14
    x15 = toivec(x14)
    if x == 15:
        return x15
    x16 = astuple(ONE, x13)
    if x == 16:
        return x16
    x17 = crop(I, x15, x16)
    if x == 17:
        return x17
    x18 = asobject(x17)
    if x == 18:
        return x18
    x19 = hperiod(x18)
    if x == 19:
        return x19
    x20 = astuple(x12, x19)
    if x == 20:
        return x20
    x21 = lbind(multiply, x20)
    if x == 21:
        return x21
    x22 = neighbors(ORIGIN)
    if x == 22:
        return x22
    x23 = mapply(neighbors, x22)
    if x == 23:
        return x23
    x24 = apply(x21, x23)
    if x == 24:
        return x24
    x25 = mapply(x5, x24)
    if x == 25:
        return x25
    O = paint(I, x25)
    return O

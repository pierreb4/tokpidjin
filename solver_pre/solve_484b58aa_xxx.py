def solve_484b58aa_one(S, I):
    return paint(I, mapply(lbind(shift, merge(difference(partition(I), colorfilter(partition(I), ZERO)))), apply(lbind(multiply, astuple(vperiod(asobject(crop(I, tojvec(power(decrement, TWO)(height_t(I))), astuple(height_t(I), TWO)))), hperiod(asobject(crop(I, toivec(power(decrement, TWO)(width_t(I))), astuple(TWO, width_t(I))))))), mapply(neighbors, neighbors(ORIGIN)))))


def solve_484b58aa(S, I, x=0):
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
    x6 = power(decrement, TWO)
    if x == 6:
        return x6
    x7 = height_t(I)
    if x == 7:
        return x7
    x8 = x6(x7)
    if x == 8:
        return x8
    x9 = tojvec(x8)
    if x == 9:
        return x9
    x10 = astuple(x7, TWO)
    if x == 10:
        return x10
    x11 = crop(I, x9, x10)
    if x == 11:
        return x11
    x12 = asobject(x11)
    if x == 12:
        return x12
    x13 = vperiod(x12)
    if x == 13:
        return x13
    x14 = width_t(I)
    if x == 14:
        return x14
    x15 = x6(x14)
    if x == 15:
        return x15
    x16 = toivec(x15)
    if x == 16:
        return x16
    x17 = astuple(TWO, x14)
    if x == 17:
        return x17
    x18 = crop(I, x16, x17)
    if x == 18:
        return x18
    x19 = asobject(x18)
    if x == 19:
        return x19
    x20 = hperiod(x19)
    if x == 20:
        return x20
    x21 = astuple(x13, x20)
    if x == 21:
        return x21
    x22 = lbind(multiply, x21)
    if x == 22:
        return x22
    x23 = neighbors(ORIGIN)
    if x == 23:
        return x23
    x24 = mapply(neighbors, x23)
    if x == 24:
        return x24
    x25 = apply(x22, x24)
    if x == 25:
        return x25
    x26 = mapply(x5, x25)
    if x == 26:
        return x26
    O = paint(I, x26)
    return O

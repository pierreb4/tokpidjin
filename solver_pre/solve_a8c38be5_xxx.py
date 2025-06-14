def solve_a8c38be5_one(S, I):
    return paint(canvas(FIVE, astuple(NINE, NINE)), mapply(fork(shift, identity, compose(chain(rbind(corner, R0), lbind(extract, apply(toindices, o_g(fill(canvas(FIVE, astuple(NINE, NINE)), ONE, combine(difference(box(asindices(canvas(FIVE, astuple(NINE, NINE)))), mapply(chain(outbox, outbox, initset), corners(asindices(canvas(FIVE, astuple(NINE, NINE)))))), sfilter_f(inbox(box(asindices(canvas(FIVE, astuple(NINE, NINE))))), compose(lbind(contained, ZERO), rbind(subtract, center(asindices(canvas(FIVE, astuple(NINE, NINE))))))))), R5))), lbind(matcher, normalize)), toindices)), apply(normalize, o_g(replace(I, FIVE, ZERO), R5))))


def solve_a8c38be5(S, I, x=0):
    x1 = astuple(NINE, NINE)
    if x == 1:
        return x1
    x2 = canvas(FIVE, x1)
    if x == 2:
        return x2
    x3 = rbind(corner, R0)
    if x == 3:
        return x3
    x4 = asindices(x2)
    if x == 4:
        return x4
    x5 = box(x4)
    if x == 5:
        return x5
    x6 = chain(outbox, outbox, initset)
    if x == 6:
        return x6
    x7 = corners(x4)
    if x == 7:
        return x7
    x8 = mapply(x6, x7)
    if x == 8:
        return x8
    x9 = difference(x5, x8)
    if x == 9:
        return x9
    x10 = inbox(x5)
    if x == 10:
        return x10
    x11 = lbind(contained, ZERO)
    if x == 11:
        return x11
    x12 = center(x4)
    if x == 12:
        return x12
    x13 = rbind(subtract, x12)
    if x == 13:
        return x13
    x14 = compose(x11, x13)
    if x == 14:
        return x14
    x15 = sfilter_f(x10, x14)
    if x == 15:
        return x15
    x16 = combine(x9, x15)
    if x == 16:
        return x16
    x17 = fill(x2, ONE, x16)
    if x == 17:
        return x17
    x18 = o_g(x17, R5)
    if x == 18:
        return x18
    x19 = apply(toindices, x18)
    if x == 19:
        return x19
    x20 = lbind(extract, x19)
    if x == 20:
        return x20
    x21 = lbind(matcher, normalize)
    if x == 21:
        return x21
    x22 = chain(x3, x20, x21)
    if x == 22:
        return x22
    x23 = compose(x22, toindices)
    if x == 23:
        return x23
    x24 = fork(shift, identity, x23)
    if x == 24:
        return x24
    x25 = replace(I, FIVE, ZERO)
    if x == 25:
        return x25
    x26 = o_g(x25, R5)
    if x == 26:
        return x26
    x27 = apply(normalize, x26)
    if x == 27:
        return x27
    x28 = mapply(x24, x27)
    if x == 28:
        return x28
    O = paint(x2, x28)
    return O

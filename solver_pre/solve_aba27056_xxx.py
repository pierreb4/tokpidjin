def solve_aba27056_one(S, I):
    return fill(fill(fill(I, FOUR, delta(mapply(toindices, o_g(I, R5)))), FOUR, mapply(lbind(shift, difference(box(mapply(toindices, o_g(I, R5))), mapply(toindices, o_g(I, R5)))), apply(lbind(multiply, position(delta(mapply(toindices, o_g(I, R5))), difference(box(mapply(toindices, o_g(I, R5))), mapply(toindices, o_g(I, R5))))), interval(ZERO, NINE, ONE)))), FOUR, mapply(fork(shoot, rbind(get_nth_f, F0), fork(subtract, rbind(get_nth_f, L1), rbind(get_nth_f, F0))), product(corners(difference(box(mapply(toindices, o_g(I, R5))), mapply(toindices, o_g(I, R5)))), sfilter_f(sfilter_f(f_ofcolor(fill(fill(I, FOUR, delta(mapply(toindices, o_g(I, R5)))), FOUR, mapply(lbind(shift, difference(box(mapply(toindices, o_g(I, R5))), mapply(toindices, o_g(I, R5)))), apply(lbind(multiply, position(delta(mapply(toindices, o_g(I, R5))), difference(box(mapply(toindices, o_g(I, R5))), mapply(toindices, o_g(I, R5))))), interval(ZERO, NINE, ONE)))), ZERO), matcher(chain(rbind(colorcount_f, ZERO), rbind(toobject, fill(fill(I, FOUR, delta(mapply(toindices, o_g(I, R5)))), FOUR, mapply(lbind(shift, difference(box(mapply(toindices, o_g(I, R5))), mapply(toindices, o_g(I, R5)))), apply(lbind(multiply, position(delta(mapply(toindices, o_g(I, R5))), difference(box(mapply(toindices, o_g(I, R5))), mapply(toindices, o_g(I, R5))))), interval(ZERO, NINE, ONE))))), dneighbors), TWO)), compose(fork(both, rbind(adjacent, mapply(toindices, o_g(I, R5))), rbind(adjacent, mapply(lbind(shift, difference(box(mapply(toindices, o_g(I, R5))), mapply(toindices, o_g(I, R5)))), apply(lbind(multiply, position(delta(mapply(toindices, o_g(I, R5))), difference(box(mapply(toindices, o_g(I, R5))), mapply(toindices, o_g(I, R5))))), interval(ZERO, NINE, ONE))))), initset)))))


def solve_aba27056(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = mapply(toindices, x1)
    if x == 2:
        return x2
    x3 = delta(x2)
    if x == 3:
        return x3
    x4 = fill(I, FOUR, x3)
    if x == 4:
        return x4
    x5 = box(x2)
    if x == 5:
        return x5
    x6 = difference(x5, x2)
    if x == 6:
        return x6
    x7 = lbind(shift, x6)
    if x == 7:
        return x7
    x8 = position(x3, x6)
    if x == 8:
        return x8
    x9 = lbind(multiply, x8)
    if x == 9:
        return x9
    x10 = interval(ZERO, NINE, ONE)
    if x == 10:
        return x10
    x11 = apply(x9, x10)
    if x == 11:
        return x11
    x12 = mapply(x7, x11)
    if x == 12:
        return x12
    x13 = fill(x4, FOUR, x12)
    if x == 13:
        return x13
    x14 = rbind(get_nth_f, F0)
    if x == 14:
        return x14
    x15 = rbind(get_nth_f, L1)
    if x == 15:
        return x15
    x16 = fork(subtract, x15, x14)
    if x == 16:
        return x16
    x17 = fork(shoot, x14, x16)
    if x == 17:
        return x17
    x18 = corners(x6)
    if x == 18:
        return x18
    x19 = f_ofcolor(x13, ZERO)
    if x == 19:
        return x19
    x20 = rbind(colorcount_f, ZERO)
    if x == 20:
        return x20
    x21 = rbind(toobject, x13)
    if x == 21:
        return x21
    x22 = chain(x20, x21, dneighbors)
    if x == 22:
        return x22
    x23 = matcher(x22, TWO)
    if x == 23:
        return x23
    x24 = sfilter_f(x19, x23)
    if x == 24:
        return x24
    x25 = rbind(adjacent, x2)
    if x == 25:
        return x25
    x26 = rbind(adjacent, x12)
    if x == 26:
        return x26
    x27 = fork(both, x25, x26)
    if x == 27:
        return x27
    x28 = compose(x27, initset)
    if x == 28:
        return x28
    x29 = sfilter_f(x24, x28)
    if x == 29:
        return x29
    x30 = product(x18, x29)
    if x == 30:
        return x30
    x31 = mapply(x17, x30)
    if x == 31:
        return x31
    O = fill(x13, FOUR, x31)
    return O

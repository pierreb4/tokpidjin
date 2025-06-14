def solve_a78176bb_one(S, I):
    return replace(fill(I, other_f(remove(ZERO, palette_t(I)), FIVE), combine_f(mapply(fork(combine, rbind(shoot, UNITY), rbind(shoot, NEG_UNITY)), apply(rbind(add, UP_RIGHT), apply(rbind(corner, R1), sfilter_f(colorfilter(o_g(I, R5), FIVE), matcher(compose(lbind(index, I), rbind(corner, R1)), FIVE))))), mapply(fork(combine, rbind(shoot, UNITY), rbind(shoot, NEG_UNITY)), apply(rbind(add, DOWN_LEFT), apply(rbind(corner, R2), difference(colorfilter(o_g(I, R5), FIVE), sfilter_f(colorfilter(o_g(I, R5), FIVE), matcher(compose(lbind(index, I), rbind(corner, R1)), FIVE)))))))), FIVE, ZERO)


def solve_a78176bb(S, I, x=0):
    x1 = palette_t(I)
    if x == 1:
        return x1
    x2 = remove(ZERO, x1)
    if x == 2:
        return x2
    x3 = other_f(x2, FIVE)
    if x == 3:
        return x3
    x4 = rbind(shoot, UNITY)
    if x == 4:
        return x4
    x5 = rbind(shoot, NEG_UNITY)
    if x == 5:
        return x5
    x6 = fork(combine, x4, x5)
    if x == 6:
        return x6
    x7 = rbind(add, UP_RIGHT)
    if x == 7:
        return x7
    x8 = rbind(corner, R1)
    if x == 8:
        return x8
    x9 = o_g(I, R5)
    if x == 9:
        return x9
    x10 = colorfilter(x9, FIVE)
    if x == 10:
        return x10
    x11 = lbind(index, I)
    if x == 11:
        return x11
    x12 = compose(x11, x8)
    if x == 12:
        return x12
    x13 = matcher(x12, FIVE)
    if x == 13:
        return x13
    x14 = sfilter_f(x10, x13)
    if x == 14:
        return x14
    x15 = apply(x8, x14)
    if x == 15:
        return x15
    x16 = apply(x7, x15)
    if x == 16:
        return x16
    x17 = mapply(x6, x16)
    if x == 17:
        return x17
    x18 = rbind(add, DOWN_LEFT)
    if x == 18:
        return x18
    x19 = rbind(corner, R2)
    if x == 19:
        return x19
    x20 = difference(x10, x14)
    if x == 20:
        return x20
    x21 = apply(x19, x20)
    if x == 21:
        return x21
    x22 = apply(x18, x21)
    if x == 22:
        return x22
    x23 = mapply(x6, x22)
    if x == 23:
        return x23
    x24 = combine_f(x17, x23)
    if x == 24:
        return x24
    x25 = fill(I, x3, x24)
    if x == 25:
        return x25
    O = replace(x25, FIVE, ZERO)
    return O

def solve_a78176bb_one(S, I):
    return replace(fill(I, other_f(remove(BLACK, palette_t(I)), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), combine_f(mapply(fork(combine, rbind(shoot, UNITY), rbind(shoot, NEG_UNITY)), apply(rbind(add, UP_RIGHT), apply(rbind(corner, R1), sfilter_f(colorfilter(o_g(I, R5), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), matcher(compose(lbind(index, I), rbind(corner, R1)), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))))))), mapply(fork(combine, rbind(shoot, UNITY), rbind(shoot, NEG_UNITY)), apply(rbind(add, DOWN_LEFT), apply(rbind(corner, R2), difference(colorfilter(o_g(I, R5), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), sfilter_f(colorfilter(o_g(I, R5), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), matcher(compose(lbind(index, I), rbind(corner, R1)), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))))))))), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK)


def solve_a78176bb(S, I, x=0):
    x1 = palette_t(I)
    if x == 1:
        return x1
    x2 = remove(BLACK, x1)
    if x == 2:
        return x2
    x3 = identity(p_g)
    if x == 3:
        return x3
    x4 = rbind(get_nth_t, F0)
    if x == 4:
        return x4
    x5 = c_iz_n(S, x3, x4)
    if x == 5:
        return x5
    x6 = other_f(x2, x5)
    if x == 6:
        return x6
    x7 = rbind(shoot, UNITY)
    if x == 7:
        return x7
    x8 = rbind(shoot, NEG_UNITY)
    if x == 8:
        return x8
    x9 = fork(combine, x7, x8)
    if x == 9:
        return x9
    x10 = rbind(add, UP_RIGHT)
    if x == 10:
        return x10
    x11 = rbind(corner, R1)
    if x == 11:
        return x11
    x12 = o_g(I, R5)
    if x == 12:
        return x12
    x13 = colorfilter(x12, x5)
    if x == 13:
        return x13
    x14 = lbind(index, I)
    if x == 14:
        return x14
    x15 = compose(x14, x11)
    if x == 15:
        return x15
    x16 = matcher(x15, x5)
    if x == 16:
        return x16
    x17 = sfilter_f(x13, x16)
    if x == 17:
        return x17
    x18 = apply(x11, x17)
    if x == 18:
        return x18
    x19 = apply(x10, x18)
    if x == 19:
        return x19
    x20 = mapply(x9, x19)
    if x == 20:
        return x20
    x21 = rbind(add, DOWN_LEFT)
    if x == 21:
        return x21
    x22 = rbind(corner, R2)
    if x == 22:
        return x22
    x23 = difference(x13, x17)
    if x == 23:
        return x23
    x24 = apply(x22, x23)
    if x == 24:
        return x24
    x25 = apply(x21, x24)
    if x == 25:
        return x25
    x26 = mapply(x9, x25)
    if x == 26:
        return x26
    x27 = combine_f(x20, x26)
    if x == 27:
        return x27
    x28 = fill(I, x6, x27)
    if x == 28:
        return x28
    O = replace(x28, x5, BLACK)
    return O

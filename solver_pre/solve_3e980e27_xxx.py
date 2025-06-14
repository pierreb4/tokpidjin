def solve_3e980e27_one(S, I):
    return paint(I, combine_f(mapply(chain(rbind(compose, center), lbind(lbind, shift), fork(shift, identity, compose(lbind(compose, compose(invert, rbind(corner, R0))), lbind(rbind, sfilter))(lbind(contained, TWO))))(mir_rot_f(get_arg_rank_f(sfilter_f(insert(insert(astuple(THREE, invert(astuple(TEN, TEN))), initset(astuple(TWO, invert(astuple(TEN, TEN))))), o_g(I, R3)), compose(lbind(contained, TWO), palette_f)), size, F0), R2)), remove_f(get_arg_rank_f(sfilter_f(insert(insert(astuple(THREE, invert(astuple(TEN, TEN))), initset(astuple(TWO, invert(astuple(TEN, TEN))))), o_g(I, R3)), compose(lbind(contained, TWO), palette_f)), size, F0), sfilter_f(insert(insert(astuple(THREE, invert(astuple(TEN, TEN))), initset(astuple(TWO, invert(astuple(TEN, TEN))))), o_g(I, R3)), compose(lbind(contained, TWO), palette_f)))), mapply(chain(rbind(compose, center), lbind(lbind, shift), fork(shift, identity, compose(lbind(compose, compose(invert, rbind(corner, R0))), lbind(rbind, sfilter))(lbind(contained, THREE))))(get_arg_rank_f(sfilter_f(insert(insert(astuple(THREE, invert(astuple(TEN, TEN))), initset(astuple(TWO, invert(astuple(TEN, TEN))))), o_g(I, R3)), compose(lbind(contained, THREE), palette_f)), size, F0)), remove_f(get_arg_rank_f(sfilter_f(insert(insert(astuple(THREE, invert(astuple(TEN, TEN))), initset(astuple(TWO, invert(astuple(TEN, TEN))))), o_g(I, R3)), compose(lbind(contained, THREE), palette_f)), size, F0), sfilter_f(insert(insert(astuple(THREE, invert(astuple(TEN, TEN))), initset(astuple(TWO, invert(astuple(TEN, TEN))))), o_g(I, R3)), compose(lbind(contained, THREE), palette_f))))))


def solve_3e980e27(S, I, x=0):
    x1 = rbind(compose, center)
    if x == 1:
        return x1
    x2 = lbind(lbind, shift)
    if x == 2:
        return x2
    x3 = rbind(corner, R0)
    if x == 3:
        return x3
    x4 = compose(invert, x3)
    if x == 4:
        return x4
    x5 = lbind(compose, x4)
    if x == 5:
        return x5
    x6 = lbind(rbind, sfilter)
    if x == 6:
        return x6
    x7 = compose(x5, x6)
    if x == 7:
        return x7
    x8 = lbind(contained, TWO)
    if x == 8:
        return x8
    x9 = x7(x8)
    if x == 9:
        return x9
    x10 = fork(shift, identity, x9)
    if x == 10:
        return x10
    x11 = chain(x1, x2, x10)
    if x == 11:
        return x11
    x12 = astuple(TEN, TEN)
    if x == 12:
        return x12
    x13 = invert(x12)
    if x == 13:
        return x13
    x14 = astuple(THREE, x13)
    if x == 14:
        return x14
    x15 = astuple(TWO, x13)
    if x == 15:
        return x15
    x16 = initset(x15)
    if x == 16:
        return x16
    x17 = insert(x14, x16)
    if x == 17:
        return x17
    x18 = o_g(I, R3)
    if x == 18:
        return x18
    x19 = insert(x17, x18)
    if x == 19:
        return x19
    x20 = compose(x8, palette_f)
    if x == 20:
        return x20
    x21 = sfilter_f(x19, x20)
    if x == 21:
        return x21
    x22 = get_arg_rank_f(x21, size, F0)
    if x == 22:
        return x22
    x23 = mir_rot_f(x22, R2)
    if x == 23:
        return x23
    x24 = x11(x23)
    if x == 24:
        return x24
    x25 = remove_f(x22, x21)
    if x == 25:
        return x25
    x26 = mapply(x24, x25)
    if x == 26:
        return x26
    x27 = lbind(contained, THREE)
    if x == 27:
        return x27
    x28 = x7(x27)
    if x == 28:
        return x28
    x29 = fork(shift, identity, x28)
    if x == 29:
        return x29
    x30 = chain(x1, x2, x29)
    if x == 30:
        return x30
    x31 = compose(x27, palette_f)
    if x == 31:
        return x31
    x32 = sfilter_f(x19, x31)
    if x == 32:
        return x32
    x33 = get_arg_rank_f(x32, size, F0)
    if x == 33:
        return x33
    x34 = x30(x33)
    if x == 34:
        return x34
    x35 = remove_f(x33, x32)
    if x == 35:
        return x35
    x36 = mapply(x34, x35)
    if x == 36:
        return x36
    x37 = combine_f(x26, x36)
    if x == 37:
        return x37
    O = paint(I, x37)
    return O

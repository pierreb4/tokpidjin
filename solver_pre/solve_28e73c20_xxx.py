def solve_28e73c20_one(S, I):
    return power(fork(vconcat, compose(lbind(hupscale, canvas(THREE, UNITY)), height_t), fork(vconcat, compose(rbind(hconcat, canvas(THREE, UNITY)), chain(lbind(hupscale, canvas(ZERO, UNITY)), decrement, height_t)), rbind(mir_rot_t, R4))), subtract(width_t(I), FOUR))(branch(even(width_t(I)), fill(upscale_t(canvas(THREE, UNITY), FOUR), ZERO, insert(astuple(TWO, TWO), insert(astuple(ONE, TWO), insert(UNITY, initset(DOWN))))), fill(hupscale(vupscale(canvas(THREE, UNITY), FIVE), THREE), ZERO, insert(astuple(THREE, ONE), insert(astuple(TWO, ONE), insert(UNITY, initset(DOWN)))))))


def solve_28e73c20(S, I, x=0):
    x1 = canvas(THREE, UNITY)
    if x == 1:
        return x1
    x2 = lbind(hupscale, x1)
    if x == 2:
        return x2
    x3 = compose(x2, height_t)
    if x == 3:
        return x3
    x4 = rbind(hconcat, x1)
    if x == 4:
        return x4
    x5 = canvas(ZERO, UNITY)
    if x == 5:
        return x5
    x6 = lbind(hupscale, x5)
    if x == 6:
        return x6
    x7 = chain(x6, decrement, height_t)
    if x == 7:
        return x7
    x8 = compose(x4, x7)
    if x == 8:
        return x8
    x9 = rbind(mir_rot_t, R4)
    if x == 9:
        return x9
    x10 = fork(vconcat, x8, x9)
    if x == 10:
        return x10
    x11 = fork(vconcat, x3, x10)
    if x == 11:
        return x11
    x12 = width_t(I)
    if x == 12:
        return x12
    x13 = subtract(x12, FOUR)
    if x == 13:
        return x13
    x14 = power(x11, x13)
    if x == 14:
        return x14
    x15 = even(x12)
    if x == 15:
        return x15
    x16 = upscale_t(x1, FOUR)
    if x == 16:
        return x16
    x17 = astuple(TWO, TWO)
    if x == 17:
        return x17
    x18 = astuple(ONE, TWO)
    if x == 18:
        return x18
    x19 = initset(DOWN)
    if x == 19:
        return x19
    x20 = insert(UNITY, x19)
    if x == 20:
        return x20
    x21 = insert(x18, x20)
    if x == 21:
        return x21
    x22 = insert(x17, x21)
    if x == 22:
        return x22
    x23 = fill(x16, ZERO, x22)
    if x == 23:
        return x23
    x24 = vupscale(x1, FIVE)
    if x == 24:
        return x24
    x25 = hupscale(x24, THREE)
    if x == 25:
        return x25
    x26 = astuple(THREE, ONE)
    if x == 26:
        return x26
    x27 = astuple(TWO, ONE)
    if x == 27:
        return x27
    x28 = insert(x27, x20)
    if x == 28:
        return x28
    x29 = insert(x26, x28)
    if x == 29:
        return x29
    x30 = fill(x25, ZERO, x29)
    if x == 30:
        return x30
    x31 = branch(x15, x23, x30)
    if x == 31:
        return x31
    O = x14(x31)
    return O

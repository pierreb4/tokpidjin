def solve_7df24a62_one(S, I):
    return fill(I, ONE, mpapply(mapply, apply(chain(lbind(lbind, shift), rbind(shift, NEG_UNITY), compose(normalize, rbind(f_ofcolor, ONE))), combine(astuple(subgrid(f_ofcolor(I, ONE), I), mir_rot_t(subgrid(f_ofcolor(I, ONE), I), R4)), astuple(mir_rot_t(subgrid(f_ofcolor(I, ONE), I), R5), mir_rot_t(subgrid(f_ofcolor(I, ONE), I), R6)))), papply(sfilter, apply(fork(product, compose(lbind(rbind(interval, ONE), ZERO), chain(increment, lbind(subtract, height_t(I)), height_f)), compose(lbind(rbind(interval, ONE), ZERO), chain(increment, lbind(subtract, width_t(I)), width_f))), apply(normalize, apply(compose(rbind(shift, corner(f_ofcolor(I, ONE), R0)), rbind(f_ofcolor, FOUR)), combine(astuple(subgrid(f_ofcolor(I, ONE), I), mir_rot_t(subgrid(f_ofcolor(I, ONE), I), R4)), astuple(mir_rot_t(subgrid(f_ofcolor(I, ONE), I), R5), mir_rot_t(subgrid(f_ofcolor(I, ONE), I), R6)))))), apply(lbind(compose, matcher(size, ZERO)), papply(compose, apply(lbind(rbind, difference), apply(lbind(difference, f_ofcolor(I, FOUR)), apply(compose(rbind(shift, corner(f_ofcolor(I, ONE), R0)), rbind(f_ofcolor, FOUR)), combine(astuple(subgrid(f_ofcolor(I, ONE), I), mir_rot_t(subgrid(f_ofcolor(I, ONE), I), R4)), astuple(mir_rot_t(subgrid(f_ofcolor(I, ONE), I), R5), mir_rot_t(subgrid(f_ofcolor(I, ONE), I), R6)))))), apply(lbind(lbind, shift), apply(normalize, apply(compose(rbind(shift, corner(f_ofcolor(I, ONE), R0)), rbind(f_ofcolor, FOUR)), combine(astuple(subgrid(f_ofcolor(I, ONE), I), mir_rot_t(subgrid(f_ofcolor(I, ONE), I), R4)), astuple(mir_rot_t(subgrid(f_ofcolor(I, ONE), I), R5), mir_rot_t(subgrid(f_ofcolor(I, ONE), I), R6)))))))))))


def solve_7df24a62(S, I, x=0):
    x1 = lbind(lbind, shift)
    if x == 1:
        return x1
    x2 = rbind(shift, NEG_UNITY)
    if x == 2:
        return x2
    x3 = rbind(f_ofcolor, ONE)
    if x == 3:
        return x3
    x4 = compose(normalize, x3)
    if x == 4:
        return x4
    x5 = chain(x1, x2, x4)
    if x == 5:
        return x5
    x6 = f_ofcolor(I, ONE)
    if x == 6:
        return x6
    x7 = subgrid(x6, I)
    if x == 7:
        return x7
    x8 = mir_rot_t(x7, R4)
    if x == 8:
        return x8
    x9 = astuple(x7, x8)
    if x == 9:
        return x9
    x10 = mir_rot_t(x7, R5)
    if x == 10:
        return x10
    x11 = mir_rot_t(x7, R6)
    if x == 11:
        return x11
    x12 = astuple(x10, x11)
    if x == 12:
        return x12
    x13 = combine(x9, x12)
    if x == 13:
        return x13
    x14 = apply(x5, x13)
    if x == 14:
        return x14
    x15 = rbind(interval, ONE)
    if x == 15:
        return x15
    x16 = lbind(x15, ZERO)
    if x == 16:
        return x16
    x17 = height_t(I)
    if x == 17:
        return x17
    x18 = lbind(subtract, x17)
    if x == 18:
        return x18
    x19 = chain(increment, x18, height_f)
    if x == 19:
        return x19
    x20 = compose(x16, x19)
    if x == 20:
        return x20
    x21 = width_t(I)
    if x == 21:
        return x21
    x22 = lbind(subtract, x21)
    if x == 22:
        return x22
    x23 = chain(increment, x22, width_f)
    if x == 23:
        return x23
    x24 = compose(x16, x23)
    if x == 24:
        return x24
    x25 = fork(product, x20, x24)
    if x == 25:
        return x25
    x26 = corner(x6, R0)
    if x == 26:
        return x26
    x27 = rbind(shift, x26)
    if x == 27:
        return x27
    x28 = rbind(f_ofcolor, FOUR)
    if x == 28:
        return x28
    x29 = compose(x27, x28)
    if x == 29:
        return x29
    x30 = apply(x29, x13)
    if x == 30:
        return x30
    x31 = apply(normalize, x30)
    if x == 31:
        return x31
    x32 = apply(x25, x31)
    if x == 32:
        return x32
    x33 = matcher(size, ZERO)
    if x == 33:
        return x33
    x34 = lbind(compose, x33)
    if x == 34:
        return x34
    x35 = lbind(rbind, difference)
    if x == 35:
        return x35
    x36 = f_ofcolor(I, FOUR)
    if x == 36:
        return x36
    x37 = lbind(difference, x36)
    if x == 37:
        return x37
    x38 = apply(x37, x30)
    if x == 38:
        return x38
    x39 = apply(x35, x38)
    if x == 39:
        return x39
    x40 = apply(x1, x31)
    if x == 40:
        return x40
    x41 = papply(compose, x39, x40)
    if x == 41:
        return x41
    x42 = apply(x34, x41)
    if x == 42:
        return x42
    x43 = papply(sfilter, x32, x42)
    if x == 43:
        return x43
    x44 = mpapply(mapply, x14, x43)
    if x == 44:
        return x44
    O = fill(I, ONE, x44)
    return O

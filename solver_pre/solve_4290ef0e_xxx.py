def solve_4290ef0e_one(S, I):
    return paint(mir_rot_t(paint(mir_rot_t(paint(mir_rot_t(paint(canvas(get_color_rank_t(I, F0), astuple(decrement(double(branch(contained(ONE, apply(size, fgpartition(I))), size_f(fgpartition(I)), increment(size_f(fgpartition(I)))))), decrement(double(branch(contained(ONE, apply(size, fgpartition(I))), size_f(fgpartition(I)), increment(size_f(fgpartition(I)))))))), mpapply(shift, apply(normalize, apply(compose(rbind(rbind(get_arg_rank, L1), centerofmass), fork(insert, rbind(mir_rot_f, R0), fork(insert, rbind(mir_rot_f, R3), fork(insert, rbind(mir_rot_f, R1), compose(initset, rbind(mir_rot_f, R2)))))), order(fgpartition(I), compose(invert, compose(fork(add, chain(fork(rbind(branch, NEG_TWO), positive, decrement), rbind(get_rank, L1), compose(lbind(remove, ZERO), fork(lbind(prapply, manhattan), identity, identity))), compose(double, rbind(rbind(get_val_rank, F0), width_f))), compose(lbind(colorfilter, o_g(I, R5)), color)))))), pair(interval(ZERO, branch(contained(ONE, apply(size, fgpartition(I))), size_f(fgpartition(I)), increment(size_f(fgpartition(I)))), ONE), interval(ZERO, branch(contained(ONE, apply(size, fgpartition(I))), size_f(fgpartition(I)), increment(size_f(fgpartition(I)))), ONE)))), R4), mpapply(shift, apply(normalize, apply(compose(rbind(rbind(get_arg_rank, L1), centerofmass), fork(insert, rbind(mir_rot_f, R0), fork(insert, rbind(mir_rot_f, R3), fork(insert, rbind(mir_rot_f, R1), compose(initset, rbind(mir_rot_f, R2)))))), order(fgpartition(I), compose(invert, compose(fork(add, chain(fork(rbind(branch, NEG_TWO), positive, decrement), rbind(get_rank, L1), compose(lbind(remove, ZERO), fork(lbind(prapply, manhattan), identity, identity))), compose(double, rbind(rbind(get_val_rank, F0), width_f))), compose(lbind(colorfilter, o_g(I, R5)), color)))))), pair(interval(ZERO, branch(contained(ONE, apply(size, fgpartition(I))), size_f(fgpartition(I)), increment(size_f(fgpartition(I)))), ONE), interval(ZERO, branch(contained(ONE, apply(size, fgpartition(I))), size_f(fgpartition(I)), increment(size_f(fgpartition(I)))), ONE)))), R4), mpapply(shift, apply(normalize, apply(compose(rbind(rbind(get_arg_rank, L1), centerofmass), fork(insert, rbind(mir_rot_f, R0), fork(insert, rbind(mir_rot_f, R3), fork(insert, rbind(mir_rot_f, R1), compose(initset, rbind(mir_rot_f, R2)))))), order(fgpartition(I), compose(invert, compose(fork(add, chain(fork(rbind(branch, NEG_TWO), positive, decrement), rbind(get_rank, L1), compose(lbind(remove, ZERO), fork(lbind(prapply, manhattan), identity, identity))), compose(double, rbind(rbind(get_val_rank, F0), width_f))), compose(lbind(colorfilter, o_g(I, R5)), color)))))), pair(interval(ZERO, branch(contained(ONE, apply(size, fgpartition(I))), size_f(fgpartition(I)), increment(size_f(fgpartition(I)))), ONE), interval(ZERO, branch(contained(ONE, apply(size, fgpartition(I))), size_f(fgpartition(I)), increment(size_f(fgpartition(I)))), ONE)))), R4), mpapply(shift, apply(normalize, apply(compose(rbind(rbind(get_arg_rank, L1), centerofmass), fork(insert, rbind(mir_rot_f, R0), fork(insert, rbind(mir_rot_f, R3), fork(insert, rbind(mir_rot_f, R1), compose(initset, rbind(mir_rot_f, R2)))))), order(fgpartition(I), compose(invert, compose(fork(add, chain(fork(rbind(branch, NEG_TWO), positive, decrement), rbind(get_rank, L1), compose(lbind(remove, ZERO), fork(lbind(prapply, manhattan), identity, identity))), compose(double, rbind(rbind(get_val_rank, F0), width_f))), compose(lbind(colorfilter, o_g(I, R5)), color)))))), pair(interval(ZERO, branch(contained(ONE, apply(size, fgpartition(I))), size_f(fgpartition(I)), increment(size_f(fgpartition(I)))), ONE), interval(ZERO, branch(contained(ONE, apply(size, fgpartition(I))), size_f(fgpartition(I)), increment(size_f(fgpartition(I)))), ONE))))


def solve_4290ef0e(S, I, x=0):
    x1 = get_color_rank_t(I, F0)
    if x == 1:
        return x1
    x2 = fgpartition(I)
    if x == 2:
        return x2
    x3 = apply(size, x2)
    if x == 3:
        return x3
    x4 = contained(ONE, x3)
    if x == 4:
        return x4
    x5 = size_f(x2)
    if x == 5:
        return x5
    x6 = increment(x5)
    if x == 6:
        return x6
    x7 = branch(x4, x5, x6)
    if x == 7:
        return x7
    x8 = double(x7)
    if x == 8:
        return x8
    x9 = decrement(x8)
    if x == 9:
        return x9
    x10 = astuple(x9, x9)
    if x == 10:
        return x10
    x11 = canvas(x1, x10)
    if x == 11:
        return x11
    x12 = rbind(get_arg_rank, L1)
    if x == 12:
        return x12
    x13 = rbind(x12, centerofmass)
    if x == 13:
        return x13
    x14 = rbind(mir_rot_f, R0)
    if x == 14:
        return x14
    x15 = rbind(mir_rot_f, R3)
    if x == 15:
        return x15
    x16 = rbind(mir_rot_f, R1)
    if x == 16:
        return x16
    x17 = rbind(mir_rot_f, R2)
    if x == 17:
        return x17
    x18 = compose(initset, x17)
    if x == 18:
        return x18
    x19 = fork(insert, x16, x18)
    if x == 19:
        return x19
    x20 = fork(insert, x15, x19)
    if x == 20:
        return x20
    x21 = fork(insert, x14, x20)
    if x == 21:
        return x21
    x22 = compose(x13, x21)
    if x == 22:
        return x22
    x23 = rbind(branch, NEG_TWO)
    if x == 23:
        return x23
    x24 = fork(x23, positive, decrement)
    if x == 24:
        return x24
    x25 = rbind(get_rank, L1)
    if x == 25:
        return x25
    x26 = lbind(remove, ZERO)
    if x == 26:
        return x26
    x27 = lbind(prapply, manhattan)
    if x == 27:
        return x27
    x28 = fork(x27, identity, identity)
    if x == 28:
        return x28
    x29 = compose(x26, x28)
    if x == 29:
        return x29
    x30 = chain(x24, x25, x29)
    if x == 30:
        return x30
    x31 = rbind(get_val_rank, F0)
    if x == 31:
        return x31
    x32 = rbind(x31, width_f)
    if x == 32:
        return x32
    x33 = compose(double, x32)
    if x == 33:
        return x33
    x34 = fork(add, x30, x33)
    if x == 34:
        return x34
    x35 = o_g(I, R5)
    if x == 35:
        return x35
    x36 = lbind(colorfilter, x35)
    if x == 36:
        return x36
    x37 = compose(x36, color)
    if x == 37:
        return x37
    x38 = compose(x34, x37)
    if x == 38:
        return x38
    x39 = compose(invert, x38)
    if x == 39:
        return x39
    x40 = order(x2, x39)
    if x == 40:
        return x40
    x41 = apply(x22, x40)
    if x == 41:
        return x41
    x42 = apply(normalize, x41)
    if x == 42:
        return x42
    x43 = interval(ZERO, x7, ONE)
    if x == 43:
        return x43
    x44 = pair(x43, x43)
    if x == 44:
        return x44
    x45 = mpapply(shift, x42, x44)
    if x == 45:
        return x45
    x46 = paint(x11, x45)
    if x == 46:
        return x46
    x47 = mir_rot_t(x46, R4)
    if x == 47:
        return x47
    x48 = paint(x47, x45)
    if x == 48:
        return x48
    x49 = mir_rot_t(x48, R4)
    if x == 49:
        return x49
    x50 = paint(x49, x45)
    if x == 50:
        return x50
    x51 = mir_rot_t(x50, R4)
    if x == 51:
        return x51
    O = paint(x51, x45)
    return O

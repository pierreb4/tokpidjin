def solve_97a05b5b_one(S, I):
    return paint(paint(subgrid(get_arg_rank_f(o_g(I, R3), size, F0), I), mapply(fork(mapply, compose(lbind(lbind, shift), normalize), fork(apply, chain(compose(lbind(rbind, subtract), rbind(corner, R0)), fork(combine, compose(lbind(recolor_o, ZERO), rbind(sfilter, compose(flip, matcher(rbind(get_nth_f, F0), TWO)))), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), normalize), fork(sfilter, compose(rbind(sfilter, chain(compose(positive, size), lbind(sfilter, apply(toindices, o_g(switch(subgrid(get_arg_rank_f(o_g(I, R3), size, F0), I), TWO, ZERO), R7))), lbind(lbind, contained))), chain(lbind(occurrences, switch(subgrid(get_arg_rank_f(o_g(I, R3), size, F0), I), TWO, ZERO)), fork(combine, compose(lbind(recolor_o, ZERO), rbind(sfilter, compose(flip, matcher(rbind(get_nth_f, F0), TWO)))), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), normalize)), chain(rbind(compose, compose(chain(size, rbind(get_nth_f, F0), lbind(sfilter, apply(toindices, o_g(switch(subgrid(get_arg_rank_f(o_g(I, R3), size, F0), I), TWO, ZERO), R7)))), lbind(lbind, contained))), lbind(rbind, equality), rbind(colorcount_f, TWO))))), mapply(lbind(rapply, apply(fork(compose, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), product(combine(astuple(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1)), astuple(rbind(mir_rot_f, R0), rbind(mir_rot_f, R2))), combine(astuple(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1)), astuple(rbind(mir_rot_f, R0), rbind(mir_rot_f, R2)))))), sfilter_f(o_g(I, R3), compose(rbind(greater, ONE), numcolors_f))))), mapply(fork(mapply, compose(lbind(lbind, shift), normalize), fork(apply, chain(compose(lbind(rbind, subtract), rbind(corner, R0)), fork(combine, compose(lbind(recolor_o, ZERO), rbind(sfilter, compose(flip, matcher(rbind(get_nth_f, F0), TWO)))), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), normalize), chain(lbind(occurrences, switch(subgrid(get_arg_rank_f(o_g(I, R3), size, F0), I), TWO, ZERO)), fork(combine, compose(lbind(recolor_o, ZERO), rbind(sfilter, compose(flip, matcher(rbind(get_nth_f, F0), TWO)))), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), normalize))), mapply(lbind(rapply, apply(fork(compose, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), product(combine(astuple(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1)), astuple(rbind(mir_rot_f, R0), rbind(mir_rot_f, R2))), combine(astuple(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1)), astuple(rbind(mir_rot_f, R0), rbind(mir_rot_f, R2)))))), sfilter_f(sfilter_f(o_g(I, R3), compose(rbind(greater, ONE), numcolors_f)), chain(flip, rbind(contained, lbind(remove, TWO)(palette_t(mapply(fork(mapply, compose(lbind(lbind, shift), normalize), fork(apply, chain(compose(lbind(rbind, subtract), rbind(corner, R0)), fork(combine, compose(lbind(recolor_o, ZERO), rbind(sfilter, compose(flip, matcher(rbind(get_nth_f, F0), TWO)))), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), normalize), fork(sfilter, compose(rbind(sfilter, chain(compose(positive, size), lbind(sfilter, apply(toindices, o_g(switch(subgrid(get_arg_rank_f(o_g(I, R3), size, F0), I), TWO, ZERO), R7))), lbind(lbind, contained))), chain(lbind(occurrences, switch(subgrid(get_arg_rank_f(o_g(I, R3), size, F0), I), TWO, ZERO)), fork(combine, compose(lbind(recolor_o, ZERO), rbind(sfilter, compose(flip, matcher(rbind(get_nth_f, F0), TWO)))), rbind(sfilter, matcher(rbind(get_nth_f, F0), TWO))), normalize)), chain(rbind(compose, compose(chain(size, rbind(get_nth_f, F0), lbind(sfilter, apply(toindices, o_g(switch(subgrid(get_arg_rank_f(o_g(I, R3), size, F0), I), TWO, ZERO), R7)))), lbind(lbind, contained))), lbind(rbind, equality), rbind(colorcount_f, TWO))))), mapply(lbind(rapply, apply(fork(compose, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), product(combine(astuple(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1)), astuple(rbind(mir_rot_f, R0), rbind(mir_rot_f, R2))), combine(astuple(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1)), astuple(rbind(mir_rot_f, R0), rbind(mir_rot_f, R2)))))), sfilter_f(o_g(I, R3), compose(rbind(greater, ONE), numcolors_f))))))), chain(rbind(get_nth_f, F0), lbind(remove, TWO), palette_f))))))


def solve_97a05b5b(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = lbind(lbind, shift)
    if x == 4:
        return x4
    x5 = compose(x4, normalize)
    if x == 5:
        return x5
    x6 = lbind(rbind, subtract)
    if x == 6:
        return x6
    x7 = rbind(corner, R0)
    if x == 7:
        return x7
    x8 = compose(x6, x7)
    if x == 8:
        return x8
    x9 = lbind(recolor_o, ZERO)
    if x == 9:
        return x9
    x10 = rbind(get_nth_f, F0)
    if x == 10:
        return x10
    x11 = matcher(x10, TWO)
    if x == 11:
        return x11
    x12 = compose(flip, x11)
    if x == 12:
        return x12
    x13 = rbind(sfilter, x12)
    if x == 13:
        return x13
    x14 = compose(x9, x13)
    if x == 14:
        return x14
    x15 = rbind(sfilter, x11)
    if x == 15:
        return x15
    x16 = fork(combine, x14, x15)
    if x == 16:
        return x16
    x17 = chain(x8, x16, normalize)
    if x == 17:
        return x17
    x18 = compose(positive, size)
    if x == 18:
        return x18
    x19 = switch(x3, TWO, ZERO)
    if x == 19:
        return x19
    x20 = o_g(x19, R7)
    if x == 20:
        return x20
    x21 = apply(toindices, x20)
    if x == 21:
        return x21
    x22 = lbind(sfilter, x21)
    if x == 22:
        return x22
    x23 = lbind(lbind, contained)
    if x == 23:
        return x23
    x24 = chain(x18, x22, x23)
    if x == 24:
        return x24
    x25 = rbind(sfilter, x24)
    if x == 25:
        return x25
    x26 = lbind(occurrences, x19)
    if x == 26:
        return x26
    x27 = chain(x26, x16, normalize)
    if x == 27:
        return x27
    x28 = compose(x25, x27)
    if x == 28:
        return x28
    x29 = chain(size, x10, x22)
    if x == 29:
        return x29
    x30 = compose(x29, x23)
    if x == 30:
        return x30
    x31 = rbind(compose, x30)
    if x == 31:
        return x31
    x32 = lbind(rbind, equality)
    if x == 32:
        return x32
    x33 = rbind(colorcount_f, TWO)
    if x == 33:
        return x33
    x34 = chain(x31, x32, x33)
    if x == 34:
        return x34
    x35 = fork(sfilter, x28, x34)
    if x == 35:
        return x35
    x36 = fork(apply, x17, x35)
    if x == 36:
        return x36
    x37 = fork(mapply, x5, x36)
    if x == 37:
        return x37
    x38 = rbind(get_nth_f, L1)
    if x == 38:
        return x38
    x39 = fork(compose, x10, x38)
    if x == 39:
        return x39
    x40 = rbind(mir_rot_f, R3)
    if x == 40:
        return x40
    x41 = rbind(mir_rot_f, R1)
    if x == 41:
        return x41
    x42 = astuple(x40, x41)
    if x == 42:
        return x42
    x43 = rbind(mir_rot_f, R0)
    if x == 43:
        return x43
    x44 = rbind(mir_rot_f, R2)
    if x == 44:
        return x44
    x45 = astuple(x43, x44)
    if x == 45:
        return x45
    x46 = combine(x42, x45)
    if x == 46:
        return x46
    x47 = product(x46, x46)
    if x == 47:
        return x47
    x48 = apply(x39, x47)
    if x == 48:
        return x48
    x49 = lbind(rapply, x48)
    if x == 49:
        return x49
    x50 = rbind(greater, ONE)
    if x == 50:
        return x50
    x51 = compose(x50, numcolors_f)
    if x == 51:
        return x51
    x52 = sfilter_f(x1, x51)
    if x == 52:
        return x52
    x53 = mapply(x49, x52)
    if x == 53:
        return x53
    x54 = mapply(x37, x53)
    if x == 54:
        return x54
    x55 = paint(x3, x54)
    if x == 55:
        return x55
    x56 = fork(apply, x17, x27)
    if x == 56:
        return x56
    x57 = fork(mapply, x5, x56)
    if x == 57:
        return x57
    x58 = lbind(remove, TWO)
    if x == 58:
        return x58
    x59 = palette_t(x54)
    if x == 59:
        return x59
    x60 = x58(x59)
    if x == 60:
        return x60
    x61 = rbind(contained, x60)
    if x == 61:
        return x61
    x62 = chain(x10, x58, palette_f)
    if x == 62:
        return x62
    x63 = chain(flip, x61, x62)
    if x == 63:
        return x63
    x64 = sfilter_f(x52, x63)
    if x == 64:
        return x64
    x65 = mapply(x49, x64)
    if x == 65:
        return x65
    x66 = mapply(x57, x65)
    if x == 66:
        return x66
    O = paint(x55, x66)
    return O

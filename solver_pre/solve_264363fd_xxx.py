def solve_264363fd_one(S, I):
    return fill(paint(paint(cover(I, get_arg_rank_f(o_g(I, R1), size, L1)), mapply(fork(shift, compose(asobject, fork(paint, rbind(subgrid, cover(I, get_arg_rank_f(o_g(I, R1), size, L1))), compose(lbind(recolor_i, index(I, add(branch(equality(height_f(get_arg_rank_f(o_g(I, R1), size, L1)), FIVE), UP, RIGHT), center(get_arg_rank_f(o_g(I, R1), size, L1))))), fork(combine, branch(equality(height_f(get_arg_rank_f(o_g(I, R1), size, L1)), FIVE), compose(lbind(mapply, vfrontier), compose(rbind(occurrences, initset(astuple(index(I, center(get_arg_rank_f(o_g(I, R1), size, L1))), ORIGIN))), rbind(subgrid, cover(I, get_arg_rank_f(o_g(I, R1), size, L1))))), compose(lbind(mapply, hfrontier), compose(rbind(occurrences, initset(astuple(index(I, center(get_arg_rank_f(o_g(I, R1), size, L1))), ORIGIN))), rbind(subgrid, cover(I, get_arg_rank_f(o_g(I, R1), size, L1)))))), branch(equality(width_f(get_arg_rank_f(o_g(I, R1), size, L1)), FIVE), compose(lbind(mapply, hfrontier), compose(rbind(occurrences, initset(astuple(index(I, center(get_arg_rank_f(o_g(I, R1), size, L1))), ORIGIN))), rbind(subgrid, cover(I, get_arg_rank_f(o_g(I, R1), size, L1))))), compose(lbind(mapply, vfrontier), compose(rbind(occurrences, initset(astuple(index(I, center(get_arg_rank_f(o_g(I, R1), size, L1))), ORIGIN))), rbind(subgrid, cover(I, get_arg_rank_f(o_g(I, R1), size, L1)))))))))), rbind(corner, R0)), o_g(cover(I, get_arg_rank_f(o_g(I, R1), size, L1)), R1))), mapply(lbind(shift, shift(normalize(get_arg_rank_f(o_g(I, R1), size, L1)), invert(add(UNITY, astuple(equality(height_f(get_arg_rank_f(o_g(I, R1), size, L1)), FIVE), equality(width_f(get_arg_rank_f(o_g(I, R1), size, L1)), FIVE)))))), occurrences(cover(I, get_arg_rank_f(o_g(I, R1), size, L1)), initset(astuple(index(I, center(get_arg_rank_f(o_g(I, R1), size, L1))), ORIGIN))))), get_color_rank_t(cover(I, get_arg_rank_f(o_g(I, R1), size, L1)), F0), f_ofcolor(cover(I, get_arg_rank_f(o_g(I, R1), size, L1)), get_color_rank_t(cover(I, get_arg_rank_f(o_g(I, R1), size, L1)), F0)))


def solve_264363fd(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, L1)
    if x == 2:
        return x2
    x3 = cover(I, x2)
    if x == 3:
        return x3
    x4 = rbind(subgrid, x3)
    if x == 4:
        return x4
    x5 = height_f(x2)
    if x == 5:
        return x5
    x6 = equality(x5, FIVE)
    if x == 6:
        return x6
    x7 = branch(x6, UP, RIGHT)
    if x == 7:
        return x7
    x8 = center(x2)
    if x == 8:
        return x8
    x9 = add(x7, x8)
    if x == 9:
        return x9
    x10 = index(I, x9)
    if x == 10:
        return x10
    x11 = lbind(recolor_i, x10)
    if x == 11:
        return x11
    x12 = lbind(mapply, vfrontier)
    if x == 12:
        return x12
    x13 = index(I, x8)
    if x == 13:
        return x13
    x14 = astuple(x13, ORIGIN)
    if x == 14:
        return x14
    x15 = initset(x14)
    if x == 15:
        return x15
    x16 = rbind(occurrences, x15)
    if x == 16:
        return x16
    x17 = compose(x16, x4)
    if x == 17:
        return x17
    x18 = compose(x12, x17)
    if x == 18:
        return x18
    x19 = lbind(mapply, hfrontier)
    if x == 19:
        return x19
    x20 = compose(x19, x17)
    if x == 20:
        return x20
    x21 = branch(x6, x18, x20)
    if x == 21:
        return x21
    x22 = width_f(x2)
    if x == 22:
        return x22
    x23 = equality(x22, FIVE)
    if x == 23:
        return x23
    x24 = branch(x23, x20, x18)
    if x == 24:
        return x24
    x25 = fork(combine, x21, x24)
    if x == 25:
        return x25
    x26 = compose(x11, x25)
    if x == 26:
        return x26
    x27 = fork(paint, x4, x26)
    if x == 27:
        return x27
    x28 = compose(asobject, x27)
    if x == 28:
        return x28
    x29 = rbind(corner, R0)
    if x == 29:
        return x29
    x30 = fork(shift, x28, x29)
    if x == 30:
        return x30
    x31 = o_g(x3, R1)
    if x == 31:
        return x31
    x32 = mapply(x30, x31)
    if x == 32:
        return x32
    x33 = paint(x3, x32)
    if x == 33:
        return x33
    x34 = normalize(x2)
    if x == 34:
        return x34
    x35 = astuple(x6, x23)
    if x == 35:
        return x35
    x36 = add(UNITY, x35)
    if x == 36:
        return x36
    x37 = invert(x36)
    if x == 37:
        return x37
    x38 = shift(x34, x37)
    if x == 38:
        return x38
    x39 = lbind(shift, x38)
    if x == 39:
        return x39
    x40 = occurrences(x3, x15)
    if x == 40:
        return x40
    x41 = mapply(x39, x40)
    if x == 41:
        return x41
    x42 = paint(x33, x41)
    if x == 42:
        return x42
    x43 = get_color_rank_t(x3, F0)
    if x == 43:
        return x43
    x44 = f_ofcolor(x3, x43)
    if x == 44:
        return x44
    O = fill(x42, x43, x44)
    return O

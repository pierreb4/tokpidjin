def solve_99fa7670_one(S, I):
    return underpaint(paint(I, mapply(fork(recolor_i, color, compose(rbind(shoot, RIGHT), center)), o_g(I, R5))), mapply(fork(recolor_i, compose(color, rbind(get_nth_f, F0)), fork(connect, compose(rbind(corner, R3), rbind(get_nth_f, F0)), compose(rbind(corner, R3), rbind(get_nth_f, L1)))), pair(remove_f(recolor_i(BLACK, initset(add(shape_t(I), DOWN_LEFT))), order(insert(recolor_i(BLACK, initset(add(shape_t(I), DOWN_LEFT))), o_g(paint(I, mapply(fork(recolor_i, color, compose(rbind(shoot, RIGHT), center)), o_g(I, R5))), R5)), rbind(col_row, R1))), remove_f(get_nth_t(order(insert(recolor_i(BLACK, initset(add(shape_t(I), DOWN_LEFT))), o_g(paint(I, mapply(fork(recolor_i, color, compose(rbind(shoot, RIGHT), center)), o_g(I, R5))), R5)), rbind(col_row, R1)), F0), order(insert(recolor_i(BLACK, initset(add(shape_t(I), DOWN_LEFT))), o_g(paint(I, mapply(fork(recolor_i, color, compose(rbind(shoot, RIGHT), center)), o_g(I, R5))), R5)), rbind(col_row, R1))))))


def solve_99fa7670(S, I, x=0):
    x1 = rbind(shoot, RIGHT)
    if x == 1:
        return x1
    x2 = compose(x1, center)
    if x == 2:
        return x2
    x3 = fork(recolor_i, color, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R5)
    if x == 4:
        return x4
    x5 = mapply(x3, x4)
    if x == 5:
        return x5
    x6 = paint(I, x5)
    if x == 6:
        return x6
    x7 = rbind(get_nth_f, F0)
    if x == 7:
        return x7
    x8 = compose(color, x7)
    if x == 8:
        return x8
    x9 = rbind(corner, R3)
    if x == 9:
        return x9
    x10 = compose(x9, x7)
    if x == 10:
        return x10
    x11 = rbind(get_nth_f, L1)
    if x == 11:
        return x11
    x12 = compose(x9, x11)
    if x == 12:
        return x12
    x13 = fork(connect, x10, x12)
    if x == 13:
        return x13
    x14 = fork(recolor_i, x8, x13)
    if x == 14:
        return x14
    x15 = shape_t(I)
    if x == 15:
        return x15
    x16 = add(x15, DOWN_LEFT)
    if x == 16:
        return x16
    x17 = initset(x16)
    if x == 17:
        return x17
    x18 = recolor_i(BLACK, x17)
    if x == 18:
        return x18
    x19 = o_g(x6, R5)
    if x == 19:
        return x19
    x20 = insert(x18, x19)
    if x == 20:
        return x20
    x21 = rbind(col_row, R1)
    if x == 21:
        return x21
    x22 = order(x20, x21)
    if x == 22:
        return x22
    x23 = remove_f(x18, x22)
    if x == 23:
        return x23
    x24 = get_nth_t(x22, F0)
    if x == 24:
        return x24
    x25 = remove_f(x24, x22)
    if x == 25:
        return x25
    x26 = pair(x23, x25)
    if x == 26:
        return x26
    x27 = mapply(x14, x26)
    if x == 27:
        return x27
    O = underpaint(x6, x27)
    return O

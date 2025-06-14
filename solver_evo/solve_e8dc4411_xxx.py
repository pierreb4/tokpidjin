def solve_e8dc4411_one(S, I):
    return fill(I, get_color_rank_t(I, L1), mapply(lbind(shift, f_ofcolor(I, BLACK)), apply(lbind(multiply, apply(branch(equality(fork(connect, rbind(corner, R0), rbind(corner, R3))(f_ofcolor(I, BLACK)), intersection(f_ofcolor(I, BLACK), fork(connect, rbind(corner, R0), rbind(corner, R3))(f_ofcolor(I, BLACK)))), identity, fork(add, identity, fork(subtract, identity, crement))), multiply(shape_f(f_ofcolor(I, BLACK)), position(f_ofcolor(I, BLACK), f_ofcolor(I, get_color_rank_t(I, L1)))))), interval(ONE, FIVE, ONE))))


def solve_e8dc4411(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, BLACK)
    if x == 2:
        return x2
    x3 = lbind(shift, x2)
    if x == 3:
        return x3
    x4 = rbind(corner, R0)
    if x == 4:
        return x4
    x5 = rbind(corner, R3)
    if x == 5:
        return x5
    x6 = fork(connect, x4, x5)
    if x == 6:
        return x6
    x7 = x6(x2)
    if x == 7:
        return x7
    x8 = intersection(x2, x7)
    if x == 8:
        return x8
    x9 = equality(x7, x8)
    if x == 9:
        return x9
    x10 = fork(subtract, identity, crement)
    if x == 10:
        return x10
    x11 = fork(add, identity, x10)
    if x == 11:
        return x11
    x12 = branch(x9, identity, x11)
    if x == 12:
        return x12
    x13 = shape_f(x2)
    if x == 13:
        return x13
    x14 = f_ofcolor(I, x1)
    if x == 14:
        return x14
    x15 = position(x2, x14)
    if x == 15:
        return x15
    x16 = multiply(x13, x15)
    if x == 16:
        return x16
    x17 = apply(x12, x16)
    if x == 17:
        return x17
    x18 = lbind(multiply, x17)
    if x == 18:
        return x18
    x19 = interval(ONE, FIVE, ONE)
    if x == 19:
        return x19
    x20 = apply(x18, x19)
    if x == 20:
        return x20
    x21 = mapply(x3, x20)
    if x == 21:
        return x21
    O = fill(I, x1, x21)
    return O

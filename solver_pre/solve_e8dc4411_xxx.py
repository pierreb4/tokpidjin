def solve_e8dc4411_one(S, I):
    return fill(I, get_color_rank_t(I, L1), mapply(lbind(shift, f_ofcolor(I, ZERO)), apply(lbind(multiply, apply(branch(equality(fork(connect, rbind(corner, R0), rbind(corner, R3))(f_ofcolor(I, ZERO)), intersection(f_ofcolor(I, ZERO), fork(connect, rbind(corner, R0), rbind(corner, R3))(f_ofcolor(I, ZERO)))), identity, fork(add, identity, fork(subtract, identity, crement))), multiply(shape_f(f_ofcolor(I, ZERO)), position(f_ofcolor(I, ZERO), f_ofcolor(I, get_color_rank_t(I, L1)))))), interval(ONE, FIVE, ONE))))


def solve_e8dc4411(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = f_ofcolor(I, ZERO)
    x3 = lbind(shift, x2)
    x4 = rbind(corner, R0)
    x5 = rbind(corner, R3)
    x6 = fork(connect, x4, x5)
    x7 = x6(x2)
    x8 = intersection(x2, x7)
    x9 = equality(x7, x8)
    x10 = fork(subtract, identity, crement)
    x11 = fork(add, identity, x10)
    x12 = branch(x9, identity, x11)
    x13 = shape_f(x2)
    x14 = f_ofcolor(I, x1)
    x15 = position(x2, x14)
    x16 = multiply(x13, x15)
    x17 = apply(x12, x16)
    x18 = lbind(multiply, x17)
    x19 = interval(ONE, FIVE, ONE)
    x20 = apply(x18, x19)
    x21 = mapply(x3, x20)
    O = fill(I, x1, x21)
    return O

def solve_f15e1fac_one(S, I):
    return chain(branch(portrait_f(f_ofcolor(I, RED)), identity, rbind(mir_rot_t, R1)), branch(equality(col_row(f_ofcolor(I, RED), R2), BLACK), identity, rbind(mir_rot_t, R2)), branch(equality(col_row(f_ofcolor(branch(equality(col_row(f_ofcolor(I, RED), R2), BLACK), identity, rbind(mir_rot_t, R2))(branch(portrait_f(f_ofcolor(I, RED)), identity, rbind(mir_rot_t, R1))(I)), CYAN), R1), BLACK), identity, rbind(mir_rot_t, R0)))(fill(branch(equality(col_row(f_ofcolor(branch(equality(col_row(f_ofcolor(I, RED), R2), BLACK), identity, rbind(mir_rot_t, R2))(branch(portrait_f(f_ofcolor(I, RED)), identity, rbind(mir_rot_t, R1))(I)), CYAN), R1), BLACK), identity, rbind(mir_rot_t, R0))(branch(equality(col_row(f_ofcolor(I, RED), R2), BLACK), identity, rbind(mir_rot_t, R2))(branch(portrait_f(f_ofcolor(I, RED)), identity, rbind(mir_rot_t, R1))(I))), CYAN, merge(papply(shift, apply(chain(lbind(sfilter, mapply(rbind(shoot, DOWN), f_ofcolor(branch(equality(col_row(f_ofcolor(branch(equality(col_row(f_ofcolor(I, RED), R2), BLACK), identity, rbind(mir_rot_t, R2))(branch(portrait_f(f_ofcolor(I, RED)), identity, rbind(mir_rot_t, R1))(I)), CYAN), R1), BLACK), identity, rbind(mir_rot_t, R0))(branch(equality(col_row(f_ofcolor(I, RED), R2), BLACK), identity, rbind(mir_rot_t, R2))(branch(portrait_f(f_ofcolor(I, RED)), identity, rbind(mir_rot_t, R1))(I))), CYAN))), lbind(compose, fork(both, fork(greater, compose(rbind(get_nth_f, F0), rbind(get_nth_f, L1)), chain(decrement, rbind(get_nth_f, F0), rbind(get_nth_f, F0))), fork(greater, chain(increment, rbind(get_nth_f, L1), rbind(get_nth_f, F0)), compose(rbind(get_nth_f, F0), rbind(get_nth_f, L1))))), lbind(lbind, astuple)), pair(order(insert(BLACK, apply(rbind(get_nth_f, F0), f_ofcolor(branch(equality(col_row(f_ofcolor(branch(equality(col_row(f_ofcolor(I, RED), R2), BLACK), identity, rbind(mir_rot_t, R2))(branch(portrait_f(f_ofcolor(I, RED)), identity, rbind(mir_rot_t, R1))(I)), CYAN), R1), BLACK), identity, rbind(mir_rot_t, R0))(branch(equality(col_row(f_ofcolor(I, RED), R2), BLACK), identity, rbind(mir_rot_t, R2))(branch(portrait_f(f_ofcolor(I, RED)), identity, rbind(mir_rot_t, R1))(I))), RED))), identity), order(apply(decrement, insert(height_t(branch(equality(col_row(f_ofcolor(branch(equality(col_row(f_ofcolor(I, RED), R2), BLACK), identity, rbind(mir_rot_t, R2))(branch(portrait_f(f_ofcolor(I, RED)), identity, rbind(mir_rot_t, R1))(I)), CYAN), R1), BLACK), identity, rbind(mir_rot_t, R0))(branch(equality(col_row(f_ofcolor(I, RED), R2), BLACK), identity, rbind(mir_rot_t, R2))(branch(portrait_f(f_ofcolor(I, RED)), identity, rbind(mir_rot_t, R1))(I)))), apply(rbind(get_nth_f, F0), f_ofcolor(branch(equality(col_row(f_ofcolor(branch(equality(col_row(f_ofcolor(I, RED), R2), BLACK), identity, rbind(mir_rot_t, R2))(branch(portrait_f(f_ofcolor(I, RED)), identity, rbind(mir_rot_t, R1))(I)), CYAN), R1), BLACK), identity, rbind(mir_rot_t, R0))(branch(equality(col_row(f_ofcolor(I, RED), R2), BLACK), identity, rbind(mir_rot_t, R2))(branch(portrait_f(f_ofcolor(I, RED)), identity, rbind(mir_rot_t, R1))(I))), RED)))), identity))), apply(tojvec, interval(ZERO, increment(size_f(f_ofcolor(branch(equality(col_row(f_ofcolor(branch(equality(col_row(f_ofcolor(I, RED), R2), BLACK), identity, rbind(mir_rot_t, R2))(branch(portrait_f(f_ofcolor(I, RED)), identity, rbind(mir_rot_t, R1))(I)), CYAN), R1), BLACK), identity, rbind(mir_rot_t, R0))(branch(equality(col_row(f_ofcolor(I, RED), R2), BLACK), identity, rbind(mir_rot_t, R2))(branch(portrait_f(f_ofcolor(I, RED)), identity, rbind(mir_rot_t, R1))(I))), RED))), ONE))))))


def solve_f15e1fac(S, I, x=0):
    x1 = f_ofcolor(I, RED)
    if x == 1:
        return x1
    x2 = portrait_f(x1)
    if x == 2:
        return x2
    x3 = rbind(mir_rot_t, R1)
    if x == 3:
        return x3
    x4 = branch(x2, identity, x3)
    if x == 4:
        return x4
    x5 = col_row(x1, R2)
    if x == 5:
        return x5
    x6 = equality(x5, BLACK)
    if x == 6:
        return x6
    x7 = rbind(mir_rot_t, R2)
    if x == 7:
        return x7
    x8 = branch(x6, identity, x7)
    if x == 8:
        return x8
    x9 = x4(I)
    if x == 9:
        return x9
    x10 = x8(x9)
    if x == 10:
        return x10
    x11 = f_ofcolor(x10, CYAN)
    if x == 11:
        return x11
    x12 = col_row(x11, R1)
    if x == 12:
        return x12
    x13 = equality(x12, BLACK)
    if x == 13:
        return x13
    x14 = rbind(mir_rot_t, R0)
    if x == 14:
        return x14
    x15 = branch(x13, identity, x14)
    if x == 15:
        return x15
    x16 = chain(x4, x8, x15)
    if x == 16:
        return x16
    x17 = x15(x10)
    if x == 17:
        return x17
    x18 = rbind(shoot, DOWN)
    if x == 18:
        return x18
    x19 = f_ofcolor(x17, CYAN)
    if x == 19:
        return x19
    x20 = mapply(x18, x19)
    if x == 20:
        return x20
    x21 = lbind(sfilter, x20)
    if x == 21:
        return x21
    x22 = rbind(get_nth_f, F0)
    if x == 22:
        return x22
    x23 = rbind(get_nth_f, L1)
    if x == 23:
        return x23
    x24 = compose(x22, x23)
    if x == 24:
        return x24
    x25 = chain(decrement, x22, x22)
    if x == 25:
        return x25
    x26 = fork(greater, x24, x25)
    if x == 26:
        return x26
    x27 = chain(increment, x23, x22)
    if x == 27:
        return x27
    x28 = fork(greater, x27, x24)
    if x == 28:
        return x28
    x29 = fork(both, x26, x28)
    if x == 29:
        return x29
    x30 = lbind(compose, x29)
    if x == 30:
        return x30
    x31 = lbind(lbind, astuple)
    if x == 31:
        return x31
    x32 = chain(x21, x30, x31)
    if x == 32:
        return x32
    x33 = f_ofcolor(x17, RED)
    if x == 33:
        return x33
    x34 = apply(x22, x33)
    if x == 34:
        return x34
    x35 = insert(BLACK, x34)
    if x == 35:
        return x35
    x36 = order(x35, identity)
    if x == 36:
        return x36
    x37 = height_t(x17)
    if x == 37:
        return x37
    x38 = insert(x37, x34)
    if x == 38:
        return x38
    x39 = apply(decrement, x38)
    if x == 39:
        return x39
    x40 = order(x39, identity)
    if x == 40:
        return x40
    x41 = pair(x36, x40)
    if x == 41:
        return x41
    x42 = apply(x32, x41)
    if x == 42:
        return x42
    x43 = size_f(x33)
    if x == 43:
        return x43
    x44 = increment(x43)
    if x == 44:
        return x44
    x45 = interval(ZERO, x44, ONE)
    if x == 45:
        return x45
    x46 = apply(tojvec, x45)
    if x == 46:
        return x46
    x47 = papply(shift, x42, x46)
    if x == 47:
        return x47
    x48 = merge(x47)
    if x == 48:
        return x48
    x49 = fill(x17, CYAN, x48)
    if x == 49:
        return x49
    O = x16(x49)
    return O

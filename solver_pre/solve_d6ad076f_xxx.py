def solve_d6ad076f_one(S, I):
    return cover(underfill(I, EIGHT, mapply(rbind(shoot, multiply(branch(vmatching(get_arg_rank_f(o_g(I, R5), size, L1), get_arg_rank_f(o_g(I, R5), size, F0)), DOWN, RIGHT), branch(equality(get_val_rank_f(o_g(I, R5), branch(vmatching(get_arg_rank_f(o_g(I, R5), size, L1), get_arg_rank_f(o_g(I, R5), size, F0)), rbind(col_row, R1), rbind(col_row, R2)), F0), branch(vmatching(get_arg_rank_f(o_g(I, R5), size, L1), get_arg_rank_f(o_g(I, R5), size, F0)), rbind(col_row, R1), rbind(col_row, R2))(get_arg_rank_f(o_g(I, R5), size, L1))), NEG_ONE, ONE))), inbox(get_arg_rank_f(o_g(I, R5), size, L1)))), mfilter_f(colorfilter(o_g(underfill(I, EIGHT, mapply(rbind(shoot, multiply(branch(vmatching(get_arg_rank_f(o_g(I, R5), size, L1), get_arg_rank_f(o_g(I, R5), size, F0)), DOWN, RIGHT), branch(equality(get_val_rank_f(o_g(I, R5), branch(vmatching(get_arg_rank_f(o_g(I, R5), size, L1), get_arg_rank_f(o_g(I, R5), size, F0)), rbind(col_row, R1), rbind(col_row, R2)), F0), branch(vmatching(get_arg_rank_f(o_g(I, R5), size, L1), get_arg_rank_f(o_g(I, R5), size, F0)), rbind(col_row, R1), rbind(col_row, R2))(get_arg_rank_f(o_g(I, R5), size, L1))), NEG_ONE, ONE))), inbox(get_arg_rank_f(o_g(I, R5), size, L1)))), R5), EIGHT), rbind(bordering, I)))


def solve_d6ad076f(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, L1)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x1, size, F0)
    if x == 3:
        return x3
    x4 = vmatching(x2, x3)
    if x == 4:
        return x4
    x5 = branch(x4, DOWN, RIGHT)
    if x == 5:
        return x5
    x6 = rbind(col_row, R1)
    if x == 6:
        return x6
    x7 = rbind(col_row, R2)
    if x == 7:
        return x7
    x8 = branch(x4, x6, x7)
    if x == 8:
        return x8
    x9 = get_val_rank_f(x1, x8, F0)
    if x == 9:
        return x9
    x10 = x8(x2)
    if x == 10:
        return x10
    x11 = equality(x9, x10)
    if x == 11:
        return x11
    x12 = branch(x11, NEG_ONE, ONE)
    if x == 12:
        return x12
    x13 = multiply(x5, x12)
    if x == 13:
        return x13
    x14 = rbind(shoot, x13)
    if x == 14:
        return x14
    x15 = inbox(x2)
    if x == 15:
        return x15
    x16 = mapply(x14, x15)
    if x == 16:
        return x16
    x17 = underfill(I, EIGHT, x16)
    if x == 17:
        return x17
    x18 = o_g(x17, R5)
    if x == 18:
        return x18
    x19 = colorfilter(x18, EIGHT)
    if x == 19:
        return x19
    x20 = rbind(bordering, I)
    if x == 20:
        return x20
    x21 = mfilter_f(x19, x20)
    if x == 21:
        return x21
    O = cover(x17, x21)
    return O

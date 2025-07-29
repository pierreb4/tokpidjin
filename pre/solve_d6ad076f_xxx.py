def solve_d6ad076f_one(S, I):
    return cover(underfill(I, EIGHT, mapply(rbind(shoot, multiply(branch(vmatching(get_arg_rank_f(o_g(I, R5), size, L1), get_arg_rank_f(o_g(I, R5), size, F0)), DOWN, RIGHT), branch(equality(get_val_rank_f(o_g(I, R5), branch(vmatching(get_arg_rank_f(o_g(I, R5), size, L1), get_arg_rank_f(o_g(I, R5), size, F0)), rbind(col_row, R1), rbind(col_row, R2)), F0), branch(vmatching(get_arg_rank_f(o_g(I, R5), size, L1), get_arg_rank_f(o_g(I, R5), size, F0)), rbind(col_row, R1), rbind(col_row, R2))(get_arg_rank_f(o_g(I, R5), size, L1))), NEG_ONE, ONE))), inbox(get_arg_rank_f(o_g(I, R5), size, L1)))), mfilter_f(colorfilter(o_g(underfill(I, EIGHT, mapply(rbind(shoot, multiply(branch(vmatching(get_arg_rank_f(o_g(I, R5), size, L1), get_arg_rank_f(o_g(I, R5), size, F0)), DOWN, RIGHT), branch(equality(get_val_rank_f(o_g(I, R5), branch(vmatching(get_arg_rank_f(o_g(I, R5), size, L1), get_arg_rank_f(o_g(I, R5), size, F0)), rbind(col_row, R1), rbind(col_row, R2)), F0), branch(vmatching(get_arg_rank_f(o_g(I, R5), size, L1), get_arg_rank_f(o_g(I, R5), size, F0)), rbind(col_row, R1), rbind(col_row, R2))(get_arg_rank_f(o_g(I, R5), size, L1))), NEG_ONE, ONE))), inbox(get_arg_rank_f(o_g(I, R5), size, L1)))), R5), EIGHT), rbind(bordering, I)))


def solve_d6ad076f(S, I):
    x1 = o_g(I, R5)
    x2 = get_arg_rank_f(x1, size, L1)
    x3 = get_arg_rank_f(x1, size, F0)
    x4 = vmatching(x2, x3)
    x5 = branch(x4, DOWN, RIGHT)
    x6 = rbind(col_row, R1)
    x7 = rbind(col_row, R2)
    x8 = branch(x4, x6, x7)
    x9 = get_val_rank_f(x1, x8, F0)
    x10 = x8(x2)
    x11 = equality(x9, x10)
    x12 = branch(x11, NEG_ONE, ONE)
    x13 = multiply(x5, x12)
    x14 = rbind(shoot, x13)
    x15 = inbox(x2)
    x16 = mapply(x14, x15)
    x17 = underfill(I, EIGHT, x16)
    x18 = o_g(x17, R5)
    x19 = colorfilter(x18, EIGHT)
    x20 = rbind(bordering, I)
    x21 = mfilter_f(x19, x20)
    O = cover(x17, x21)
    return O

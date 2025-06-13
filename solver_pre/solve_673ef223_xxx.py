def solve_673ef223_one(S, I):
    return underfill(underfill(replace(I, EIGHT, FOUR), EIGHT, mapply(rbind(shoot, branch(equality(col_row(get_arg_rank_f(o_g(I, R5), rbind(col_row, R1), L1), R2), ZERO), LEFT, RIGHT)), f_ofcolor(I, EIGHT))), EIGHT, mapply(hfrontier, shift(f_ofcolor(I, EIGHT), toivec(fork(subtract, rbind(get_rank, F0), rbind(get_rank, L1))(apply(rbind(col_row, R1), colorfilter(o_g(I, R5), TWO)))))))


def solve_673ef223(S, I):
    x1 = replace(I, EIGHT, FOUR)
    x2 = o_g(I, R5)
    x3 = rbind(col_row, R1)
    x4 = get_arg_rank_f(x2, x3, L1)
    x5 = col_row(x4, R2)
    x6 = equality(x5, ZERO)
    x7 = branch(x6, LEFT, RIGHT)
    x8 = rbind(shoot, x7)
    x9 = f_ofcolor(I, EIGHT)
    x10 = mapply(x8, x9)
    x11 = underfill(x1, EIGHT, x10)
    x12 = rbind(get_rank, F0)
    x13 = rbind(get_rank, L1)
    x14 = fork(subtract, x12, x13)
    x15 = colorfilter(x2, TWO)
    x16 = apply(x3, x15)
    x17 = x14(x16)
    x18 = toivec(x17)
    x19 = shift(x9, x18)
    x20 = mapply(hfrontier, x19)
    O = underfill(x11, EIGHT, x20)
    return O

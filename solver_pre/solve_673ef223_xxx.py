def solve_673ef223_one(S, I):
    return underfill(underfill(replace(I, EIGHT, FOUR), EIGHT, mapply(rbind(shoot, branch(equality(col_row(get_arg_rank_f(o_g(I, R5), rbind(col_row, R1), L1), R2), ZERO), LEFT, RIGHT)), f_ofcolor(I, EIGHT))), EIGHT, mapply(hfrontier, shift(f_ofcolor(I, EIGHT), toivec(fork(subtract, rbind(get_rank, F0), rbind(get_rank, L1))(apply(rbind(col_row, R1), colorfilter(o_g(I, R5), TWO)))))))


def solve_673ef223(S, I, x=0):
    x1 = replace(I, EIGHT, FOUR)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = rbind(col_row, R1)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x2, x3, L1)
    if x == 4:
        return x4
    x5 = col_row(x4, R2)
    if x == 5:
        return x5
    x6 = equality(x5, ZERO)
    if x == 6:
        return x6
    x7 = branch(x6, LEFT, RIGHT)
    if x == 7:
        return x7
    x8 = rbind(shoot, x7)
    if x == 8:
        return x8
    x9 = f_ofcolor(I, EIGHT)
    if x == 9:
        return x9
    x10 = mapply(x8, x9)
    if x == 10:
        return x10
    x11 = underfill(x1, EIGHT, x10)
    if x == 11:
        return x11
    x12 = rbind(get_rank, F0)
    if x == 12:
        return x12
    x13 = rbind(get_rank, L1)
    if x == 13:
        return x13
    x14 = fork(subtract, x12, x13)
    if x == 14:
        return x14
    x15 = colorfilter(x2, TWO)
    if x == 15:
        return x15
    x16 = apply(x3, x15)
    if x == 16:
        return x16
    x17 = x14(x16)
    if x == 17:
        return x17
    x18 = toivec(x17)
    if x == 18:
        return x18
    x19 = shift(x9, x18)
    if x == 19:
        return x19
    x20 = mapply(hfrontier, x19)
    if x == 20:
        return x20
    O = underfill(x11, EIGHT, x20)
    return O

def solve_673ef223_one(S, I):
    return underfill(underfill(replace(I, CYAN, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0))), CYAN, mapply(rbind(shoot, branch(equality(col_row(get_arg_rank_f(o_g(I, R5), rbind(col_row, R1), L1), R2), BLACK), LEFT, RIGHT)), f_ofcolor(I, CYAN))), CYAN, mapply(hfrontier, shift(f_ofcolor(I, CYAN), toivec(fork(subtract, rbind(get_rank, F0), rbind(get_rank, L1))(apply(rbind(col_row, R1), colorfilter(o_g(I, R5), RED)))))))


def solve_673ef223(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = replace(I, CYAN, x3)
    if x == 4:
        return x4
    x5 = o_g(I, R5)
    if x == 5:
        return x5
    x6 = rbind(col_row, R1)
    if x == 6:
        return x6
    x7 = get_arg_rank_f(x5, x6, L1)
    if x == 7:
        return x7
    x8 = col_row(x7, R2)
    if x == 8:
        return x8
    x9 = equality(x8, BLACK)
    if x == 9:
        return x9
    x10 = branch(x9, LEFT, RIGHT)
    if x == 10:
        return x10
    x11 = rbind(shoot, x10)
    if x == 11:
        return x11
    x12 = f_ofcolor(I, CYAN)
    if x == 12:
        return x12
    x13 = mapply(x11, x12)
    if x == 13:
        return x13
    x14 = underfill(x4, CYAN, x13)
    if x == 14:
        return x14
    x15 = rbind(get_rank, F0)
    if x == 15:
        return x15
    x16 = rbind(get_rank, L1)
    if x == 16:
        return x16
    x17 = fork(subtract, x15, x16)
    if x == 17:
        return x17
    x18 = colorfilter(x5, RED)
    if x == 18:
        return x18
    x19 = apply(x6, x18)
    if x == 19:
        return x19
    x20 = x17(x19)
    if x == 20:
        return x20
    x21 = toivec(x20)
    if x == 21:
        return x21
    x22 = shift(x12, x21)
    if x == 22:
        return x22
    x23 = mapply(hfrontier, x22)
    if x == 23:
        return x23
    O = underfill(x14, CYAN, x23)
    return O

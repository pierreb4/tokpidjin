def solve_890034e9_one(S, I):
    return fill(I, get_color_rank_t(I, L1), mapply(lbind(shift, shift(normalize(f_ofcolor(I, get_color_rank_t(I, L1))), NEG_UNITY)), occurrences(I, recolor_i(ZERO, inbox(f_ofcolor(I, get_color_rank_t(I, L1)))))))


def solve_890034e9(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, x1)
    if x == 2:
        return x2
    x3 = normalize(x2)
    if x == 3:
        return x3
    x4 = shift(x3, NEG_UNITY)
    if x == 4:
        return x4
    x5 = lbind(shift, x4)
    if x == 5:
        return x5
    x6 = inbox(x2)
    if x == 6:
        return x6
    x7 = recolor_i(ZERO, x6)
    if x == 7:
        return x7
    x8 = occurrences(I, x7)
    if x == 8:
        return x8
    x9 = mapply(x5, x8)
    if x == 9:
        return x9
    O = fill(I, x1, x9)
    return O

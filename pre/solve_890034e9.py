def solve_890034e9_one(S, I):
    return fill(I, get_color_rank_t(I, L1), mapply(lbind(shift, shift(normalize(f_ofcolor(I, get_color_rank_t(I, L1))), NEG_UNITY)), occurrences(I, recolor_i(ZERO, inbox(f_ofcolor(I, get_color_rank_t(I, L1)))))))


def solve_890034e9(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = f_ofcolor(I, x1)
    x3 = normalize(x2)
    x4 = shift(x3, NEG_UNITY)
    x5 = lbind(shift, x4)
    x6 = inbox(x2)
    x7 = recolor_i(ZERO, x6)
    x8 = occurrences(I, x7)
    x9 = mapply(x5, x8)
    O = fill(I, x1, x9)
    return O

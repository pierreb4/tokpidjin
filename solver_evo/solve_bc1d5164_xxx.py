def solve_bc1d5164_one(S, I):
    return fill(canvas(BLACK, THREE_BY_THREE), get_color_rank_t(I, L1), mapply(rbind(f_ofcolor, get_color_rank_t(I, L1)), combine_t(astuple(crop(I, ORIGIN, THREE_BY_THREE), crop(I, TWO_BY_ZERO, THREE_BY_THREE)), astuple(crop(I, tojvec(FOUR), THREE_BY_THREE), crop(I, astuple(TWO, FOUR), THREE_BY_THREE)))))


def solve_bc1d5164(S, I):
    x1 = canvas(BLACK, THREE_BY_THREE)
    x2 = get_color_rank_t(I, L1)
    x3 = rbind(f_ofcolor, x2)
    x4 = crop(I, ORIGIN, THREE_BY_THREE)
    x5 = crop(I, TWO_BY_ZERO, THREE_BY_THREE)
    x6 = astuple(x4, x5)
    x7 = tojvec(FOUR)
    x8 = crop(I, x7, THREE_BY_THREE)
    x9 = astuple(TWO, FOUR)
    x10 = crop(I, x9, THREE_BY_THREE)
    x11 = astuple(x8, x10)
    x12 = combine_t(x6, x11)
    x13 = mapply(x3, x12)
    O = fill(x1, x2, x13)
    return O

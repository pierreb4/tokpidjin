def solve_bc1d5164_one(S, I):
    return fill(canvas(BLACK, THREE_BY_THREE), get_color_rank_t(I, L1), mapply(rbind(f_ofcolor, get_color_rank_t(I, L1)), combine_t(astuple(crop(I, ORIGIN, THREE_BY_THREE), crop(I, TWO_BY_ZERO, THREE_BY_THREE)), astuple(crop(I, tojvec(FOUR), THREE_BY_THREE), crop(I, astuple(TWO, FOUR), THREE_BY_THREE)))))


def solve_bc1d5164(S, I, x=0):
    x1 = canvas(BLACK, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = get_color_rank_t(I, L1)
    if x == 2:
        return x2
    x3 = rbind(f_ofcolor, x2)
    if x == 3:
        return x3
    x4 = crop(I, ORIGIN, THREE_BY_THREE)
    if x == 4:
        return x4
    x5 = crop(I, TWO_BY_ZERO, THREE_BY_THREE)
    if x == 5:
        return x5
    x6 = astuple(x4, x5)
    if x == 6:
        return x6
    x7 = tojvec(FOUR)
    if x == 7:
        return x7
    x8 = crop(I, x7, THREE_BY_THREE)
    if x == 8:
        return x8
    x9 = astuple(TWO, FOUR)
    if x == 9:
        return x9
    x10 = crop(I, x9, THREE_BY_THREE)
    if x == 10:
        return x10
    x11 = astuple(x8, x10)
    if x == 11:
        return x11
    x12 = combine_t(x6, x11)
    if x == 12:
        return x12
    x13 = mapply(x3, x12)
    if x == 13:
        return x13
    O = fill(x1, x2, x13)
    return O

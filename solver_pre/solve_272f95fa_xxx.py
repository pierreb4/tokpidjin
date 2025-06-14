def solve_272f95fa_one(S, I):
    return fill(fill(fill(fill(fill(I, SIX, extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I)))), TWO, get_arg_rank_f(sfilter_f(remove_f(extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I))), apply(toindices, colorfilter(o_g(I, R4), ZERO))), lbind(vmatching, extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I))))), rbind(col_row, R1), L1)), ONE, get_arg_rank_f(sfilter_f(remove_f(extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I))), apply(toindices, colorfilter(o_g(I, R4), ZERO))), lbind(vmatching, extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I))))), rbind(col_row, R1), F0)), FOUR, get_arg_rank_f(sfilter_f(remove_f(extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I))), apply(toindices, colorfilter(o_g(I, R4), ZERO))), lbind(hmatching, extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I))))), rbind(col_row, R2), L1)), THREE, get_arg_rank_f(sfilter_f(remove_f(extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I))), apply(toindices, colorfilter(o_g(I, R4), ZERO))), lbind(hmatching, extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I))))), rbind(col_row, R2), F0))


def solve_272f95fa(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = apply(toindices, x2)
    if x == 3:
        return x3
    x4 = rbind(bordering, I)
    if x == 4:
        return x4
    x5 = compose(flip, x4)
    if x == 5:
        return x5
    x6 = extract(x3, x5)
    if x == 6:
        return x6
    x7 = fill(I, SIX, x6)
    if x == 7:
        return x7
    x8 = remove_f(x6, x3)
    if x == 8:
        return x8
    x9 = lbind(vmatching, x6)
    if x == 9:
        return x9
    x10 = sfilter_f(x8, x9)
    if x == 10:
        return x10
    x11 = rbind(col_row, R1)
    if x == 11:
        return x11
    x12 = get_arg_rank_f(x10, x11, L1)
    if x == 12:
        return x12
    x13 = fill(x7, TWO, x12)
    if x == 13:
        return x13
    x14 = get_arg_rank_f(x10, x11, F0)
    if x == 14:
        return x14
    x15 = fill(x13, ONE, x14)
    if x == 15:
        return x15
    x16 = lbind(hmatching, x6)
    if x == 16:
        return x16
    x17 = sfilter_f(x8, x16)
    if x == 17:
        return x17
    x18 = rbind(col_row, R2)
    if x == 18:
        return x18
    x19 = get_arg_rank_f(x17, x18, L1)
    if x == 19:
        return x19
    x20 = fill(x15, FOUR, x19)
    if x == 20:
        return x20
    x21 = get_arg_rank_f(x17, x18, F0)
    if x == 21:
        return x21
    O = fill(x20, THREE, x21)
    return O

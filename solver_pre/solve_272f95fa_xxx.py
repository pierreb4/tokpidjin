def solve_272f95fa_one(S, I):
    return fill(fill(fill(fill(fill(I, SIX, extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I)))), TWO, get_arg_rank_f(sfilter_f(remove_f(extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I))), apply(toindices, colorfilter(o_g(I, R4), ZERO))), lbind(vmatching, extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I))))), rbind(col_row, R1), L1)), ONE, get_arg_rank_f(sfilter_f(remove_f(extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I))), apply(toindices, colorfilter(o_g(I, R4), ZERO))), lbind(vmatching, extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I))))), rbind(col_row, R1), F0)), FOUR, get_arg_rank_f(sfilter_f(remove_f(extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I))), apply(toindices, colorfilter(o_g(I, R4), ZERO))), lbind(hmatching, extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I))))), rbind(col_row, R2), L1)), THREE, get_arg_rank_f(sfilter_f(remove_f(extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I))), apply(toindices, colorfilter(o_g(I, R4), ZERO))), lbind(hmatching, extract(apply(toindices, colorfilter(o_g(I, R4), ZERO)), compose(flip, rbind(bordering, I))))), rbind(col_row, R2), F0))


def solve_272f95fa(S, I):
    x1 = o_g(I, R4)
    x2 = colorfilter(x1, ZERO)
    x3 = apply(toindices, x2)
    x4 = rbind(bordering, I)
    x5 = compose(flip, x4)
    x6 = extract(x3, x5)
    x7 = fill(I, SIX, x6)
    x8 = remove_f(x6, x3)
    x9 = lbind(vmatching, x6)
    x10 = sfilter_f(x8, x9)
    x11 = rbind(col_row, R1)
    x12 = get_arg_rank_f(x10, x11, L1)
    x13 = fill(x7, TWO, x12)
    x14 = get_arg_rank_f(x10, x11, F0)
    x15 = fill(x13, ONE, x14)
    x16 = lbind(hmatching, x6)
    x17 = sfilter_f(x8, x16)
    x18 = rbind(col_row, R2)
    x19 = get_arg_rank_f(x17, x18, L1)
    x20 = fill(x15, FOUR, x19)
    x21 = get_arg_rank_f(x17, x18, F0)
    O = fill(x20, THREE, x21)
    return O

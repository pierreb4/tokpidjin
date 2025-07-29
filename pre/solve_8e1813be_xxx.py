def solve_8e1813be_one(S, I):
    return branch(vline_o(get_nth_f(o_g(replace(I, FIVE, ZERO), R7), F0)), rbind(mir_rot_t, R1), identity)(apply(rbind(repeat, size_t(dedupe(apply(color, order(o_g(branch(vline_o(get_nth_f(o_g(replace(I, FIVE, ZERO), R7), F0)), rbind(mir_rot_t, R1), identity)(replace(I, FIVE, ZERO)), R7), rbind(col_row, R1)))))), dedupe(apply(color, order(o_g(branch(vline_o(get_nth_f(o_g(replace(I, FIVE, ZERO), R7), F0)), rbind(mir_rot_t, R1), identity)(replace(I, FIVE, ZERO)), R7), rbind(col_row, R1))))))


def solve_8e1813be(S, I):
    x1 = replace(I, FIVE, ZERO)
    x2 = o_g(x1, R7)
    x3 = get_nth_f(x2, F0)
    x4 = vline_o(x3)
    x5 = rbind(mir_rot_t, R1)
    x6 = branch(x4, x5, identity)
    x7 = x6(x1)
    x8 = o_g(x7, R7)
    x9 = rbind(col_row, R1)
    x10 = order(x8, x9)
    x11 = apply(color, x10)
    x12 = dedupe(x11)
    x13 = size_t(x12)
    x14 = rbind(repeat, x13)
    x15 = apply(x14, x12)
    O = x6(x15)
    return O

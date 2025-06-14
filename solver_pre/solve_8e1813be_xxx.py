def solve_8e1813be_one(S, I):
    return branch(vline_o(get_nth_f(o_g(replace(I, FIVE, ZERO), R7), F0)), rbind(mir_rot_t, R1), identity)(apply(rbind(repeat, size_t(dedupe(apply(color, order(o_g(branch(vline_o(get_nth_f(o_g(replace(I, FIVE, ZERO), R7), F0)), rbind(mir_rot_t, R1), identity)(replace(I, FIVE, ZERO)), R7), rbind(col_row, R1)))))), dedupe(apply(color, order(o_g(branch(vline_o(get_nth_f(o_g(replace(I, FIVE, ZERO), R7), F0)), rbind(mir_rot_t, R1), identity)(replace(I, FIVE, ZERO)), R7), rbind(col_row, R1))))))


def solve_8e1813be(S, I, x=0):
    x1 = replace(I, FIVE, ZERO)
    if x == 1:
        return x1
    x2 = o_g(x1, R7)
    if x == 2:
        return x2
    x3 = get_nth_f(x2, F0)
    if x == 3:
        return x3
    x4 = vline_o(x3)
    if x == 4:
        return x4
    x5 = rbind(mir_rot_t, R1)
    if x == 5:
        return x5
    x6 = branch(x4, x5, identity)
    if x == 6:
        return x6
    x7 = x6(x1)
    if x == 7:
        return x7
    x8 = o_g(x7, R7)
    if x == 8:
        return x8
    x9 = rbind(col_row, R1)
    if x == 9:
        return x9
    x10 = order(x8, x9)
    if x == 10:
        return x10
    x11 = apply(color, x10)
    if x == 11:
        return x11
    x12 = dedupe(x11)
    if x == 12:
        return x12
    x13 = size_t(x12)
    if x == 13:
        return x13
    x14 = rbind(repeat, x13)
    if x == 14:
        return x14
    x15 = apply(x14, x12)
    if x == 15:
        return x15
    O = x6(x15)
    return O

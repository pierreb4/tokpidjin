def solve_8e1813be_one(S, I):
    return branch(vline_o(get_nth_f(o_g(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), R7), F0)), rbind(mir_rot_t, R1), identity)(apply(rbind(repeat, size_t(dedupe(apply(color, order(o_g(branch(vline_o(get_nth_f(o_g(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), R7), F0)), rbind(mir_rot_t, R1), identity)(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), R7), rbind(col_row, R1)))))), dedupe(apply(color, order(o_g(branch(vline_o(get_nth_f(o_g(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), R7), F0)), rbind(mir_rot_t, R1), identity)(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), R7), rbind(col_row, R1))))))


def solve_8e1813be(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F1)
    if x == 2:
        return x2
    x3 = c_iz_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = rbind(get_nth_t, F0)
    if x == 4:
        return x4
    x5 = c_iz_n(S, x1, x4)
    if x == 5:
        return x5
    x6 = replace(I, x3, x5)
    if x == 6:
        return x6
    x7 = o_g(x6, R7)
    if x == 7:
        return x7
    x8 = get_nth_f(x7, F0)
    if x == 8:
        return x8
    x9 = vline_o(x8)
    if x == 9:
        return x9
    x10 = rbind(mir_rot_t, R1)
    if x == 10:
        return x10
    x11 = branch(x9, x10, identity)
    if x == 11:
        return x11
    x12 = x11(x6)
    if x == 12:
        return x12
    x13 = o_g(x12, R7)
    if x == 13:
        return x13
    x14 = rbind(col_row, R1)
    if x == 14:
        return x14
    x15 = order(x13, x14)
    if x == 15:
        return x15
    x16 = apply(color, x15)
    if x == 16:
        return x16
    x17 = dedupe(x16)
    if x == 17:
        return x17
    x18 = size_t(x17)
    if x == 18:
        return x18
    x19 = rbind(repeat, x18)
    if x == 19:
        return x19
    x20 = apply(x19, x17)
    if x == 20:
        return x20
    O = x11(x20)
    return O

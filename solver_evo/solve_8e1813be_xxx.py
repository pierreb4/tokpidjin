def solve_8e1813be_one(S, I):
    return branch(vline_o(get_nth_f(o_g(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), R7), F0)), rbind(mir_rot_t, R1), identity)(apply(rbind(repeat, size_t(dedupe(apply(color, order(o_g(branch(vline_o(get_nth_f(o_g(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), R7), F0)), rbind(mir_rot_t, R1), identity)(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), R7), rbind(col_row, R1)))))), dedupe(apply(color, order(o_g(branch(vline_o(get_nth_f(o_g(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), R7), F0)), rbind(mir_rot_t, R1), identity)(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), R7), rbind(col_row, R1))))))


def solve_8e1813be(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F1)
    x3 = c_iz_n(S, x1, x2)
    x4 = rbind(get_nth_t, F0)
    x5 = c_iz_n(S, x1, x4)
    x6 = replace(I, x3, x5)
    x7 = o_g(x6, R7)
    x8 = get_nth_f(x7, F0)
    x9 = vline_o(x8)
    x10 = rbind(mir_rot_t, R1)
    x11 = branch(x9, x10, identity)
    x12 = x11(x6)
    x13 = o_g(x12, R7)
    x14 = rbind(col_row, R1)
    x15 = order(x13, x14)
    x16 = apply(color, x15)
    x17 = dedupe(x16)
    x18 = size_t(x17)
    x19 = rbind(repeat, x18)
    x20 = apply(x19, x17)
    O = x11(x20)
    return O

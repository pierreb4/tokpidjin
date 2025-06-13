def solve_4093f84a_one(S, I):
    return branch(portrait_f(f_ofcolor(I, GRAY)), identity, rbind(mir_rot_t, R1))(hconcat(apply(rbind(order, identity), lefthalf(branch(portrait_f(f_ofcolor(I, GRAY)), identity, rbind(mir_rot_t, R1))(replace(I, get_color_rank_t(I, L1), GRAY)))), apply(rbind(order, invert), righthalf(branch(portrait_f(f_ofcolor(I, GRAY)), identity, rbind(mir_rot_t, R1))(replace(I, get_color_rank_t(I, L1), GRAY))))))


def solve_4093f84a(S, I):
    x1 = f_ofcolor(I, GRAY)
    x2 = portrait_f(x1)
    x3 = rbind(mir_rot_t, R1)
    x4 = branch(x2, identity, x3)
    x5 = rbind(order, identity)
    x6 = get_color_rank_t(I, L1)
    x7 = replace(I, x6, GRAY)
    x8 = x4(x7)
    x9 = lefthalf(x8)
    x10 = apply(x5, x9)
    x11 = rbind(order, invert)
    x12 = righthalf(x8)
    x13 = apply(x11, x12)
    x14 = hconcat(x10, x13)
    O = x4(x14)
    return O

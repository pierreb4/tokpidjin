def solve_4093f84a_one(S, I):
    return branch(portrait_f(f_ofcolor(I, FIVE)), identity, rbind(mir_rot_t, R1))(hconcat(apply(rbind(order, identity), lefthalf(branch(portrait_f(f_ofcolor(I, FIVE)), identity, rbind(mir_rot_t, R1))(replace(I, get_color_rank_t(I, L1), FIVE)))), apply(rbind(order, invert), righthalf(branch(portrait_f(f_ofcolor(I, FIVE)), identity, rbind(mir_rot_t, R1))(replace(I, get_color_rank_t(I, L1), FIVE))))))


def solve_4093f84a(S, I, x=0):
    x1 = f_ofcolor(I, FIVE)
    if x == 1:
        return x1
    x2 = portrait_f(x1)
    if x == 2:
        return x2
    x3 = rbind(mir_rot_t, R1)
    if x == 3:
        return x3
    x4 = branch(x2, identity, x3)
    if x == 4:
        return x4
    x5 = rbind(order, identity)
    if x == 5:
        return x5
    x6 = get_color_rank_t(I, L1)
    if x == 6:
        return x6
    x7 = replace(I, x6, FIVE)
    if x == 7:
        return x7
    x8 = x4(x7)
    if x == 8:
        return x8
    x9 = lefthalf(x8)
    if x == 9:
        return x9
    x10 = apply(x5, x9)
    if x == 10:
        return x10
    x11 = rbind(order, invert)
    if x == 11:
        return x11
    x12 = righthalf(x8)
    if x == 12:
        return x12
    x13 = apply(x11, x12)
    if x == 13:
        return x13
    x14 = hconcat(x10, x13)
    if x == 14:
        return x14
    O = x4(x14)
    return O

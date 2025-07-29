def solve_a87f7484_one(S, I):
    return branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(extract(hsplit(branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(I), decrement(numcolors_t(I))), matcher(rbind(f_ofcolor, ZERO), get_common_rank_t(apply(rbind(f_ofcolor, ZERO), hsplit(branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(I), decrement(numcolors_t(I)))), L1))))


def solve_a87f7484(S, I):
    x1 = portrait_t(I)
    x2 = rbind(mir_rot_t, R1)
    x3 = branch(x1, x2, identity)
    x4 = x3(I)
    x5 = numcolors_t(I)
    x6 = decrement(x5)
    x7 = hsplit(x4, x6)
    x8 = rbind(f_ofcolor, ZERO)
    x9 = apply(x8, x7)
    x10 = get_common_rank_t(x9, L1)
    x11 = matcher(x8, x10)
    x12 = extract(x7, x11)
    O = x3(x12)
    return O

def solve_a87f7484_one(S, I):
    return branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(extract(hsplit(branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(I), decrement(numcolors_t(I))), matcher(rbind(f_ofcolor, ZERO), get_common_rank_t(apply(rbind(f_ofcolor, ZERO), hsplit(branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(I), decrement(numcolors_t(I)))), L1))))


def solve_a87f7484(S, I, x=0):
    x1 = portrait_t(I)
    if x == 1:
        return x1
    x2 = rbind(mir_rot_t, R1)
    if x == 2:
        return x2
    x3 = branch(x1, x2, identity)
    if x == 3:
        return x3
    x4 = x3(I)
    if x == 4:
        return x4
    x5 = numcolors_t(I)
    if x == 5:
        return x5
    x6 = decrement(x5)
    if x == 6:
        return x6
    x7 = hsplit(x4, x6)
    if x == 7:
        return x7
    x8 = rbind(f_ofcolor, ZERO)
    if x == 8:
        return x8
    x9 = apply(x8, x7)
    if x == 9:
        return x9
    x10 = get_common_rank_t(x9, L1)
    if x == 10:
        return x10
    x11 = matcher(x8, x10)
    if x == 11:
        return x11
    x12 = extract(x7, x11)
    if x == 12:
        return x12
    O = x3(x12)
    return O

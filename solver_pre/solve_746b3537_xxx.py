def solve_746b3537_one(S, I):
    return branch(equality(chain(size, dedupe, rbind(get_nth_f, F0))(I), ONE), rbind(mir_rot_t, R1), identity)(repeat(apply(color, order(o_g(branch(equality(chain(size, dedupe, rbind(get_nth_f, F0))(I), ONE), rbind(mir_rot_t, R1), identity)(I), R4), rbind(col_row, R2))), ONE))


def solve_746b3537(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = chain(size, dedupe, x1)
    if x == 2:
        return x2
    x3 = x2(I)
    if x == 3:
        return x3
    x4 = equality(x3, ONE)
    if x == 4:
        return x4
    x5 = rbind(mir_rot_t, R1)
    if x == 5:
        return x5
    x6 = branch(x4, x5, identity)
    if x == 6:
        return x6
    x7 = x6(I)
    if x == 7:
        return x7
    x8 = o_g(x7, R4)
    if x == 8:
        return x8
    x9 = rbind(col_row, R2)
    if x == 9:
        return x9
    x10 = order(x8, x9)
    if x == 10:
        return x10
    x11 = apply(color, x10)
    if x == 11:
        return x11
    x12 = repeat(x11, ONE)
    if x == 12:
        return x12
    O = x6(x12)
    return O

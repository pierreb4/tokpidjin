def solve_746b3537_one(S, I):
    return branch(equality(chain(size, dedupe, rbind(get_nth_f, F0))(I), BLUE), rbind(mir_rot_t, R1), identity)(repeat(apply(color, order(o_g(branch(equality(chain(size, dedupe, rbind(get_nth_f, F0))(I), BLUE), rbind(mir_rot_t, R1), identity)(I), R4), rbind(col_row, R2))), BLUE))


def solve_746b3537(S, I):
    x1 = rbind(get_nth_f, F0)
    x2 = chain(size, dedupe, x1)
    x3 = x2(I)
    x4 = equality(x3, BLUE)
    x5 = rbind(mir_rot_t, R1)
    x6 = branch(x4, x5, identity)
    x7 = x6(I)
    x8 = o_g(x7, R4)
    x9 = rbind(col_row, R2)
    x10 = order(x8, x9)
    x11 = apply(color, x10)
    x12 = repeat(x11, BLUE)
    O = x6(x12)
    return O

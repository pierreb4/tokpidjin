def solve_508bd3b6_one(S, I):
    return paint(paint(fill(paint(fill(I, THREE, connect(add(branch(equality(index(I, corner(get_arg_rank_f(o_g(I, R7), size, L1), R0)), EIGHT), corner(get_arg_rank_f(o_g(I, R7), size, L1), R0), corner(get_arg_rank_f(o_g(I, R7), size, L1), R1)), double(multiply(branch(equality(index(I, corner(get_arg_rank_f(o_g(I, R7), size, L1), R0)), EIGHT), UNITY, DOWN_LEFT), width_t(I)))), subtract(branch(equality(index(I, corner(get_arg_rank_f(o_g(I, R7), size, L1), R0)), EIGHT), corner(get_arg_rank_f(o_g(I, R7), size, L1), R0), corner(get_arg_rank_f(o_g(I, R7), size, L1), R1)), double(multiply(branch(equality(index(I, corner(get_arg_rank_f(o_g(I, R7), size, L1), R0)), EIGHT), UNITY, DOWN_LEFT), width_t(I)))))), get_arg_rank_f(o_g(I, R7), size, F0)), THREE, connect(add(get_nth_t(get_nth_f(extract(o_g(paint(fill(I, THREE, connect(add(branch(equality(index(I, corner(get_arg_rank_f(o_g(I, R7), size, L1), R0)), EIGHT), corner(get_arg_rank_f(o_g(I, R7), size, L1), R0), corner(get_arg_rank_f(o_g(I, R7), size, L1), R1)), double(multiply(branch(equality(index(I, corner(get_arg_rank_f(o_g(I, R7), size, L1), R0)), EIGHT), UNITY, DOWN_LEFT), width_t(I)))), subtract(branch(equality(index(I, corner(get_arg_rank_f(o_g(I, R7), size, L1), R0)), EIGHT), corner(get_arg_rank_f(o_g(I, R7), size, L1), R0), corner(get_arg_rank_f(o_g(I, R7), size, L1), R1)), double(multiply(branch(equality(index(I, corner(get_arg_rank_f(o_g(I, R7), size, L1), R0)), EIGHT), UNITY, DOWN_LEFT), width_t(I)))))), get_arg_rank_f(o_g(I, R7), size, F0)), R5), rbind(adjacent, get_arg_rank_f(o_g(I, R7), size, F0))), F0), L1), double(multiply(branch(flip(equality(index(I, corner(get_arg_rank_f(o_g(I, R7), size, L1), R0)), EIGHT)), UNITY, DOWN_LEFT), width_t(I)))), subtract(get_nth_t(get_nth_f(extract(o_g(paint(fill(I, THREE, connect(add(branch(equality(index(I, corner(get_arg_rank_f(o_g(I, R7), size, L1), R0)), EIGHT), corner(get_arg_rank_f(o_g(I, R7), size, L1), R0), corner(get_arg_rank_f(o_g(I, R7), size, L1), R1)), double(multiply(branch(equality(index(I, corner(get_arg_rank_f(o_g(I, R7), size, L1), R0)), EIGHT), UNITY, DOWN_LEFT), width_t(I)))), subtract(branch(equality(index(I, corner(get_arg_rank_f(o_g(I, R7), size, L1), R0)), EIGHT), corner(get_arg_rank_f(o_g(I, R7), size, L1), R0), corner(get_arg_rank_f(o_g(I, R7), size, L1), R1)), double(multiply(branch(equality(index(I, corner(get_arg_rank_f(o_g(I, R7), size, L1), R0)), EIGHT), UNITY, DOWN_LEFT), width_t(I)))))), get_arg_rank_f(o_g(I, R7), size, F0)), R5), rbind(adjacent, get_arg_rank_f(o_g(I, R7), size, F0))), F0), L1), double(multiply(branch(flip(equality(index(I, corner(get_arg_rank_f(o_g(I, R7), size, L1), R0)), EIGHT)), UNITY, DOWN_LEFT), width_t(I)))))), get_arg_rank_f(o_g(I, R7), size, L1)), get_arg_rank_f(o_g(I, R7), size, F0))


def solve_508bd3b6(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, L1)
    if x == 2:
        return x2
    x3 = corner(x2, R0)
    if x == 3:
        return x3
    x4 = index(I, x3)
    if x == 4:
        return x4
    x5 = equality(x4, EIGHT)
    if x == 5:
        return x5
    x6 = corner(x2, R1)
    if x == 6:
        return x6
    x7 = branch(x5, x3, x6)
    if x == 7:
        return x7
    x8 = branch(x5, UNITY, DOWN_LEFT)
    if x == 8:
        return x8
    x9 = width_t(I)
    if x == 9:
        return x9
    x10 = multiply(x8, x9)
    if x == 10:
        return x10
    x11 = double(x10)
    if x == 11:
        return x11
    x12 = add(x7, x11)
    if x == 12:
        return x12
    x13 = subtract(x7, x11)
    if x == 13:
        return x13
    x14 = connect(x12, x13)
    if x == 14:
        return x14
    x15 = fill(I, THREE, x14)
    if x == 15:
        return x15
    x16 = get_arg_rank_f(x1, size, F0)
    if x == 16:
        return x16
    x17 = paint(x15, x16)
    if x == 17:
        return x17
    x18 = o_g(x17, R5)
    if x == 18:
        return x18
    x19 = rbind(adjacent, x16)
    if x == 19:
        return x19
    x20 = extract(x18, x19)
    if x == 20:
        return x20
    x21 = get_nth_f(x20, F0)
    if x == 21:
        return x21
    x22 = get_nth_t(x21, L1)
    if x == 22:
        return x22
    x23 = flip(x5)
    if x == 23:
        return x23
    x24 = branch(x23, UNITY, DOWN_LEFT)
    if x == 24:
        return x24
    x25 = multiply(x24, x9)
    if x == 25:
        return x25
    x26 = double(x25)
    if x == 26:
        return x26
    x27 = add(x22, x26)
    if x == 27:
        return x27
    x28 = subtract(x22, x26)
    if x == 28:
        return x28
    x29 = connect(x27, x28)
    if x == 29:
        return x29
    x30 = fill(x17, THREE, x29)
    if x == 30:
        return x30
    x31 = paint(x30, x2)
    if x == 31:
        return x31
    O = paint(x31, x16)
    return O

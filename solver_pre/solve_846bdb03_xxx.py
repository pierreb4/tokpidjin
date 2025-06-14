def solve_846bdb03_one(S, I):
    return paint(subgrid(merge_f(remove_f(extract(o_g(I, R1), matcher(rbind(colorcount_f, FOUR), ZERO)), o_g(I, R1))), I), shift(normalize(branch(equality(index(subgrid(merge_f(remove_f(extract(o_g(I, R1), matcher(rbind(colorcount_f, FOUR), ZERO)), o_g(I, R1))), I), DOWN), other_f(palette_t(lefthalf(subgrid(extract(o_g(I, R1), matcher(rbind(colorcount_f, FOUR), ZERO)), I))), ZERO)), identity, rbind(mir_rot_f, R2))(extract(o_g(I, R1), matcher(rbind(colorcount_f, FOUR), ZERO)))), UNITY))


def solve_846bdb03(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = rbind(colorcount_f, FOUR)
    if x == 2:
        return x2
    x3 = matcher(x2, ZERO)
    if x == 3:
        return x3
    x4 = extract(x1, x3)
    if x == 4:
        return x4
    x5 = remove_f(x4, x1)
    if x == 5:
        return x5
    x6 = merge_f(x5)
    if x == 6:
        return x6
    x7 = subgrid(x6, I)
    if x == 7:
        return x7
    x8 = index(x7, DOWN)
    if x == 8:
        return x8
    x9 = subgrid(x4, I)
    if x == 9:
        return x9
    x10 = lefthalf(x9)
    if x == 10:
        return x10
    x11 = palette_t(x10)
    if x == 11:
        return x11
    x12 = other_f(x11, ZERO)
    if x == 12:
        return x12
    x13 = equality(x8, x12)
    if x == 13:
        return x13
    x14 = rbind(mir_rot_f, R2)
    if x == 14:
        return x14
    x15 = branch(x13, identity, x14)
    if x == 15:
        return x15
    x16 = x15(x4)
    if x == 16:
        return x16
    x17 = normalize(x16)
    if x == 17:
        return x17
    x18 = shift(x17, UNITY)
    if x == 18:
        return x18
    O = paint(x7, x18)
    return O

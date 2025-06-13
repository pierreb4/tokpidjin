def solve_846bdb03_one(S, I):
    return paint(subgrid(merge_f(remove_f(extract(o_g(I, R1), matcher(rbind(colorcount_f, YELLOW), BLACK)), o_g(I, R1))), I), shift(normalize(branch(equality(index(subgrid(merge_f(remove_f(extract(o_g(I, R1), matcher(rbind(colorcount_f, YELLOW), BLACK)), o_g(I, R1))), I), DOWN), other_f(palette_t(lefthalf(subgrid(extract(o_g(I, R1), matcher(rbind(colorcount_f, YELLOW), BLACK)), I))), BLACK)), identity, rbind(mir_rot_f, R2))(extract(o_g(I, R1), matcher(rbind(colorcount_f, YELLOW), BLACK)))), UNITY))


def solve_846bdb03(S, I):
    x1 = o_g(I, R1)
    x2 = rbind(colorcount_f, YELLOW)
    x3 = matcher(x2, BLACK)
    x4 = extract(x1, x3)
    x5 = remove_f(x4, x1)
    x6 = merge_f(x5)
    x7 = subgrid(x6, I)
    x8 = index(x7, DOWN)
    x9 = subgrid(x4, I)
    x10 = lefthalf(x9)
    x11 = palette_t(x10)
    x12 = other_f(x11, BLACK)
    x13 = equality(x8, x12)
    x14 = rbind(mir_rot_f, R2)
    x15 = branch(x13, identity, x14)
    x16 = x15(x4)
    x17 = normalize(x16)
    x18 = shift(x17, UNITY)
    O = paint(x7, x18)
    return O

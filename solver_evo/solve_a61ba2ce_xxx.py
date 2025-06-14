def solve_a61ba2ce_one(S, I):
    return vconcat(hconcat(chain(rbind(subgrid, I), lbind(extract, o_g(I, R5)), lbind(compose, matcher(lbind(index, I), BLACK)))(rbind(corner, R3)), chain(rbind(subgrid, I), lbind(extract, o_g(I, R5)), lbind(compose, matcher(lbind(index, I), BLACK)))(rbind(corner, R2))), hconcat(chain(rbind(subgrid, I), lbind(extract, o_g(I, R5)), lbind(compose, matcher(lbind(index, I), BLACK)))(rbind(corner, R1)), chain(rbind(subgrid, I), lbind(extract, o_g(I, R5)), lbind(compose, matcher(lbind(index, I), BLACK)))(rbind(corner, R0))))


def solve_a61ba2ce(S, I, x=0):
    x1 = rbind(subgrid, I)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = lbind(extract, x2)
    if x == 3:
        return x3
    x4 = lbind(index, I)
    if x == 4:
        return x4
    x5 = matcher(x4, BLACK)
    if x == 5:
        return x5
    x6 = lbind(compose, x5)
    if x == 6:
        return x6
    x7 = chain(x1, x3, x6)
    if x == 7:
        return x7
    x8 = rbind(corner, R3)
    if x == 8:
        return x8
    x9 = x7(x8)
    if x == 9:
        return x9
    x10 = rbind(corner, R2)
    if x == 10:
        return x10
    x11 = x7(x10)
    if x == 11:
        return x11
    x12 = hconcat(x9, x11)
    if x == 12:
        return x12
    x13 = rbind(corner, R1)
    if x == 13:
        return x13
    x14 = x7(x13)
    if x == 14:
        return x14
    x15 = rbind(corner, R0)
    if x == 15:
        return x15
    x16 = x7(x15)
    if x == 16:
        return x16
    x17 = hconcat(x14, x16)
    if x == 17:
        return x17
    O = vconcat(x12, x17)
    return O

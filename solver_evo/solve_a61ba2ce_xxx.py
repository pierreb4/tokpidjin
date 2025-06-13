def solve_a61ba2ce_one(S, I):
    return vconcat(hconcat(chain(rbind(subgrid, I), lbind(extract, o_g(I, R5)), lbind(compose, matcher(lbind(index, I), BLACK)))(rbind(corner, R3)), chain(rbind(subgrid, I), lbind(extract, o_g(I, R5)), lbind(compose, matcher(lbind(index, I), BLACK)))(rbind(corner, R2))), hconcat(chain(rbind(subgrid, I), lbind(extract, o_g(I, R5)), lbind(compose, matcher(lbind(index, I), BLACK)))(rbind(corner, R1)), chain(rbind(subgrid, I), lbind(extract, o_g(I, R5)), lbind(compose, matcher(lbind(index, I), BLACK)))(rbind(corner, R0))))


def solve_a61ba2ce(S, I):
    x1 = rbind(subgrid, I)
    x2 = o_g(I, R5)
    x3 = lbind(extract, x2)
    x4 = lbind(index, I)
    x5 = matcher(x4, BLACK)
    x6 = lbind(compose, x5)
    x7 = chain(x1, x3, x6)
    x8 = rbind(corner, R3)
    x9 = x7(x8)
    x10 = rbind(corner, R2)
    x11 = x7(x10)
    x12 = hconcat(x9, x11)
    x13 = rbind(corner, R1)
    x14 = x7(x13)
    x15 = rbind(corner, R0)
    x16 = x7(x15)
    x17 = hconcat(x14, x16)
    O = vconcat(x12, x17)
    return O

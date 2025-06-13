def solve_4612dd53_one(S, I):
    return underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), shift(f_ofcolor(fill(subgrid(f_ofcolor(I, BLUE), fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), box(f_ofcolor(I, BLUE)))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), branch(greater(size_f(mapply(vfrontier, f_ofcolor(subgrid(f_ofcolor(I, BLUE), fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), box(f_ofcolor(I, BLUE)))), BLUE))), size_f(mapply(hfrontier, f_ofcolor(subgrid(f_ofcolor(I, BLUE), fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), box(f_ofcolor(I, BLUE)))), BLUE)))), mapply(hfrontier, f_ofcolor(subgrid(f_ofcolor(I, BLUE), fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), box(f_ofcolor(I, BLUE)))), BLUE)), mapply(vfrontier, f_ofcolor(subgrid(f_ofcolor(I, BLUE), fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), box(f_ofcolor(I, BLUE)))), BLUE)))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0))), corner(f_ofcolor(I, BLUE), R0)))


def solve_4612dd53(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = f_ofcolor(I, BLUE)
    x5 = box(x4)
    x6 = fill(I, x3, x5)
    x7 = subgrid(x4, x6)
    x8 = f_ofcolor(x7, BLUE)
    x9 = mapply(vfrontier, x8)
    x10 = size_f(x9)
    x11 = mapply(hfrontier, x8)
    x12 = size_f(x11)
    x13 = greater(x10, x12)
    x14 = branch(x13, x11, x9)
    x15 = fill(x7, x3, x14)
    x16 = f_ofcolor(x15, x3)
    x17 = corner(x4, R0)
    x18 = shift(x16, x17)
    O = underfill(I, x3, x18)
    return O

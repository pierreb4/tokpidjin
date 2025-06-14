def solve_4612dd53_one(S, I):
    return underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), shift(f_ofcolor(fill(subgrid(f_ofcolor(I, BLUE), fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), box(f_ofcolor(I, BLUE)))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), branch(greater(size_f(mapply(vfrontier, f_ofcolor(subgrid(f_ofcolor(I, BLUE), fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), box(f_ofcolor(I, BLUE)))), BLUE))), size_f(mapply(hfrontier, f_ofcolor(subgrid(f_ofcolor(I, BLUE), fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), box(f_ofcolor(I, BLUE)))), BLUE)))), mapply(hfrontier, f_ofcolor(subgrid(f_ofcolor(I, BLUE), fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), box(f_ofcolor(I, BLUE)))), BLUE)), mapply(vfrontier, f_ofcolor(subgrid(f_ofcolor(I, BLUE), fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), box(f_ofcolor(I, BLUE)))), BLUE)))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0))), corner(f_ofcolor(I, BLUE), R0)))


def solve_4612dd53(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, BLUE)
    if x == 4:
        return x4
    x5 = box(x4)
    if x == 5:
        return x5
    x6 = fill(I, x3, x5)
    if x == 6:
        return x6
    x7 = subgrid(x4, x6)
    if x == 7:
        return x7
    x8 = f_ofcolor(x7, BLUE)
    if x == 8:
        return x8
    x9 = mapply(vfrontier, x8)
    if x == 9:
        return x9
    x10 = size_f(x9)
    if x == 10:
        return x10
    x11 = mapply(hfrontier, x8)
    if x == 11:
        return x11
    x12 = size_f(x11)
    if x == 12:
        return x12
    x13 = greater(x10, x12)
    if x == 13:
        return x13
    x14 = branch(x13, x11, x9)
    if x == 14:
        return x14
    x15 = fill(x7, x3, x14)
    if x == 15:
        return x15
    x16 = f_ofcolor(x15, x3)
    if x == 16:
        return x16
    x17 = corner(x4, R0)
    if x == 17:
        return x17
    x18 = shift(x16, x17)
    if x == 18:
        return x18
    O = underfill(I, x3, x18)
    return O

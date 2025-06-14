def solve_e48d4e1a_one(S, I):
    return fill(canvas(BLACK, shape_t(I)), get_color_rank_t(fill(I, BLACK, f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), L1), fork(combine, vfrontier, hfrontier)(add(multiply(DOWN_LEFT, size_f(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))))), extract(f_ofcolor(I, get_color_rank_t(fill(I, BLACK, f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), L1)), matcher(chain(rbind(colorcount_f, get_color_rank_t(fill(I, BLACK, f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), L1)), rbind(toobject, I), dneighbors), YELLOW)))))


def solve_e48d4e1a(S, I, x=0):
    x1 = shape_t(I)
    if x == 1:
        return x1
    x2 = canvas(BLACK, x1)
    if x == 2:
        return x2
    x3 = identity(p_g)
    if x == 3:
        return x3
    x4 = rbind(get_nth_t, F0)
    if x == 4:
        return x4
    x5 = c_iz_n(S, x3, x4)
    if x == 5:
        return x5
    x6 = f_ofcolor(I, x5)
    if x == 6:
        return x6
    x7 = fill(I, BLACK, x6)
    if x == 7:
        return x7
    x8 = get_color_rank_t(x7, L1)
    if x == 8:
        return x8
    x9 = fork(combine, vfrontier, hfrontier)
    if x == 9:
        return x9
    x10 = size_f(x6)
    if x == 10:
        return x10
    x11 = multiply(DOWN_LEFT, x10)
    if x == 11:
        return x11
    x12 = f_ofcolor(I, x8)
    if x == 12:
        return x12
    x13 = rbind(colorcount_f, x8)
    if x == 13:
        return x13
    x14 = rbind(toobject, I)
    if x == 14:
        return x14
    x15 = chain(x13, x14, dneighbors)
    if x == 15:
        return x15
    x16 = matcher(x15, YELLOW)
    if x == 16:
        return x16
    x17 = extract(x12, x16)
    if x == 17:
        return x17
    x18 = add(x11, x17)
    if x == 18:
        return x18
    x19 = x9(x18)
    if x == 19:
        return x19
    O = fill(x2, x8, x19)
    return O

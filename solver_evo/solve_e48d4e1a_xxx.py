def solve_e48d4e1a_one(S, I):
    return fill(canvas(BLACK, shape_t(I)), get_color_rank_t(fill(I, BLACK, f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), L1), fork(combine, vfrontier, hfrontier)(add(multiply(DOWN_LEFT, size_f(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))))), extract(f_ofcolor(I, get_color_rank_t(fill(I, BLACK, f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), L1)), matcher(chain(rbind(colorcount_f, get_color_rank_t(fill(I, BLACK, f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), L1)), rbind(toobject, I), dneighbors), YELLOW)))))


def solve_e48d4e1a(S, I):
    x1 = shape_t(I)
    x2 = canvas(BLACK, x1)
    x3 = identity(p_g)
    x4 = rbind(get_nth_t, F0)
    x5 = c_iz_n(S, x3, x4)
    x6 = f_ofcolor(I, x5)
    x7 = fill(I, BLACK, x6)
    x8 = get_color_rank_t(x7, L1)
    x9 = fork(combine, vfrontier, hfrontier)
    x10 = size_f(x6)
    x11 = multiply(DOWN_LEFT, x10)
    x12 = f_ofcolor(I, x8)
    x13 = rbind(colorcount_f, x8)
    x14 = rbind(toobject, I)
    x15 = chain(x13, x14, dneighbors)
    x16 = matcher(x15, YELLOW)
    x17 = extract(x12, x16)
    x18 = add(x11, x17)
    x19 = x9(x18)
    O = fill(x2, x8, x19)
    return O

def solve_e48d4e1a_one(S, I):
    return fill(canvas(ZERO, shape_t(I)), get_color_rank_t(fill(I, ZERO, f_ofcolor(I, FIVE)), L1), fork(combine, vfrontier, hfrontier)(add(multiply(DOWN_LEFT, size_f(f_ofcolor(I, FIVE))), extract(f_ofcolor(I, get_color_rank_t(fill(I, ZERO, f_ofcolor(I, FIVE)), L1)), matcher(chain(rbind(colorcount_f, get_color_rank_t(fill(I, ZERO, f_ofcolor(I, FIVE)), L1)), rbind(toobject, I), dneighbors), FOUR)))))


def solve_e48d4e1a(S, I):
    x1 = shape_t(I)
    x2 = canvas(ZERO, x1)
    x3 = f_ofcolor(I, FIVE)
    x4 = fill(I, ZERO, x3)
    x5 = get_color_rank_t(x4, L1)
    x6 = fork(combine, vfrontier, hfrontier)
    x7 = size_f(x3)
    x8 = multiply(DOWN_LEFT, x7)
    x9 = f_ofcolor(I, x5)
    x10 = rbind(colorcount_f, x5)
    x11 = rbind(toobject, I)
    x12 = chain(x10, x11, dneighbors)
    x13 = matcher(x12, FOUR)
    x14 = extract(x9, x13)
    x15 = add(x8, x14)
    x16 = x6(x15)
    O = fill(x2, x5, x16)
    return O

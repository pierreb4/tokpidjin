def solve_e48d4e1a_one(S, I):
    return fill(canvas(ZERO, shape_t(I)), get_color_rank_t(fill(I, ZERO, f_ofcolor(I, FIVE)), L1), fork(combine, vfrontier, hfrontier)(add(multiply(DOWN_LEFT, size_f(f_ofcolor(I, FIVE))), extract(f_ofcolor(I, get_color_rank_t(fill(I, ZERO, f_ofcolor(I, FIVE)), L1)), matcher(chain(rbind(colorcount_f, get_color_rank_t(fill(I, ZERO, f_ofcolor(I, FIVE)), L1)), rbind(toobject, I), dneighbors), FOUR)))))


def solve_e48d4e1a(S, I, x=0):
    x1 = shape_t(I)
    if x == 1:
        return x1
    x2 = canvas(ZERO, x1)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, FIVE)
    if x == 3:
        return x3
    x4 = fill(I, ZERO, x3)
    if x == 4:
        return x4
    x5 = get_color_rank_t(x4, L1)
    if x == 5:
        return x5
    x6 = fork(combine, vfrontier, hfrontier)
    if x == 6:
        return x6
    x7 = size_f(x3)
    if x == 7:
        return x7
    x8 = multiply(DOWN_LEFT, x7)
    if x == 8:
        return x8
    x9 = f_ofcolor(I, x5)
    if x == 9:
        return x9
    x10 = rbind(colorcount_f, x5)
    if x == 10:
        return x10
    x11 = rbind(toobject, I)
    if x == 11:
        return x11
    x12 = chain(x10, x11, dneighbors)
    if x == 12:
        return x12
    x13 = matcher(x12, FOUR)
    if x == 13:
        return x13
    x14 = extract(x9, x13)
    if x == 14:
        return x14
    x15 = add(x8, x14)
    if x == 15:
        return x15
    x16 = x6(x15)
    if x == 16:
        return x16
    O = fill(x2, x5, x16)
    return O

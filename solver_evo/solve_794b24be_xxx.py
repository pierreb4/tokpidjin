def solve_794b24be_one(S, I):
    return fill(canvas(BLACK, THREE_BY_THREE), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), branch(equality(size_f(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), YELLOW), insert(UNITY, connect(ORIGIN, tojvec(decrement(size_f(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))))))), connect(ORIGIN, tojvec(decrement(size_f(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))))))))


def solve_794b24be(S, I, x=0):
    x1 = canvas(BLACK, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = identity(p_g)
    if x == 2:
        return x2
    x3 = rbind(get_nth_t, F0)
    if x == 3:
        return x3
    x4 = c_zo_n(S, x2, x3)
    if x == 4:
        return x4
    x5 = c_iz_n(S, x2, x3)
    if x == 5:
        return x5
    x6 = f_ofcolor(I, x5)
    if x == 6:
        return x6
    x7 = size_f(x6)
    if x == 7:
        return x7
    x8 = equality(x7, YELLOW)
    if x == 8:
        return x8
    x9 = decrement(x7)
    if x == 9:
        return x9
    x10 = tojvec(x9)
    if x == 10:
        return x10
    x11 = connect(ORIGIN, x10)
    if x == 11:
        return x11
    x12 = insert(UNITY, x11)
    if x == 12:
        return x12
    x13 = branch(x8, x12, x11)
    if x == 13:
        return x13
    O = fill(x1, x4, x13)
    return O

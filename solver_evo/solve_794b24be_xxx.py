def solve_794b24be_one(S, I):
    return fill(canvas(BLACK, THREE_BY_THREE), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), branch(equality(size_f(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), YELLOW), insert(UNITY, connect(ORIGIN, tojvec(decrement(size_f(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))))))), connect(ORIGIN, tojvec(decrement(size_f(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))))))))


def solve_794b24be(S, I):
    x1 = canvas(BLACK, THREE_BY_THREE)
    x2 = identity(p_g)
    x3 = rbind(get_nth_t, F0)
    x4 = c_zo_n(S, x2, x3)
    x5 = c_iz_n(S, x2, x3)
    x6 = f_ofcolor(I, x5)
    x7 = size_f(x6)
    x8 = equality(x7, YELLOW)
    x9 = decrement(x7)
    x10 = tojvec(x9)
    x11 = connect(ORIGIN, x10)
    x12 = insert(UNITY, x11)
    x13 = branch(x8, x12, x11)
    O = fill(x1, x4, x13)
    return O

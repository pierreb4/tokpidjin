def solve_794b24be_one(S, I):
    return fill(canvas(ZERO, THREE_BY_THREE), TWO, branch(equality(size_f(f_ofcolor(I, ONE)), FOUR), insert(UNITY, connect(ORIGIN, tojvec(decrement(size_f(f_ofcolor(I, ONE)))))), connect(ORIGIN, tojvec(decrement(size_f(f_ofcolor(I, ONE)))))))


def solve_794b24be(S, I):
    x1 = canvas(ZERO, THREE_BY_THREE)
    x2 = f_ofcolor(I, ONE)
    x3 = size_f(x2)
    x4 = equality(x3, FOUR)
    x5 = decrement(x3)
    x6 = tojvec(x5)
    x7 = connect(ORIGIN, x6)
    x8 = insert(UNITY, x7)
    x9 = branch(x4, x8, x7)
    O = fill(x1, TWO, x9)
    return O

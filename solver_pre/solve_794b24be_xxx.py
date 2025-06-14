def solve_794b24be_one(S, I):
    return fill(canvas(ZERO, THREE_BY_THREE), TWO, branch(equality(size_f(f_ofcolor(I, ONE)), FOUR), insert(UNITY, connect(ORIGIN, tojvec(decrement(size_f(f_ofcolor(I, ONE)))))), connect(ORIGIN, tojvec(decrement(size_f(f_ofcolor(I, ONE)))))))


def solve_794b24be(S, I, x=0):
    x1 = canvas(ZERO, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, ONE)
    if x == 2:
        return x2
    x3 = size_f(x2)
    if x == 3:
        return x3
    x4 = equality(x3, FOUR)
    if x == 4:
        return x4
    x5 = decrement(x3)
    if x == 5:
        return x5
    x6 = tojvec(x5)
    if x == 6:
        return x6
    x7 = connect(ORIGIN, x6)
    if x == 7:
        return x7
    x8 = insert(UNITY, x7)
    if x == 8:
        return x8
    x9 = branch(x4, x8, x7)
    if x == 9:
        return x9
    O = fill(x1, TWO, x9)
    return O

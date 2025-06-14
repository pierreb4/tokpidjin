def solve_d8c310e9_one(S, I):
    return paint(paint(I, shift(get_nth_f(o_g(I, R1), F0), tojvec(hperiod(get_nth_f(o_g(I, R1), F0))))), shift(get_nth_f(o_g(I, R1), F0), tojvec(multiply(hperiod(get_nth_f(o_g(I, R1), F0)), THREE))))


def solve_d8c310e9(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = hperiod(x2)
    if x == 3:
        return x3
    x4 = tojvec(x3)
    if x == 4:
        return x4
    x5 = shift(x2, x4)
    if x == 5:
        return x5
    x6 = paint(I, x5)
    if x == 6:
        return x6
    x7 = multiply(x3, THREE)
    if x == 7:
        return x7
    x8 = tojvec(x7)
    if x == 8:
        return x8
    x9 = shift(x2, x8)
    if x == 9:
        return x9
    O = paint(x6, x9)
    return O

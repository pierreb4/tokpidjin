def solve_d8c310e9_one(S, I):
    return paint(paint(I, shift(get_nth_f(o_g(I, R1), F0), tojvec(hperiod(get_nth_f(o_g(I, R1), F0))))), shift(get_nth_f(o_g(I, R1), F0), tojvec(multiply(hperiod(get_nth_f(o_g(I, R1), F0)), THREE))))


def solve_d8c310e9(S, I):
    x1 = o_g(I, R1)
    x2 = get_nth_f(x1, F0)
    x3 = hperiod(x2)
    x4 = tojvec(x3)
    x5 = shift(x2, x4)
    x6 = paint(I, x5)
    x7 = multiply(x3, THREE)
    x8 = tojvec(x7)
    x9 = shift(x2, x8)
    O = paint(x6, x9)
    return O

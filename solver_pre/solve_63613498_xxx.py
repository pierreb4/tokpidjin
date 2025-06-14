def solve_63613498_one(S, I):
    return paint(fill(I, FIVE, mfilter_f(o_g(I, R5), matcher(compose(toindices, normalize), normalize(difference(asindices(crop(I, ORIGIN, THREE_BY_THREE)), f_ofcolor(crop(I, ORIGIN, THREE_BY_THREE), ZERO)))))), asobject(crop(I, ORIGIN, THREE_BY_THREE)))


def solve_63613498(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = compose(toindices, normalize)
    if x == 2:
        return x2
    x3 = crop(I, ORIGIN, THREE_BY_THREE)
    if x == 3:
        return x3
    x4 = asindices(x3)
    if x == 4:
        return x4
    x5 = f_ofcolor(x3, ZERO)
    if x == 5:
        return x5
    x6 = difference(x4, x5)
    if x == 6:
        return x6
    x7 = normalize(x6)
    if x == 7:
        return x7
    x8 = matcher(x2, x7)
    if x == 8:
        return x8
    x9 = mfilter_f(x1, x8)
    if x == 9:
        return x9
    x10 = fill(I, FIVE, x9)
    if x == 10:
        return x10
    x11 = asobject(x3)
    if x == 11:
        return x11
    O = paint(x10, x11)
    return O

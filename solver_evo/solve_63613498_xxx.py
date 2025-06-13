def solve_63613498_one(S, I):
    return paint(fill(I, GRAY, mfilter_f(o_g(I, R5), matcher(compose(toindices, normalize), normalize(difference(asindices(crop(I, ORIGIN, THREE_BY_THREE)), f_ofcolor(crop(I, ORIGIN, THREE_BY_THREE), BLACK)))))), asobject(crop(I, ORIGIN, THREE_BY_THREE)))


def solve_63613498(S, I):
    x1 = o_g(I, R5)
    x2 = compose(toindices, normalize)
    x3 = crop(I, ORIGIN, THREE_BY_THREE)
    x4 = asindices(x3)
    x5 = f_ofcolor(x3, BLACK)
    x6 = difference(x4, x5)
    x7 = normalize(x6)
    x8 = matcher(x2, x7)
    x9 = mfilter_f(x1, x8)
    x10 = fill(I, GRAY, x9)
    x11 = asobject(x3)
    O = paint(x10, x11)
    return O

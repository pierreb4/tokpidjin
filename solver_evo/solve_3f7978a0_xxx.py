def solve_3f7978a0_one(S, I):
    return crop(I, subtract(corner(extract(fgpartition(I), matcher(color, GRAY)), R0), DOWN), add(shape_f(extract(fgpartition(I), matcher(color, GRAY))), TWO_BY_ZERO))


def solve_3f7978a0(S, I, x=0):
    x1 = fgpartition(I)
    if x == 1:
        return x1
    x2 = matcher(color, GRAY)
    if x == 2:
        return x2
    x3 = extract(x1, x2)
    if x == 3:
        return x3
    x4 = corner(x3, R0)
    if x == 4:
        return x4
    x5 = subtract(x4, DOWN)
    if x == 5:
        return x5
    x6 = shape_f(x3)
    if x == 6:
        return x6
    x7 = add(x6, TWO_BY_ZERO)
    if x == 7:
        return x7
    O = crop(I, x5, x7)
    return O

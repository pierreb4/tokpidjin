def solve_3f7978a0_one(S, I):
    return crop(I, subtract(corner(extract(fgpartition(I), matcher(color, FIVE)), R0), DOWN), add(shape_f(extract(fgpartition(I), matcher(color, FIVE))), TWO_BY_ZERO))


def solve_3f7978a0(S, I):
    x1 = fgpartition(I)
    x2 = matcher(color, FIVE)
    x3 = extract(x1, x2)
    x4 = corner(x3, R0)
    x5 = subtract(x4, DOWN)
    x6 = shape_f(x3)
    x7 = add(x6, TWO_BY_ZERO)
    O = crop(I, x5, x7)
    return O

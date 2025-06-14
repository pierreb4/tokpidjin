def solve_1e32b0e9_one(S, I):
    return underfill(I, get_nth_f(difference(difference(palette_f(asobject(I)), palette_f(extract(partition(crop(I, ORIGIN, astuple(divide(subtract(height_t(I), TWO), THREE), divide(subtract(height_t(I), TWO), THREE)))), compose(flip, matcher(color, ZERO))))), initset(get_color_rank_t(I, F0))), F0), mapply(lbind(shift, extract(partition(crop(I, ORIGIN, astuple(divide(subtract(height_t(I), TWO), THREE), divide(subtract(height_t(I), TWO), THREE)))), compose(flip, matcher(color, ZERO)))), papply(astuple, papply(add, apply(lbind(multiply, divide(subtract(height_t(I), TWO), THREE)), apply(rbind(get_nth_f, F0), totuple(product(interval(ZERO, THREE, ONE), interval(ZERO, THREE, ONE))))), apply(rbind(get_nth_f, F0), totuple(product(interval(ZERO, THREE, ONE), interval(ZERO, THREE, ONE))))), papply(add, apply(lbind(multiply, divide(subtract(height_t(I), TWO), THREE)), apply(rbind(get_nth_f, L1), totuple(product(interval(ZERO, THREE, ONE), interval(ZERO, THREE, ONE))))), apply(rbind(get_nth_f, L1), totuple(product(interval(ZERO, THREE, ONE), interval(ZERO, THREE, ONE))))))))


def solve_1e32b0e9(S, I, x=0):
    x1 = asobject(I)
    if x == 1:
        return x1
    x2 = palette_f(x1)
    if x == 2:
        return x2
    x3 = height_t(I)
    if x == 3:
        return x3
    x4 = subtract(x3, TWO)
    if x == 4:
        return x4
    x5 = divide(x4, THREE)
    if x == 5:
        return x5
    x6 = astuple(x5, x5)
    if x == 6:
        return x6
    x7 = crop(I, ORIGIN, x6)
    if x == 7:
        return x7
    x8 = partition(x7)
    if x == 8:
        return x8
    x9 = matcher(color, ZERO)
    if x == 9:
        return x9
    x10 = compose(flip, x9)
    if x == 10:
        return x10
    x11 = extract(x8, x10)
    if x == 11:
        return x11
    x12 = palette_f(x11)
    if x == 12:
        return x12
    x13 = difference(x2, x12)
    if x == 13:
        return x13
    x14 = get_color_rank_t(I, F0)
    if x == 14:
        return x14
    x15 = initset(x14)
    if x == 15:
        return x15
    x16 = difference(x13, x15)
    if x == 16:
        return x16
    x17 = get_nth_f(x16, F0)
    if x == 17:
        return x17
    x18 = lbind(shift, x11)
    if x == 18:
        return x18
    x19 = lbind(multiply, x5)
    if x == 19:
        return x19
    x20 = rbind(get_nth_f, F0)
    if x == 20:
        return x20
    x21 = interval(ZERO, THREE, ONE)
    if x == 21:
        return x21
    x22 = product(x21, x21)
    if x == 22:
        return x22
    x23 = totuple(x22)
    if x == 23:
        return x23
    x24 = apply(x20, x23)
    if x == 24:
        return x24
    x25 = apply(x19, x24)
    if x == 25:
        return x25
    x26 = papply(add, x25, x24)
    if x == 26:
        return x26
    x27 = rbind(get_nth_f, L1)
    if x == 27:
        return x27
    x28 = apply(x27, x23)
    if x == 28:
        return x28
    x29 = apply(x19, x28)
    if x == 29:
        return x29
    x30 = papply(add, x29, x28)
    if x == 30:
        return x30
    x31 = papply(astuple, x26, x30)
    if x == 31:
        return x31
    x32 = mapply(x18, x31)
    if x == 32:
        return x32
    O = underfill(I, x17, x32)
    return O

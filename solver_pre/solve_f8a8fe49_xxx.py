def solve_f8a8fe49_one(S, I):
    return paint(paint(replace(I, FIVE, ZERO), shift(shift(get_nth_t(apply(compose(normalize, asobject), branch(portrait_f(get_nth_f(colorfilter(o_g(I, R5), TWO), F0)), hsplit, vsplit)(branch(portrait_f(get_nth_f(colorfilter(o_g(I, R5), TWO), F0)), rbind(mir_rot_t, R2), rbind(mir_rot_t, R0))(trim(subgrid(f_ofcolor(I, TWO), I))), TWO)), L1), increment(corner(f_ofcolor(I, TWO), R0))), invert(compose(branch(portrait_f(get_nth_f(colorfilter(o_g(I, R5), TWO), F0)), tojvec, toivec), increment)(branch(portrait_f(get_nth_f(colorfilter(o_g(I, R5), TWO), F0)), width_f, height_f)(get_nth_t(apply(compose(normalize, asobject), branch(portrait_f(get_nth_f(colorfilter(o_g(I, R5), TWO), F0)), hsplit, vsplit)(branch(portrait_f(get_nth_f(colorfilter(o_g(I, R5), TWO), F0)), rbind(mir_rot_t, R2), rbind(mir_rot_t, R0))(trim(subgrid(f_ofcolor(I, TWO), I))), TWO)), L1)))))), shift(shift(get_nth_f(apply(compose(normalize, asobject), branch(portrait_f(get_nth_f(colorfilter(o_g(I, R5), TWO), F0)), hsplit, vsplit)(branch(portrait_f(get_nth_f(colorfilter(o_g(I, R5), TWO), F0)), rbind(mir_rot_t, R2), rbind(mir_rot_t, R0))(trim(subgrid(f_ofcolor(I, TWO), I))), TWO)), F0), increment(corner(f_ofcolor(I, TWO), R0))), compose(branch(portrait_f(get_nth_f(colorfilter(o_g(I, R5), TWO), F0)), tojvec, toivec), increment)(double(branch(portrait_f(get_nth_f(colorfilter(o_g(I, R5), TWO), F0)), width_f, height_f)(get_nth_t(apply(compose(normalize, asobject), branch(portrait_f(get_nth_f(colorfilter(o_g(I, R5), TWO), F0)), hsplit, vsplit)(branch(portrait_f(get_nth_f(colorfilter(o_g(I, R5), TWO), F0)), rbind(mir_rot_t, R2), rbind(mir_rot_t, R0))(trim(subgrid(f_ofcolor(I, TWO), I))), TWO)), L1))))))


def solve_f8a8fe49(S, I, x=0):
    x1 = replace(I, FIVE, ZERO)
    if x == 1:
        return x1
    x2 = compose(normalize, asobject)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = colorfilter(x3, TWO)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = portrait_f(x5)
    if x == 6:
        return x6
    x7 = branch(x6, hsplit, vsplit)
    if x == 7:
        return x7
    x8 = rbind(mir_rot_t, R2)
    if x == 8:
        return x8
    x9 = rbind(mir_rot_t, R0)
    if x == 9:
        return x9
    x10 = branch(x6, x8, x9)
    if x == 10:
        return x10
    x11 = f_ofcolor(I, TWO)
    if x == 11:
        return x11
    x12 = subgrid(x11, I)
    if x == 12:
        return x12
    x13 = trim(x12)
    if x == 13:
        return x13
    x14 = x10(x13)
    if x == 14:
        return x14
    x15 = x7(x14, TWO)
    if x == 15:
        return x15
    x16 = apply(x2, x15)
    if x == 16:
        return x16
    x17 = get_nth_t(x16, L1)
    if x == 17:
        return x17
    x18 = corner(x11, R0)
    if x == 18:
        return x18
    x19 = increment(x18)
    if x == 19:
        return x19
    x20 = shift(x17, x19)
    if x == 20:
        return x20
    x21 = branch(x6, tojvec, toivec)
    if x == 21:
        return x21
    x22 = compose(x21, increment)
    if x == 22:
        return x22
    x23 = branch(x6, width_f, height_f)
    if x == 23:
        return x23
    x24 = x23(x17)
    if x == 24:
        return x24
    x25 = x22(x24)
    if x == 25:
        return x25
    x26 = invert(x25)
    if x == 26:
        return x26
    x27 = shift(x20, x26)
    if x == 27:
        return x27
    x28 = paint(x1, x27)
    if x == 28:
        return x28
    x29 = get_nth_f(x16, F0)
    if x == 29:
        return x29
    x30 = shift(x29, x19)
    if x == 30:
        return x30
    x31 = double(x24)
    if x == 31:
        return x31
    x32 = x22(x31)
    if x == 32:
        return x32
    x33 = shift(x30, x32)
    if x == 33:
        return x33
    O = paint(x28, x33)
    return O

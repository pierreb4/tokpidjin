def solve_780d0b14_one(S, I):
    return mir_rot_t(sfilter(mir_rot_t(sfilter(paint(fill(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), asindices(I)), pair(apply(color, totuple(sfilter(o_g(I, R7), compose(rbind(greater, RED), size)))), apply(center, totuple(sfilter(o_g(I, R7), compose(rbind(greater, RED), size)))))), chain(rbind(greater, BLUE), size, compose(dedupe, totuple))), R4), chain(rbind(greater, BLUE), size, compose(dedupe, totuple))), R6)


def solve_780d0b14(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_iz_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = asindices(I)
    if x == 4:
        return x4
    x5 = fill(I, x3, x4)
    if x == 5:
        return x5
    x6 = o_g(I, R7)
    if x == 6:
        return x6
    x7 = rbind(greater, RED)
    if x == 7:
        return x7
    x8 = compose(x7, size)
    if x == 8:
        return x8
    x9 = sfilter(x6, x8)
    if x == 9:
        return x9
    x10 = totuple(x9)
    if x == 10:
        return x10
    x11 = apply(color, x10)
    if x == 11:
        return x11
    x12 = apply(center, x10)
    if x == 12:
        return x12
    x13 = pair(x11, x12)
    if x == 13:
        return x13
    x14 = paint(x5, x13)
    if x == 14:
        return x14
    x15 = rbind(greater, BLUE)
    if x == 15:
        return x15
    x16 = compose(dedupe, totuple)
    if x == 16:
        return x16
    x17 = chain(x15, size, x16)
    if x == 17:
        return x17
    x18 = sfilter(x14, x17)
    if x == 18:
        return x18
    x19 = mir_rot_t(x18, R4)
    if x == 19:
        return x19
    x20 = sfilter(x19, x17)
    if x == 20:
        return x20
    O = mir_rot_t(x20, R6)
    return O

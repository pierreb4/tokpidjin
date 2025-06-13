def solve_780d0b14_one(S, I):
    return mir_rot_t(sfilter(mir_rot_t(sfilter(paint(fill(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), asindices(I)), pair(apply(color, totuple(sfilter(o_g(I, R7), compose(rbind(greater, RED), size)))), apply(center, totuple(sfilter(o_g(I, R7), compose(rbind(greater, RED), size)))))), chain(rbind(greater, BLUE), size, compose(dedupe, totuple))), R4), chain(rbind(greater, BLUE), size, compose(dedupe, totuple))), R6)


def solve_780d0b14(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_iz_n(S, x1, x2)
    x4 = asindices(I)
    x5 = fill(I, x3, x4)
    x6 = o_g(I, R7)
    x7 = rbind(greater, RED)
    x8 = compose(x7, size)
    x9 = sfilter(x6, x8)
    x10 = totuple(x9)
    x11 = apply(color, x10)
    x12 = apply(center, x10)
    x13 = pair(x11, x12)
    x14 = paint(x5, x13)
    x15 = rbind(greater, BLUE)
    x16 = compose(dedupe, totuple)
    x17 = chain(x15, size, x16)
    x18 = sfilter(x14, x17)
    x19 = mir_rot_t(x18, R4)
    x20 = sfilter(x19, x17)
    O = mir_rot_t(x20, R6)
    return O

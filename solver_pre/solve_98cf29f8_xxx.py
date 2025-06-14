def solve_98cf29f8_one(S, I):
    return fill(cover(I, other_f(fgpartition(I), extract(fgpartition(I), fork(equality, size, fork(multiply, height_f, width_f))))), color(other_f(fgpartition(I), extract(fgpartition(I), fork(equality, size, fork(multiply, height_f, width_f))))), shift(backdrop(outbox(sfilter_f(other_f(fgpartition(I), extract(fgpartition(I), fork(equality, size, fork(multiply, height_f, width_f)))), chain(rbind(greater, THREE), rbind(colorcount_f, color(other_f(fgpartition(I), extract(fgpartition(I), fork(equality, size, fork(multiply, height_f, width_f)))))), chain(rbind(toobject, I), ineighbors, rbind(get_nth_f, L1)))))), gravitate(backdrop(outbox(sfilter_f(other_f(fgpartition(I), extract(fgpartition(I), fork(equality, size, fork(multiply, height_f, width_f)))), chain(rbind(greater, THREE), rbind(colorcount_f, color(other_f(fgpartition(I), extract(fgpartition(I), fork(equality, size, fork(multiply, height_f, width_f)))))), chain(rbind(toobject, I), ineighbors, rbind(get_nth_f, L1)))))), extract(fgpartition(I), fork(equality, size, fork(multiply, height_f, width_f))))))


def solve_98cf29f8(S, I, x=0):
    x1 = fgpartition(I)
    if x == 1:
        return x1
    x2 = fork(multiply, height_f, width_f)
    if x == 2:
        return x2
    x3 = fork(equality, size, x2)
    if x == 3:
        return x3
    x4 = extract(x1, x3)
    if x == 4:
        return x4
    x5 = other_f(x1, x4)
    if x == 5:
        return x5
    x6 = cover(I, x5)
    if x == 6:
        return x6
    x7 = color(x5)
    if x == 7:
        return x7
    x8 = rbind(greater, THREE)
    if x == 8:
        return x8
    x9 = rbind(colorcount_f, x7)
    if x == 9:
        return x9
    x10 = rbind(toobject, I)
    if x == 10:
        return x10
    x11 = rbind(get_nth_f, L1)
    if x == 11:
        return x11
    x12 = chain(x10, ineighbors, x11)
    if x == 12:
        return x12
    x13 = chain(x8, x9, x12)
    if x == 13:
        return x13
    x14 = sfilter_f(x5, x13)
    if x == 14:
        return x14
    x15 = outbox(x14)
    if x == 15:
        return x15
    x16 = backdrop(x15)
    if x == 16:
        return x16
    x17 = gravitate(x16, x4)
    if x == 17:
        return x17
    x18 = shift(x16, x17)
    if x == 18:
        return x18
    O = fill(x6, x7, x18)
    return O

def solve_98cf29f8_one(S, I):
    return fill(cover(I, other_f(fgpartition(I), extract(fgpartition(I), fork(equality, size, fork(multiply, height_f, width_f))))), color(other_f(fgpartition(I), extract(fgpartition(I), fork(equality, size, fork(multiply, height_f, width_f))))), shift(backdrop(outbox(sfilter_f(other_f(fgpartition(I), extract(fgpartition(I), fork(equality, size, fork(multiply, height_f, width_f)))), chain(rbind(greater, THREE), rbind(colorcount_f, color(other_f(fgpartition(I), extract(fgpartition(I), fork(equality, size, fork(multiply, height_f, width_f)))))), chain(rbind(toobject, I), ineighbors, rbind(get_nth_f, L1)))))), gravitate(backdrop(outbox(sfilter_f(other_f(fgpartition(I), extract(fgpartition(I), fork(equality, size, fork(multiply, height_f, width_f)))), chain(rbind(greater, THREE), rbind(colorcount_f, color(other_f(fgpartition(I), extract(fgpartition(I), fork(equality, size, fork(multiply, height_f, width_f)))))), chain(rbind(toobject, I), ineighbors, rbind(get_nth_f, L1)))))), extract(fgpartition(I), fork(equality, size, fork(multiply, height_f, width_f))))))


def solve_98cf29f8(S, I):
    x1 = fgpartition(I)
    x2 = fork(multiply, height_f, width_f)
    x3 = fork(equality, size, x2)
    x4 = extract(x1, x3)
    x5 = other_f(x1, x4)
    x6 = cover(I, x5)
    x7 = color(x5)
    x8 = rbind(greater, THREE)
    x9 = rbind(colorcount_f, x7)
    x10 = rbind(toobject, I)
    x11 = rbind(get_nth_f, L1)
    x12 = chain(x10, ineighbors, x11)
    x13 = chain(x8, x9, x12)
    x14 = sfilter_f(x5, x13)
    x15 = outbox(x14)
    x16 = backdrop(x15)
    x17 = gravitate(x16, x4)
    x18 = shift(x16, x17)
    O = fill(x6, x7, x18)
    return O

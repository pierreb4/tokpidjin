def solve_776ffc46_one(S, I):
    return fill(I, color(normalize(sfilter_f(asobject(subgrid(inbox(extract(colorfilter(o_g(I, R5), GRAY), fork(equality, toindices, box))), I)), compose(flip, matcher(rbind(get_nth_f, F0), BLACK))))), mfilter_f(o_g(I, R5), matcher(compose(toindices, normalize), toindices(normalize(sfilter_f(asobject(subgrid(inbox(extract(colorfilter(o_g(I, R5), GRAY), fork(equality, toindices, box))), I)), compose(flip, matcher(rbind(get_nth_f, F0), BLACK))))))))


def solve_776ffc46(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = colorfilter(x1, GRAY)
    if x == 2:
        return x2
    x3 = fork(equality, toindices, box)
    if x == 3:
        return x3
    x4 = extract(x2, x3)
    if x == 4:
        return x4
    x5 = inbox(x4)
    if x == 5:
        return x5
    x6 = subgrid(x5, I)
    if x == 6:
        return x6
    x7 = asobject(x6)
    if x == 7:
        return x7
    x8 = rbind(get_nth_f, F0)
    if x == 8:
        return x8
    x9 = matcher(x8, BLACK)
    if x == 9:
        return x9
    x10 = compose(flip, x9)
    if x == 10:
        return x10
    x11 = sfilter_f(x7, x10)
    if x == 11:
        return x11
    x12 = normalize(x11)
    if x == 12:
        return x12
    x13 = color(x12)
    if x == 13:
        return x13
    x14 = compose(toindices, normalize)
    if x == 14:
        return x14
    x15 = toindices(x12)
    if x == 15:
        return x15
    x16 = matcher(x14, x15)
    if x == 16:
        return x16
    x17 = mfilter_f(x1, x16)
    if x == 17:
        return x17
    O = fill(I, x13, x17)
    return O

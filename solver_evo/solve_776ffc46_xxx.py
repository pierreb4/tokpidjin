def solve_776ffc46_one(S, I):
    return fill(I, color(normalize(sfilter_f(asobject(subgrid(inbox(extract(colorfilter(o_g(I, R5), GRAY), fork(equality, toindices, box))), I)), compose(flip, matcher(rbind(get_nth_f, F0), BLACK))))), mfilter_f(o_g(I, R5), matcher(compose(toindices, normalize), toindices(normalize(sfilter_f(asobject(subgrid(inbox(extract(colorfilter(o_g(I, R5), GRAY), fork(equality, toindices, box))), I)), compose(flip, matcher(rbind(get_nth_f, F0), BLACK))))))))


def solve_776ffc46(S, I):
    x1 = o_g(I, R5)
    x2 = colorfilter(x1, GRAY)
    x3 = fork(equality, toindices, box)
    x4 = extract(x2, x3)
    x5 = inbox(x4)
    x6 = subgrid(x5, I)
    x7 = asobject(x6)
    x8 = rbind(get_nth_f, F0)
    x9 = matcher(x8, BLACK)
    x10 = compose(flip, x9)
    x11 = sfilter_f(x7, x10)
    x12 = normalize(x11)
    x13 = color(x12)
    x14 = compose(toindices, normalize)
    x15 = toindices(x12)
    x16 = matcher(x14, x15)
    x17 = mfilter_f(x1, x16)
    O = fill(I, x13, x17)
    return O

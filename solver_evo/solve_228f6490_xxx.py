def solve_228f6490_one(S, I):
    return move(move(I, extract(difference(o_g(I, R4), colorfilter(o_g(I, R4), BLACK)), matcher(compose(normalize, toindices), compose(normalize, toindices)(get_nth_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I))), F0)))), subtract(corner(get_nth_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I))), F0), R0), corner(extract(difference(o_g(I, R4), colorfilter(o_g(I, R4), BLACK)), matcher(compose(normalize, toindices), compose(normalize, toindices)(get_nth_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I))), F0)))), R0))), extract(difference(o_g(I, R4), colorfilter(o_g(I, R4), BLACK)), matcher(compose(normalize, toindices), compose(normalize, toindices)(get_nth_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I))), L1)))), subtract(corner(get_nth_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I))), L1), R0), corner(extract(difference(o_g(I, R4), colorfilter(o_g(I, R4), BLACK)), matcher(compose(normalize, toindices), compose(normalize, toindices)(get_nth_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I))), L1)))), R0)))


def solve_228f6490(S, I):
    x1 = o_g(I, R4)
    x2 = colorfilter(x1, BLACK)
    x3 = difference(x1, x2)
    x4 = compose(normalize, toindices)
    x5 = rbind(bordering, I)
    x6 = compose(flip, x5)
    x7 = sfilter_f(x2, x6)
    x8 = get_nth_f(x7, F0)
    x9 = x4(x8)
    x10 = matcher(x4, x9)
    x11 = extract(x3, x10)
    x12 = corner(x8, R0)
    x13 = corner(x11, R0)
    x14 = subtract(x12, x13)
    x15 = move(I, x11, x14)
    x16 = get_nth_f(x7, L1)
    x17 = x4(x16)
    x18 = matcher(x4, x17)
    x19 = extract(x3, x18)
    x20 = corner(x16, R0)
    x21 = corner(x19, R0)
    x22 = subtract(x20, x21)
    O = move(x15, x19, x22)
    return O

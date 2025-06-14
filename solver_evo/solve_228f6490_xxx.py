def solve_228f6490_one(S, I):
    return move(move(I, extract(difference(o_g(I, R4), colorfilter(o_g(I, R4), BLACK)), matcher(compose(normalize, toindices), compose(normalize, toindices)(get_nth_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I))), F0)))), subtract(corner(get_nth_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I))), F0), R0), corner(extract(difference(o_g(I, R4), colorfilter(o_g(I, R4), BLACK)), matcher(compose(normalize, toindices), compose(normalize, toindices)(get_nth_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I))), F0)))), R0))), extract(difference(o_g(I, R4), colorfilter(o_g(I, R4), BLACK)), matcher(compose(normalize, toindices), compose(normalize, toindices)(get_nth_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I))), L1)))), subtract(corner(get_nth_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I))), L1), R0), corner(extract(difference(o_g(I, R4), colorfilter(o_g(I, R4), BLACK)), matcher(compose(normalize, toindices), compose(normalize, toindices)(get_nth_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), compose(flip, rbind(bordering, I))), L1)))), R0)))


def solve_228f6490(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, BLACK)
    if x == 2:
        return x2
    x3 = difference(x1, x2)
    if x == 3:
        return x3
    x4 = compose(normalize, toindices)
    if x == 4:
        return x4
    x5 = rbind(bordering, I)
    if x == 5:
        return x5
    x6 = compose(flip, x5)
    if x == 6:
        return x6
    x7 = sfilter_f(x2, x6)
    if x == 7:
        return x7
    x8 = get_nth_f(x7, F0)
    if x == 8:
        return x8
    x9 = x4(x8)
    if x == 9:
        return x9
    x10 = matcher(x4, x9)
    if x == 10:
        return x10
    x11 = extract(x3, x10)
    if x == 11:
        return x11
    x12 = corner(x8, R0)
    if x == 12:
        return x12
    x13 = corner(x11, R0)
    if x == 13:
        return x13
    x14 = subtract(x12, x13)
    if x == 14:
        return x14
    x15 = move(I, x11, x14)
    if x == 15:
        return x15
    x16 = get_nth_f(x7, L1)
    if x == 16:
        return x16
    x17 = x4(x16)
    if x == 17:
        return x17
    x18 = matcher(x4, x17)
    if x == 18:
        return x18
    x19 = extract(x3, x18)
    if x == 19:
        return x19
    x20 = corner(x16, R0)
    if x == 20:
        return x20
    x21 = corner(x19, R0)
    if x == 21:
        return x21
    x22 = subtract(x20, x21)
    if x == 22:
        return x22
    O = move(x15, x19, x22)
    return O

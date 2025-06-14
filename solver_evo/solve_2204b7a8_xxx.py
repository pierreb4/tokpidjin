def solve_2204b7a8_one(S, I):
    return branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), hconcat, vconcat)(replace(branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), lefthalf, tophalf)(I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), index(branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), lefthalf, tophalf)(I), ORIGIN)), replace(branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), righthalf, bottomhalf)(I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), index(branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), righthalf, bottomhalf)(I), decrement(shape_t(branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), righthalf, bottomhalf)(I))))))


def solve_2204b7a8(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = lbind(sfilter, x1)
    if x == 2:
        return x2
    x3 = compose(size, x2)
    if x == 3:
        return x3
    x4 = x3(vline_o)
    if x == 4:
        return x4
    x5 = x3(hline_o)
    if x == 5:
        return x5
    x6 = greater(x4, x5)
    if x == 6:
        return x6
    x7 = branch(x6, hconcat, vconcat)
    if x == 7:
        return x7
    x8 = branch(x6, lefthalf, tophalf)
    if x == 8:
        return x8
    x9 = x8(I)
    if x == 9:
        return x9
    x10 = identity(p_g)
    if x == 10:
        return x10
    x11 = rbind(get_nth_t, F0)
    if x == 11:
        return x11
    x12 = c_iz_n(S, x10, x11)
    if x == 12:
        return x12
    x13 = index(x9, ORIGIN)
    if x == 13:
        return x13
    x14 = replace(x9, x12, x13)
    if x == 14:
        return x14
    x15 = branch(x6, righthalf, bottomhalf)
    if x == 15:
        return x15
    x16 = x15(I)
    if x == 16:
        return x16
    x17 = shape_t(x16)
    if x == 17:
        return x17
    x18 = decrement(x17)
    if x == 18:
        return x18
    x19 = index(x16, x18)
    if x == 19:
        return x19
    x20 = replace(x16, x12, x19)
    if x == 20:
        return x20
    O = x7(x14, x20)
    return O

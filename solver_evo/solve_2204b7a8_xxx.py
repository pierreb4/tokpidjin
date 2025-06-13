def solve_2204b7a8_one(S, I):
    return branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), hconcat, vconcat)(replace(branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), lefthalf, tophalf)(I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), index(branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), lefthalf, tophalf)(I), ORIGIN)), replace(branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), righthalf, bottomhalf)(I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), index(branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), righthalf, bottomhalf)(I), decrement(shape_t(branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), righthalf, bottomhalf)(I))))))


def solve_2204b7a8(S, I):
    x1 = o_g(I, R5)
    x2 = lbind(sfilter, x1)
    x3 = compose(size, x2)
    x4 = x3(vline_o)
    x5 = x3(hline_o)
    x6 = greater(x4, x5)
    x7 = branch(x6, hconcat, vconcat)
    x8 = branch(x6, lefthalf, tophalf)
    x9 = x8(I)
    x10 = identity(p_g)
    x11 = rbind(get_nth_t, F0)
    x12 = c_iz_n(S, x10, x11)
    x13 = index(x9, ORIGIN)
    x14 = replace(x9, x12, x13)
    x15 = branch(x6, righthalf, bottomhalf)
    x16 = x15(I)
    x17 = shape_t(x16)
    x18 = decrement(x17)
    x19 = index(x16, x18)
    x20 = replace(x16, x12, x19)
    O = x7(x14, x20)
    return O

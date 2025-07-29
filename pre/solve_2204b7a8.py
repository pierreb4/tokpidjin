def solve_2204b7a8_one(S, I):
    return branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), hconcat, vconcat)(replace(branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), lefthalf, tophalf)(I), THREE, index(branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), lefthalf, tophalf)(I), ORIGIN)), replace(branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), righthalf, bottomhalf)(I), THREE, index(branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), righthalf, bottomhalf)(I), decrement(shape_t(branch(greater(compose(size, lbind(sfilter, o_g(I, R5)))(vline_o), compose(size, lbind(sfilter, o_g(I, R5)))(hline_o)), righthalf, bottomhalf)(I))))))


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
    x10 = index(x9, ORIGIN)
    x11 = replace(x9, THREE, x10)
    x12 = branch(x6, righthalf, bottomhalf)
    x13 = x12(I)
    x14 = shape_t(x13)
    x15 = decrement(x14)
    x16 = index(x13, x15)
    x17 = replace(x13, THREE, x16)
    O = x7(x11, x17)
    return O

def solve_6cf79266_one(S, I):
    return fill(I, ONE, mapply(lbind(shift, toindices(upscale_f(initset(astuple(ZERO, ORIGIN)), THREE))), sfilter_f(f_ofcolor(I, ZERO), fork(both, matcher(chain(size, rbind(difference, f_ofcolor(I, ZERO)), lbind(shift, toindices(upscale_f(initset(astuple(ZERO, ORIGIN)), THREE)))), ZERO), chain(flip, matcher(chain(size, rbind(difference, f_ofcolor(I, ZERO)), lbind(shift, toindices(upscale_f(initset(astuple(ZERO, ORIGIN)), THREE)))), ZERO), lbind(add, NEG_UNITY))))))


def solve_6cf79266(S, I):
    x1 = astuple(ZERO, ORIGIN)
    x2 = initset(x1)
    x3 = upscale_f(x2, THREE)
    x4 = toindices(x3)
    x5 = lbind(shift, x4)
    x6 = f_ofcolor(I, ZERO)
    x7 = rbind(difference, x6)
    x8 = chain(size, x7, x5)
    x9 = matcher(x8, ZERO)
    x10 = lbind(add, NEG_UNITY)
    x11 = chain(flip, x9, x10)
    x12 = fork(both, x9, x11)
    x13 = sfilter_f(x6, x12)
    x14 = mapply(x5, x13)
    O = fill(I, ONE, x14)
    return O

def solve_6cf79266_one(S, I):
    return fill(I, ONE, mapply(lbind(shift, toindices(upscale_f(initset(astuple(ZERO, ORIGIN)), THREE))), sfilter_f(f_ofcolor(I, ZERO), fork(both, matcher(chain(size, rbind(difference, f_ofcolor(I, ZERO)), lbind(shift, toindices(upscale_f(initset(astuple(ZERO, ORIGIN)), THREE)))), ZERO), chain(flip, matcher(chain(size, rbind(difference, f_ofcolor(I, ZERO)), lbind(shift, toindices(upscale_f(initset(astuple(ZERO, ORIGIN)), THREE)))), ZERO), lbind(add, NEG_UNITY))))))


def solve_6cf79266(S, I, x=0):
    x1 = astuple(ZERO, ORIGIN)
    if x == 1:
        return x1
    x2 = initset(x1)
    if x == 2:
        return x2
    x3 = upscale_f(x2, THREE)
    if x == 3:
        return x3
    x4 = toindices(x3)
    if x == 4:
        return x4
    x5 = lbind(shift, x4)
    if x == 5:
        return x5
    x6 = f_ofcolor(I, ZERO)
    if x == 6:
        return x6
    x7 = rbind(difference, x6)
    if x == 7:
        return x7
    x8 = chain(size, x7, x5)
    if x == 8:
        return x8
    x9 = matcher(x8, ZERO)
    if x == 9:
        return x9
    x10 = lbind(add, NEG_UNITY)
    if x == 10:
        return x10
    x11 = chain(flip, x9, x10)
    if x == 11:
        return x11
    x12 = fork(both, x9, x11)
    if x == 12:
        return x12
    x13 = sfilter_f(x6, x12)
    if x == 13:
        return x13
    x14 = mapply(x5, x13)
    if x == 14:
        return x14
    O = fill(I, ONE, x14)
    return O

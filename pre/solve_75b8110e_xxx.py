def solve_75b8110e_one(S, I):
    return paint(paint(paint(tophalf(lefthalf(I)), fork(toobject, fork(difference, asindices, rbind(f_ofcolor, ZERO)), identity)(bottomhalf(righthalf(I)))), fork(toobject, fork(difference, asindices, rbind(f_ofcolor, ZERO)), identity)(bottomhalf(lefthalf(I)))), fork(toobject, fork(difference, asindices, rbind(f_ofcolor, ZERO)), identity)(tophalf(righthalf(I))))


def solve_75b8110e(S, I):
    x1 = lefthalf(I)
    x2 = tophalf(x1)
    x3 = rbind(f_ofcolor, ZERO)
    x4 = fork(difference, asindices, x3)
    x5 = fork(toobject, x4, identity)
    x6 = righthalf(I)
    x7 = bottomhalf(x6)
    x8 = x5(x7)
    x9 = paint(x2, x8)
    x10 = bottomhalf(x1)
    x11 = x5(x10)
    x12 = paint(x9, x11)
    x13 = tophalf(x6)
    x14 = x5(x13)
    O = paint(x12, x14)
    return O

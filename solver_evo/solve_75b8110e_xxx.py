def solve_75b8110e_one(S, I):
    return paint(paint(paint(tophalf(lefthalf(I)), fork(toobject, fork(difference, asindices, rbind(f_ofcolor, BLACK)), identity)(bottomhalf(righthalf(I)))), fork(toobject, fork(difference, asindices, rbind(f_ofcolor, BLACK)), identity)(bottomhalf(lefthalf(I)))), fork(toobject, fork(difference, asindices, rbind(f_ofcolor, BLACK)), identity)(tophalf(righthalf(I))))


def solve_75b8110e(S, I, x=0):
    x1 = lefthalf(I)
    if x == 1:
        return x1
    x2 = tophalf(x1)
    if x == 2:
        return x2
    x3 = rbind(f_ofcolor, BLACK)
    if x == 3:
        return x3
    x4 = fork(difference, asindices, x3)
    if x == 4:
        return x4
    x5 = fork(toobject, x4, identity)
    if x == 5:
        return x5
    x6 = righthalf(I)
    if x == 6:
        return x6
    x7 = bottomhalf(x6)
    if x == 7:
        return x7
    x8 = x5(x7)
    if x == 8:
        return x8
    x9 = paint(x2, x8)
    if x == 9:
        return x9
    x10 = bottomhalf(x1)
    if x == 10:
        return x10
    x11 = x5(x10)
    if x == 11:
        return x11
    x12 = paint(x9, x11)
    if x == 12:
        return x12
    x13 = tophalf(x6)
    if x == 13:
        return x13
    x14 = x5(x13)
    if x == 14:
        return x14
    O = paint(x12, x14)
    return O

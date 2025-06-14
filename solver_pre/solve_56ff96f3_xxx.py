def solve_56ff96f3_one(S, I):
    return paint(I, mapply(fork(recolor_i, color, backdrop), fgpartition(I)))


def solve_56ff96f3(S, I, x=0):
    x1 = fork(recolor_i, color, backdrop)
    if x == 1:
        return x1
    x2 = fgpartition(I)
    if x == 2:
        return x2
    x3 = mapply(x1, x2)
    if x == 3:
        return x3
    O = paint(I, x3)
    return O

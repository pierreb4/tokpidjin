def solve_56ff96f3_one(S, I):
    return paint(I, mapply(fork(recolor_i, color, backdrop), fgpartition(I)))


def solve_56ff96f3(S, I):
    x1 = fork(recolor_i, color, backdrop)
    x2 = fgpartition(I)
    x3 = mapply(x1, x2)
    O = paint(I, x3)
    return O

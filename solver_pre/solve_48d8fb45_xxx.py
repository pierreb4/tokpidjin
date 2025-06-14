def solve_48d8fb45_one(S, I):
    return subgrid(extract(o_g(I, R7), lbind(adjacent, extract(o_g(I, R7), matcher(size, ONE)))), I)


def solve_48d8fb45(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = matcher(size, ONE)
    if x == 2:
        return x2
    x3 = extract(x1, x2)
    if x == 3:
        return x3
    x4 = lbind(adjacent, x3)
    if x == 4:
        return x4
    x5 = extract(x1, x4)
    if x == 5:
        return x5
    O = subgrid(x5, I)
    return O

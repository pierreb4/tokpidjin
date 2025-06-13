def solve_48d8fb45_one(S, I):
    return subgrid(extract(o_g(I, R7), lbind(adjacent, extract(o_g(I, R7), matcher(size, BLUE)))), I)


def solve_48d8fb45(S, I):
    x1 = o_g(I, R7)
    x2 = matcher(size, BLUE)
    x3 = extract(x1, x2)
    x4 = lbind(adjacent, x3)
    x5 = extract(x1, x4)
    O = subgrid(x5, I)
    return O

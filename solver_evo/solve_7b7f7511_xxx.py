def solve_7b7f7511_one(S, I):
    return branch(portrait_t(I), tophalf, lefthalf)(I)


def solve_7b7f7511(S, I, x=0):
    x1 = portrait_t(I)
    if x == 1:
        return x1
    x2 = branch(x1, tophalf, lefthalf)
    if x == 2:
        return x2
    O = x2(I)
    return O

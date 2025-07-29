def solve_7b7f7511_one(S, I):
    return branch(portrait_t(I), tophalf, lefthalf)(I)


def solve_7b7f7511(S, I):
    x1 = portrait_t(I)
    x2 = branch(x1, tophalf, lefthalf)
    O = x2(I)
    return O

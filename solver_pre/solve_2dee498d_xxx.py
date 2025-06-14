def solve_2dee498d_one(S, I):
    return get_nth_t(hsplit(I, THREE), F0)


def solve_2dee498d(S, I, x=0):
    x1 = hsplit(I, THREE)
    if x == 1:
        return x1
    O = get_nth_t(x1, F0)
    return O

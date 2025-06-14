def solve_b9b7f026_one(S, I):
    return canvas(color(extract(remove_f(get_arg_rank_f(o_g(I, R4), size, L1), o_g(I, R4)), rbind(adjacent, get_arg_rank_f(o_g(I, R4), size, L1)))), UNITY)


def solve_b9b7f026(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, L1)
    if x == 2:
        return x2
    x3 = remove_f(x2, x1)
    if x == 3:
        return x3
    x4 = rbind(adjacent, x2)
    if x == 4:
        return x4
    x5 = extract(x3, x4)
    if x == 5:
        return x5
    x6 = color(x5)
    if x == 6:
        return x6
    O = canvas(x6, UNITY)
    return O

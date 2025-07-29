def solve_b9b7f026_one(S, I):
    return canvas(color(extract(remove_f(get_arg_rank_f(o_g(I, R4), size, L1), o_g(I, R4)), rbind(adjacent, get_arg_rank_f(o_g(I, R4), size, L1)))), UNITY)


def solve_b9b7f026(S, I):
    x1 = o_g(I, R4)
    x2 = get_arg_rank_f(x1, size, L1)
    x3 = remove_f(x2, x1)
    x4 = rbind(adjacent, x2)
    x5 = extract(x3, x4)
    x6 = color(x5)
    O = canvas(x6, UNITY)
    return O

def solve_8f2ea7aa_one(S, I):
    return cellwise(upscale_t(subgrid(merge_f(o_g(I, R5)), I), THREE), vconcat(vconcat(hconcat(hconcat(subgrid(merge_f(o_g(I, R5)), I), subgrid(merge_f(o_g(I, R5)), I)), subgrid(merge_f(o_g(I, R5)), I)), hconcat(hconcat(subgrid(merge_f(o_g(I, R5)), I), subgrid(merge_f(o_g(I, R5)), I)), subgrid(merge_f(o_g(I, R5)), I))), hconcat(hconcat(subgrid(merge_f(o_g(I, R5)), I), subgrid(merge_f(o_g(I, R5)), I)), subgrid(merge_f(o_g(I, R5)), I))), ZERO)


def solve_8f2ea7aa(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = upscale_t(x3, THREE)
    if x == 4:
        return x4
    x5 = hconcat(x3, x3)
    if x == 5:
        return x5
    x6 = hconcat(x5, x3)
    if x == 6:
        return x6
    x7 = vconcat(x6, x6)
    if x == 7:
        return x7
    x8 = vconcat(x7, x6)
    if x == 8:
        return x8
    O = cellwise(x4, x8, ZERO)
    return O

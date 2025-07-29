def solve_8f2ea7aa_one(S, I):
    return cellwise(upscale_t(subgrid(merge_f(o_g(I, R5)), I), THREE), vconcat(vconcat(hconcat(hconcat(subgrid(merge_f(o_g(I, R5)), I), subgrid(merge_f(o_g(I, R5)), I)), subgrid(merge_f(o_g(I, R5)), I)), hconcat(hconcat(subgrid(merge_f(o_g(I, R5)), I), subgrid(merge_f(o_g(I, R5)), I)), subgrid(merge_f(o_g(I, R5)), I))), hconcat(hconcat(subgrid(merge_f(o_g(I, R5)), I), subgrid(merge_f(o_g(I, R5)), I)), subgrid(merge_f(o_g(I, R5)), I))), ZERO)


def solve_8f2ea7aa(S, I):
    x1 = o_g(I, R5)
    x2 = merge_f(x1)
    x3 = subgrid(x2, I)
    x4 = upscale_t(x3, THREE)
    x5 = hconcat(x3, x3)
    x6 = hconcat(x5, x3)
    x7 = vconcat(x6, x6)
    x8 = vconcat(x7, x6)
    O = cellwise(x4, x8, ZERO)
    return O

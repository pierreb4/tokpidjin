def solve_007bbfb7_one(S, I):
    return cellwise(vupscale(hupscale(I, THREE), THREE), vconcat(vconcat(hconcat(hconcat(I, I), I), hconcat(hconcat(I, I), I)), hconcat(hconcat(I, I), I)), ZERO)


def solve_007bbfb7(S, I, x=0):
    x1 = hupscale(I, THREE)
    if x == 1:
        return x1
    x2 = vupscale(x1, THREE)
    if x == 2:
        return x2
    x3 = hconcat(I, I)
    if x == 3:
        return x3
    x4 = hconcat(x3, I)
    if x == 4:
        return x4
    x5 = vconcat(x4, x4)
    if x == 5:
        return x5
    x6 = vconcat(x5, x4)
    if x == 6:
        return x6
    O = cellwise(x2, x6, ZERO)
    return O

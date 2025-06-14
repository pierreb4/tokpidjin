def solve_662c240a_one(S, I):
    return extract(vsplit(I, THREE), compose(flip, fork(equality, rbind(mir_rot_t, R1), identity)))


def solve_662c240a(S, I, x=0):
    x1 = vsplit(I, THREE)
    if x == 1:
        return x1
    x2 = rbind(mir_rot_t, R1)
    if x == 2:
        return x2
    x3 = fork(equality, x2, identity)
    if x == 3:
        return x3
    x4 = compose(flip, x3)
    if x == 4:
        return x4
    O = extract(x1, x4)
    return O

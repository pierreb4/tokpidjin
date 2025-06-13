def solve_662c240a_one(S, I):
    return extract(vsplit(I, THREE), compose(flip, fork(equality, rbind(mir_rot_t, R1), identity)))


def solve_662c240a(S, I):
    x1 = vsplit(I, THREE)
    x2 = rbind(mir_rot_t, R1)
    x3 = fork(equality, x2, identity)
    x4 = compose(flip, x3)
    O = extract(x1, x4)
    return O

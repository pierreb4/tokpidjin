def get_f15e1fac_x4_x3(a1: bool) -> Callable:
    return branch(a1, identity, rbind(mir_rot_t, R1))

# {'a1': 'bool', 'return': 'Callable'}

func_d = {('get_f15e1fac_x4_x3', 'Callable', 'bool'): 'branch(a1, identity, rbind(mir_rot_t, R1))'}


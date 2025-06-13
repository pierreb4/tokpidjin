def get_f15e1fac_x8_x7(a1: bool) -> Callable:
    return branch(a1, identity, rbind(mir_rot_t, R2))

# {'a1': 'bool', 'return': 'Callable'}

func_d = {('get_f15e1fac_x8_x7', 'Callable', 'bool'): 'branch(a1, identity, rbind(mir_rot_t, R2))'}


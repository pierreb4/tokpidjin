def get_4522001f_x20_x19(a1: bool, a2: Grid) -> Grid:
    return branch(a1, mir_rot_t(a2, R4), a2)

# {'a1': 'bool', 'a2': 'Grid', 'return': 'Grid'}

func_d = {('get_4522001f_x20_x19', 'Grid', 'bool', 'Grid'): 'branch(a1, mir_rot_t(a2, R4), a2)'}


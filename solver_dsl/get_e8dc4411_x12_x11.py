def get_e8dc4411_x12_x11(a1: bool, a2: Callable) -> Callable:
    return branch(a1, identity, fork(add, identity, a2))

# {'a1': 'bool', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_e8dc4411_x12_x11', 'Callable', 'bool', 'Callable'): 'branch(a1, identity, fork(add, identity, a2))'}


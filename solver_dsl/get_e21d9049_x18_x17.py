def get_e21d9049_x18_x17(a1: Callable, a2: Any) -> Callable:
    return fork(either, a1, lbind(vmatching, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_e21d9049_x18_x17', 'Callable', 'Callable', 'Any'): 'fork(either, a1, lbind(vmatching, a2))'}


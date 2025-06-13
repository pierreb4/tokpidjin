def get_e21d9049_x18_x16(a1: Any, a2: Callable) -> Callable:
    return fork(either, lbind(hmatching, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Any'}

func_d = {('get_e21d9049_x18_x16', 'Callable', 'Any', 'Callable'): 'fork(either, lbind(hmatching, a1), a2)'}


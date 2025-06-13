def get_b775ac94_x58_x57(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return fork(intersection, a1, a2(a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Any'}

func_d = {('get_b775ac94_x58_x57', 'Callable', 'Callable', 'Callable', 'Any'): 'fork(intersection, a1, a2(a3))'}


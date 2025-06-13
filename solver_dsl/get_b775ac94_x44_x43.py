def get_b775ac94_x44_x43(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return fork(shift, a1, a2(a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Any'}

func_d = {('get_b775ac94_x44_x43', 'Callable', 'Callable', 'Callable', 'Any'): 'fork(shift, a1, a2(a3))'}


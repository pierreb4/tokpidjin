def get_9aec4887_x24_x23(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return fork(connect, a1, a2)(a3)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_9aec4887_x24_x23', 'Callable', 'Callable', 'Callable', 'Any'): 'fork(connect, a1, a2)(a3)'}


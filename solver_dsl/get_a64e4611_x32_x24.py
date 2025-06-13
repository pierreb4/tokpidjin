def get_a64e4611_x32_x24(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return fork(mapply, a1, a2)(a3)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_a64e4611_x32_x24', 'Callable', 'Callable', 'Callable', 'Any'): 'fork(mapply, a1, a2)(a3)'}


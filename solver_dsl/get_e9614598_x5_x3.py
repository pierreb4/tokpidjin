def get_e9614598_x5_x3(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return fork(add, a1, a2)(a3)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_e9614598_x5_x3', 'Callable', 'Callable', 'Callable', 'Any'): 'fork(add, a1, a2)(a3)'}


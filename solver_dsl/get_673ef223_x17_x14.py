def get_673ef223_x17_x14(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return fork(subtract, a1, a2)(a3)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_673ef223_x17_x14', 'Callable', 'Callable', 'Callable', 'Any'): 'fork(subtract, a1, a2)(a3)'}


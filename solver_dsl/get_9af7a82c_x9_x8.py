def get_9af7a82c_x9_x8(a1: Callable, a2: Any) -> Callable:
    return chain(a1, lbind(subtract, a2), size)

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_9af7a82c_x9_x8', 'Callable', 'Callable', 'Any'): 'chain(a1, lbind(subtract, a2), size)'}


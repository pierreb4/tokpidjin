def get_6a1e5592_x28_x27(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return rbind(a1, fork(subtract, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_6a1e5592_x28_x27', 'Callable', 'Callable', 'Callable', 'Callable'): 'rbind(a1, fork(subtract, a2, a3))'}


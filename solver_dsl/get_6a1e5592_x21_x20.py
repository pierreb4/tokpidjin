def get_6a1e5592_x21_x20(a1: Callable, a2: Callable) -> Callable:
    return fork(subtract, a1, chain(size, a2, outbox))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_6a1e5592_x21_x20', 'Callable', 'Callable', 'Callable'): 'fork(subtract, a1, chain(size, a2, outbox))'}


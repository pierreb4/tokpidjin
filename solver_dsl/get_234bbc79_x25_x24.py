def get_234bbc79_x25_x24(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return fork(subtract, a1, chain(a2, a3, a4))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable', 'a4': 'Callable'}

func_d = {('get_234bbc79_x25_x24', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(subtract, a1, chain(a2, a3, a4))'}


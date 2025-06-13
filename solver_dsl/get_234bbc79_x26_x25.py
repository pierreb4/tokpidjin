def get_234bbc79_x26_x25(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return compose(a1, fork(subtract, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_234bbc79_x26_x25', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(a1, fork(subtract, a2, a3))'}


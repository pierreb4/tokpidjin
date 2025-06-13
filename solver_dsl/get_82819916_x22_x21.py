def get_82819916_x22_x21(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(recolor_o, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_82819916_x22_x21', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(recolor_o, a1, compose(a2, a3))'}


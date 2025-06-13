def get_234bbc79_x18_x17(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return compose(compose(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_234bbc79_x18_x17', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(compose(a1, a2), a3)'}


def get_234bbc79_x24_x23(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(compose(a1, a2), a3, a1)

# {'a3': 'Callable', 'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_234bbc79_x24_x23', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(compose(a1, a2), a3, a1)'}


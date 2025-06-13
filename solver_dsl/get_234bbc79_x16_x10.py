def get_234bbc79_x16_x10(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(a1, fork(sfilter, identity, a2), a3)

# {'a1': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_234bbc79_x16_x10', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(a1, fork(sfilter, identity, a2), a3)'}


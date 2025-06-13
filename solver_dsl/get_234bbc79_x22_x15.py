def get_234bbc79_x22_x15(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return fork(a1, a2, chain(a3, a4, toindices))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Callable', 'a4': 'Callable'}

func_d = {('get_234bbc79_x22_x15', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(a1, a2, chain(a3, a4, toindices))'}


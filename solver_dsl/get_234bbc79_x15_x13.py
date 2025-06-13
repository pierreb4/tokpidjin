def get_234bbc79_x15_x13(a1: Callable, a2: Callable) -> Callable:
    return chain(lbind(a1, size), a2, toindices)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_234bbc79_x15_x13', 'Callable', 'Callable', 'Callable'): 'chain(lbind(a1, size), a2, toindices)'}


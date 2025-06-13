def get_5daaa586_x5_x4(a1: Container, a2: Callable) -> Callable:
    return extract(a1, compose(flip, a2))

# {'a1': 'Container', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_5daaa586_x5_x4', 'Callable', 'Container', 'Callable'): 'extract(a1, compose(flip, a2))'}


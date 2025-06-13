def get_846bdb03_x4_x3(a1: Container, a2: Callable) -> Callable:
    return extract(a1, matcher(a2, ZERO))

# {'a1': 'Container', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_846bdb03_x4_x3', 'Callable', 'Container', 'Callable'): 'extract(a1, matcher(a2, ZERO))'}


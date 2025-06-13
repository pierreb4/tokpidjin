def get_a87f7484_x12_x11(a1: Container, a2: Callable, a3: Any) -> Callable:
    return extract(a1, matcher(a2, a3))

# {'a1': 'Container', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Any'}

func_d = {('get_a87f7484_x12_x11', 'Callable', 'Container', 'Callable', 'Any'): 'extract(a1, matcher(a2, a3))'}


def get_a48eeaf7_x11_x10(a1: Callable, a2: Callable, a3: Container[Container]) -> Callable:
    return mapply(compose(a1, a2), a3)

# {'a3': 'Container[Container]', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_a48eeaf7_x11_x10', 'Callable', 'Callable', 'Callable', 'Container[Container]'): 'mapply(compose(a1, a2), a3)'}


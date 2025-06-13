def get_855e0971_x11_x10(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return chain(a1, a2, rbind(subgrid, a3))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_855e0971_x11_x10', 'Callable', 'Callable', 'Callable', 'Any'): 'chain(a1, a2, rbind(subgrid, a3))'}


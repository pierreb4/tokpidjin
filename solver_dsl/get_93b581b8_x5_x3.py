def get_93b581b8_x5_x3(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return chain(a1, a2, merge)(a3)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_93b581b8_x5_x3', 'Callable', 'Callable', 'Callable', 'Any'): 'chain(a1, a2, merge)(a3)'}


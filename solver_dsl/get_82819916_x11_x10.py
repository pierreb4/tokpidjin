def get_82819916_x11_x10(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return matcher(a1, a2(a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Any'}

func_d = {('get_82819916_x11_x10', 'Callable', 'Callable', 'Callable', 'Any'): 'matcher(a1, a2(a3))'}


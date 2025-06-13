def get_6a1e5592_x31_x28(a1: Callable, a2: Any, a3: Callable, a4: Callable) -> Callable:
    return chain(rbind(a1, a2), a3, a4)

# {'a3': 'Callable', 'a4': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Any'}

func_d = {('get_6a1e5592_x31_x28', 'Callable', 'Callable', 'Any', 'Callable', 'Callable'): 'chain(rbind(a1, a2), a3, a4)'}


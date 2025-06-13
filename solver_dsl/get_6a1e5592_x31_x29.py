def get_6a1e5592_x31_x29(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return chain(a1, rbind(apply, a2), a3)

# {'a1': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_6a1e5592_x31_x29', 'Callable', 'Callable', 'Any', 'Callable'): 'chain(a1, rbind(apply, a2), a3)'}


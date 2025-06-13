def get_0a938d79_x15_x13(a1: Callable, a2: Callable, a3: Any, a4: Callable) -> Callable:
    return chain(a1, rbind(a2, a3), a4)

# {'a1': 'Callable', 'a4': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Any'}

func_d = {('get_0a938d79_x15_x13', 'Callable', 'Callable', 'Callable', 'Any', 'Callable'): 'chain(a1, rbind(a2, a3), a4)'}


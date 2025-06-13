def get_045e512c_x10_x7(a1: Any, a2: Callable, a3: Callable) -> Callable:
    return chain(rbind(apply, a1), a2, a3)

# {'a2': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a1': 'Any'}

func_d = {('get_045e512c_x10_x7', 'Callable', 'Any', 'Callable', 'Callable'): 'chain(rbind(apply, a1), a2, a3)'}


def get_e73095fd_x11_x7(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return chain(a1, rbind(intersection, a2), a3)

# {'a1': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_e73095fd_x11_x7', 'Callable', 'Callable', 'Any', 'Callable'): 'chain(a1, rbind(intersection, a2), a3)'}


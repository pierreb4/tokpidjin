def get_7837ac64_x22_x3(a1: Any, a2: Callable, a3: Callable) -> Callable:
    return chain(lbind(apply, a1), a2, a3)

# {'a2': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a1': 'Any'}

func_d = {('get_7837ac64_x22_x3', 'Callable', 'Any', 'Callable', 'Callable'): 'chain(lbind(apply, a1), a2, a3)'}


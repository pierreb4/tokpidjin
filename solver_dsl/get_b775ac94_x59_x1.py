def get_b775ac94_x59_x1(a1: Any, a2: Callable, a3: Callable) -> Callable:
    return chain(lbind(index, a1), a2, a3)

# {'a2': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a1': 'Any'}

func_d = {('get_b775ac94_x59_x1', 'Callable', 'Any', 'Callable', 'Callable'): 'chain(lbind(index, a1), a2, a3)'}


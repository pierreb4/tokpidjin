def get_b775ac94_x7_x4(a1: Any, a2: Callable, a3: Callable) -> Callable:
    return chain(rbind(compose, a1), a2, a3)

# {'a2': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a1': 'Any'}

func_d = {('get_b775ac94_x7_x4', 'Callable', 'Any', 'Callable', 'Callable'): 'chain(rbind(compose, a1), a2, a3)'}


def get_b775ac94_x44_x42(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return fork(shift, a1(a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Any'}

func_d = {('get_b775ac94_x44_x42', 'Callable', 'Callable', 'Any', 'Callable'): 'fork(shift, a1(a2), a3)'}


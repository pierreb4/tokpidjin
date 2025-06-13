def get_e8dc4411_x7_x6(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return fork(connect, a1, a2)(a3)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_e8dc4411_x7_x6', 'Callable', 'Callable', 'Callable', 'Any'): 'fork(connect, a1, a2)(a3)'}


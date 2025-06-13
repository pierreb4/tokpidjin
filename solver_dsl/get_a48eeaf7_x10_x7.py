def get_a48eeaf7_x10_x7(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return compose(lbind(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Any'}

func_d = {('get_a48eeaf7_x10_x7', 'Callable', 'Callable', 'Any', 'Callable'): 'compose(lbind(a1, a2), a3)'}


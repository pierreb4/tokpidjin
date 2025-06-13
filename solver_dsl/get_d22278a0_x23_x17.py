def get_d22278a0_x23_x17(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return compose(lbind(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Any'}

func_d = {('get_d22278a0_x23_x17', 'Callable', 'Callable', 'Any', 'Callable'): 'compose(lbind(a1, a2), a3)'}


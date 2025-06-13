def get_d22278a0_x26_x2(a1: Any, a2: Callable, a3: Callable) -> Callable:
    return chain(lbind(sfilter, a1), a2, a3)

# {'a2': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a1': 'Any'}

func_d = {('get_d22278a0_x26_x2', 'Callable', 'Any', 'Callable', 'Callable'): 'chain(lbind(sfilter, a1), a2, a3)'}


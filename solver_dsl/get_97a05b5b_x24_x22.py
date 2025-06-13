def get_97a05b5b_x24_x22(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return chain(a1, lbind(sfilter, a2), a3)

# {'a1': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_97a05b5b_x24_x22', 'Callable', 'Callable', 'Any', 'Callable'): 'chain(a1, lbind(sfilter, a2), a3)'}


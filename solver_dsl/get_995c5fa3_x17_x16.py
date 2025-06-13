def get_995c5fa3_x17_x16(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return compose(a1, matcher(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Any'}

func_d = {('get_995c5fa3_x17_x16', 'Callable', 'Callable', 'Callable', 'Any'): 'compose(a1, matcher(a2, a3))'}


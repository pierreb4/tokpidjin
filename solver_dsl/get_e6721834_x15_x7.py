def get_e6721834_x15_x7(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return chain(a1, lbind(occurrences, a2), a3)

# {'a1': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_e6721834_x15_x7', 'Callable', 'Callable', 'Any', 'Callable'): 'chain(a1, lbind(occurrences, a2), a3)'}


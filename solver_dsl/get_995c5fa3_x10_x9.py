def get_995c5fa3_x10_x9(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, double, matcher(a2, UNITY))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_995c5fa3_x10_x9', 'Callable', 'Callable', 'Callable'): 'chain(a1, double, matcher(a2, UNITY))'}


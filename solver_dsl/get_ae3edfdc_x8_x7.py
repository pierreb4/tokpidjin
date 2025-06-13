def get_ae3edfdc_x8_x7(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(a1, a2, a3)(TWO)

# {'a1': 'Callable', 'a2': 'Callable', 'a3': 'Callable', 'return': 'Callable'}

func_d = {('get_ae3edfdc_x8_x7', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, a3)(TWO)'}


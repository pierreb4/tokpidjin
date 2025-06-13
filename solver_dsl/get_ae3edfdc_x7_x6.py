def get_ae3edfdc_x7_x6(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return chain(a1, a2, lbind(colorfilter, a3))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_ae3edfdc_x7_x6', 'Callable', 'Callable', 'Callable', 'Any'): 'chain(a1, a2, lbind(colorfilter, a3))'}


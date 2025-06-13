def get_a61ba2ce_x7_x3(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return chain(a1, lbind(extract, a2), a3)

# {'a1': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_a61ba2ce_x7_x3', 'Callable', 'Callable', 'Any', 'Callable'): 'chain(a1, lbind(extract, a2), a3)'}


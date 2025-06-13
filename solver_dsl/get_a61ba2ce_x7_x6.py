def get_a61ba2ce_x7_x6(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return chain(a1, a2, lbind(compose, a3))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_a61ba2ce_x7_x6', 'Callable', 'Callable', 'Callable', 'Any'): 'chain(a1, a2, lbind(compose, a3))'}


def get_f15e1fac_O_x16(a1: Callable, a2: Callable, a3: Callable, a4: Any) -> Callable:
    return chain(a1, a2, a3)(a4)

# {'a1': 'Callable', 'a2': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a4': 'Any'}

func_d = {('get_f15e1fac_O_x16', 'Callable', 'Callable', 'Callable', 'Callable', 'Any'): 'chain(a1, a2, a3)(a4)'}


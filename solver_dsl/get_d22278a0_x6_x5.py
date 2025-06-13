def get_d22278a0_x6_x5(a1: Callable, a2: Any) -> Callable:
    return chain(even, a1, lbind(apply, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_d22278a0_x6_x5', 'Callable', 'Callable', 'Any'): 'chain(even, a1, lbind(apply, a2))'}


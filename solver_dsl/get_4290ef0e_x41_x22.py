def get_4290ef0e_x41_x22(a1: Callable, a2: Callable, a3: Container) -> Callable:
    return apply(compose(a1, a2), a3)

# {'a3': 'Container', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_4290ef0e_x41_x22', 'Callable', 'Callable', 'Callable', 'Container'): 'apply(compose(a1, a2), a3)'}


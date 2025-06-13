def get_23581191_x10_x2(a1: Callable, a2: Container) -> Callable:
    return apply(compose(a1, center), a2)

# {'a2': 'Container', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_23581191_x10_x2', 'Callable', 'Callable', 'Container'): 'apply(compose(a1, center), a2)'}


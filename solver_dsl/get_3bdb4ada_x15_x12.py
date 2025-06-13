def get_3bdb4ada_x15_x12(a1: Callable, a2: Container) -> Callable:
    return apply(compose(increment, a1), a2)

# {'a2': 'Container', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_3bdb4ada_x15_x12', 'Callable', 'Callable', 'Container'): 'apply(compose(increment, a1), a2)'}


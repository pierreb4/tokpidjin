def get_3bdb4ada_x18_x17(a1: Callable, a2: Container) -> Callable:
    return apply(compose(decrement, a1), a2)

# {'a2': 'Container', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_3bdb4ada_x18_x17', 'Callable', 'Callable', 'Container'): 'apply(compose(decrement, a1), a2)'}


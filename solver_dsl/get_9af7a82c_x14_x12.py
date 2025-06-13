def get_9af7a82c_x14_x12(a1: Callable, a2: Callable, a3: Container) -> Callable:
    return apply(compose(a1, a2), a3)

# {'a3': 'Container', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_9af7a82c_x14_x12', 'Callable', 'Callable', 'Callable', 'Container'): 'apply(compose(a1, a2), a3)'}


def get_ecdecbb3_x17_x11(a1: Callable, a2: Container, a3: Container) -> FrozenSet:
    return apply(a1, product(a2, a3))

# {'a1': 'Callable', 'return': 'FrozenSet', 'a2': 'Container', 'a3': 'Container'}

func_d = {('get_ecdecbb3_x17_x11', 'FrozenSet', 'Callable', 'Container', 'Container'): 'apply(a1, product(a2, a3))'}


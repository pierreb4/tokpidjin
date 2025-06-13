def get_ded97339_x6_x5(a1: Callable, a2: Container) -> FrozenSet:
    return apply(a1, product(a2, a2))

# {'a1': 'Callable', 'return': 'FrozenSet', 'a2': 'Container'}

func_d = {('get_ded97339_x6_x5', 'FrozenSet', 'Callable', 'Container'): 'apply(a1, product(a2, a2))'}


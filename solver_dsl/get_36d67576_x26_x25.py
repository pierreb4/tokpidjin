def get_36d67576_x26_x25(a1: Callable, a2: Container) -> FrozenSet:
    return apply(a1, product(a2, a2))

# {'a1': 'Callable', 'return': 'FrozenSet', 'a2': 'Container'}

func_d = {('get_36d67576_x26_x25', 'FrozenSet', 'Callable', 'Container'): 'apply(a1, product(a2, a2))'}


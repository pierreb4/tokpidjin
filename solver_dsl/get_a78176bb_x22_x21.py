def get_a78176bb_x22_x21(a1: Callable, a2: Callable, a3: Container) -> Container:
    return apply(a1, apply(a2, a3))

# {'a1': 'Callable', 'return': 'Container', 'a2': 'Callable', 'a3': 'Container'}

func_d = {('get_a78176bb_x22_x21', 'Container', 'Callable', 'Callable', 'Container'): 'apply(a1, apply(a2, a3))'}


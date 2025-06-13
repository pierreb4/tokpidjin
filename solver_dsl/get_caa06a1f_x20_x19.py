def get_caa06a1f_x20_x19(a1: Callable, a2: Callable, a3: Any) -> Container:
    return apply(a1, a2(a3))

# {'a1': 'Callable', 'return': 'Container', 'a2': 'Callable', 'a3': 'Any'}

func_d = {('get_caa06a1f_x20_x19', 'Container', 'Callable', 'Callable', 'Any'): 'apply(a1, a2(a3))'}


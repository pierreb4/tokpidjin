def get_82819916_x10_x6(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return compose(a1, a2)(a3)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_82819916_x10_x6', 'Callable', 'Callable', 'Callable', 'Any'): 'compose(a1, a2)(a3)'}


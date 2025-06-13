def get_3e980e27_x10_x9(a1: Callable, a2: Any) -> Callable:
    return fork(shift, identity, a1(a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Any'}

func_d = {('get_3e980e27_x10_x9', 'Callable', 'Callable', 'Any'): 'fork(shift, identity, a1(a2))'}


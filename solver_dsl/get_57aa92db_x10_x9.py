def get_57aa92db_x10_x9(a1: Callable, a2: Callable) -> Callable:
    return compose(a1, fork(apply, a2, palette_f))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_57aa92db_x10_x9', 'Callable', 'Callable', 'Callable'): 'compose(a1, fork(apply, a2, palette_f))'}


def get_57aa92db_x26_x25(a1: Callable, a2: Callable) -> Callable:
    return fork(upscale_f, compose(a1, a2), width_f)

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_57aa92db_x26_x25', 'Callable', 'Callable', 'Callable'): 'fork(upscale_f, compose(a1, a2), width_f)'}


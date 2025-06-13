def get_57aa92db_x3_x2(a1: Callable) -> Callable:
    return chain(a1, lbind(remove, ZERO), palette_f)

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_57aa92db_x3_x2', 'Callable', 'Callable'): 'chain(a1, lbind(remove, ZERO), palette_f)'}


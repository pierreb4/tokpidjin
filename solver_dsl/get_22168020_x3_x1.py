def get_22168020_x3_x1(a1: Callable) -> Callable:
    return fork(lbind(prapply, connect), a1, a1)

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_22168020_x3_x1', 'Callable', 'Callable'): 'fork(lbind(prapply, connect), a1, a1)'}


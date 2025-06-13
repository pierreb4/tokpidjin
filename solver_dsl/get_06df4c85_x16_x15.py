def get_06df4c85_x16_x15(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(equality, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_06df4c85_x16_x15', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(equality, a1, compose(a2, a3))'}


def get_6aa20dc0_x10_x1(a1: Callable) -> Callable:
    return fork(mapply, lbind(lbind, shift), a1)

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_6aa20dc0_x10_x1', 'Callable', 'Callable'): 'fork(mapply, lbind(lbind, shift), a1)'}


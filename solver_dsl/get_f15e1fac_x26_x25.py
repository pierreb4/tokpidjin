def get_f15e1fac_x26_x25(a1: Callable, a2: Callable) -> Callable:
    return fork(greater, a1, chain(decrement, a2, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_f15e1fac_x26_x25', 'Callable', 'Callable', 'Callable'): 'fork(greater, a1, chain(decrement, a2, a2))'}


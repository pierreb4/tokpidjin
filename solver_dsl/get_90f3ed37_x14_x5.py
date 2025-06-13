def get_90f3ed37_x14_x5(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, lbind(lbind, shift), a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_90f3ed37_x14_x5', 'Callable', 'Callable', 'Callable'): 'chain(a1, lbind(lbind, shift), a2)'}


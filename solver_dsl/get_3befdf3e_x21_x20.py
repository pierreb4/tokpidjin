def get_3befdf3e_x21_x20(a1: Callable, a2: Callable) -> Callable:
    return compose(lbind(a1, inbox), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_3befdf3e_x21_x20', 'Callable', 'Callable', 'Callable'): 'compose(lbind(a1, inbox), a2)'}


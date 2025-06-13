def get_e6721834_x15_x6(a1: Callable, a2: Callable) -> Callable:
    return chain(rbind(get_nth_f, F0), a1, a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_e6721834_x15_x6', 'Callable', 'Callable', 'Callable'): 'chain(rbind(get_nth_f, F0), a1, a2)'}


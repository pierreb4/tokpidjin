def get_234bbc79_x24_x2(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, a2, rbind(get_nth_f, L1))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_234bbc79_x24_x2', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, rbind(get_nth_f, L1))'}


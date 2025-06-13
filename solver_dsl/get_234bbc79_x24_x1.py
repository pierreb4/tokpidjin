def get_234bbc79_x24_x1(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, rbind(get_nth_f, F0), a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_234bbc79_x24_x1', 'Callable', 'Callable', 'Callable'): 'chain(a1, rbind(get_nth_f, F0), a2)'}


def get_b775ac94_x59_x2(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, rbind(get_nth_f, F0), a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_b775ac94_x59_x2', 'Callable', 'Callable', 'Callable'): 'chain(a1, rbind(get_nth_f, F0), a2)'}


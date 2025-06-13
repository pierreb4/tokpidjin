def get_4290ef0e_x30_x25(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, rbind(get_rank, L1), a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_4290ef0e_x30_x25', 'Callable', 'Callable', 'Callable'): 'chain(a1, rbind(get_rank, L1), a2)'}


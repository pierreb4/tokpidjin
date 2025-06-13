def get_a64e4611_x23_x22(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(occurrences, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_a64e4611_x23_x22', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(occurrences, a1, compose(a2, a3))'}


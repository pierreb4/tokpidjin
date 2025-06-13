def get_3eda0437_x3_x2(a1: Callable, a2: Any) -> Callable:
    return fork(apply, a1, lbind(occurrences, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_3eda0437_x3_x2', 'Callable', 'Callable', 'Any'): 'fork(apply, a1, lbind(occurrences, a2))'}


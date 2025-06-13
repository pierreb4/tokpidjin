def get_f1cefba8_x22_x21(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return fork(either, a1, matcher(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Any'}

func_d = {('get_f1cefba8_x22_x21', 'Callable', 'Callable', 'Callable', 'Any'): 'fork(either, a1, matcher(a2, a3))'}


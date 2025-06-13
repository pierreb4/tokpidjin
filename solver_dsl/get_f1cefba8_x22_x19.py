def get_f1cefba8_x22_x19(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return fork(either, matcher(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Any'}

func_d = {('get_f1cefba8_x22_x19', 'Callable', 'Callable', 'Any', 'Callable'): 'fork(either, matcher(a1, a2), a3)'}


def get_7837ac64_x22_x21(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return chain(a1, a2, rbind(pair, a3))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_7837ac64_x22_x21', 'Callable', 'Callable', 'Callable', 'Any'): 'chain(a1, a2, rbind(pair, a3))'}


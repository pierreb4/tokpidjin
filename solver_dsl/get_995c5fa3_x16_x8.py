def get_995c5fa3_x16_x8(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return matcher(compose(a1, a2), a3)

# {'a3': 'Any', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_995c5fa3_x16_x8', 'Callable', 'Callable', 'Callable', 'Any'): 'matcher(compose(a1, a2), a3)'}


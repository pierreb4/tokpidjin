def get_7df24a62_x5_x2(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, rbind(shift, NEG_UNITY), a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_7df24a62_x5_x2', 'Callable', 'Callable', 'Callable'): 'chain(a1, rbind(shift, NEG_UNITY), a2)'}


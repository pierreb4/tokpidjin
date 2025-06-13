def get_29623171_x17_x15(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return matcher(compose(a1, a2), a3)

# {'a3': 'Any', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_29623171_x17_x15', 'Callable', 'Callable', 'Callable', 'Any'): 'matcher(compose(a1, a2), a3)'}


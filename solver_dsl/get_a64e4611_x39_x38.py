def get_a64e4611_x39_x38(a1: Callable, a2: Callable) -> Callable:
    return matcher(chain(a1, a2, neighbors), EIGHT)

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_a64e4611_x39_x38', 'Callable', 'Callable', 'Callable'): 'matcher(chain(a1, a2, neighbors), EIGHT)'}


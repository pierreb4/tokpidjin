def get_a78176bb_x13_x12(a1: Callable, a2: Callable) -> Callable:
    return matcher(compose(a1, a2), FIVE)

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_a78176bb_x13_x12', 'Callable', 'Callable', 'Callable'): 'matcher(compose(a1, a2), FIVE)'}


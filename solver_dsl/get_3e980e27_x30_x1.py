def get_3e980e27_x30_x1(a1: Callable, a2: Callable) -> Callable:
    return chain(rbind(compose, center), a1, a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_3e980e27_x30_x1', 'Callable', 'Callable', 'Callable'): 'chain(rbind(compose, center), a1, a2)'}


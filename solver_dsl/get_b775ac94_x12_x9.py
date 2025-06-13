def get_b775ac94_x12_x9(a1: Callable, a2: Callable) -> Callable:
    return chain(rbind(compose, initset), a1, a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_b775ac94_x12_x9', 'Callable', 'Callable', 'Callable'): 'chain(rbind(compose, initset), a1, a2)'}


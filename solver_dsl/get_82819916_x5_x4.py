def get_82819916_x5_x4(a1: Callable, a2: Callable) -> Callable:
    return rbind(a1, compose(a2, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_82819916_x5_x4', 'Callable', 'Callable', 'Callable'): 'rbind(a1, compose(a2, a2))'}


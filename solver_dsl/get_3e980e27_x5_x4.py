def get_3e980e27_x5_x4(a1: Callable) -> Callable:
    return lbind(compose, compose(invert, a1))

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_3e980e27_x5_x4', 'Callable', 'Callable'): 'lbind(compose, compose(invert, a1))'}


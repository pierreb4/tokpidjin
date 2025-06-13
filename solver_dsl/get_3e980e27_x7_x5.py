def get_3e980e27_x7_x5(a1: Any, a2: Callable) -> Callable:
    return compose(lbind(compose, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Any'}

func_d = {('get_3e980e27_x7_x5', 'Callable', 'Any', 'Callable'): 'compose(lbind(compose, a1), a2)'}


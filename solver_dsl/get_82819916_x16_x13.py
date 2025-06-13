def get_82819916_x16_x13(a1: Any, a2: Callable) -> Callable:
    return compose(lbind(shift, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Any'}

func_d = {('get_82819916_x16_x13', 'Callable', 'Any', 'Callable'): 'compose(lbind(shift, a1), a2)'}


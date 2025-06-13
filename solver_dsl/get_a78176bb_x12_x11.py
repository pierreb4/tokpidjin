def get_a78176bb_x12_x11(a1: Any, a2: Callable) -> Callable:
    return compose(lbind(index, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Any'}

func_d = {('get_a78176bb_x12_x11', 'Callable', 'Any', 'Callable'): 'compose(lbind(index, a1), a2)'}


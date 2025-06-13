def get_941d9a10_x6_x4(a1: Any, a2: Callable) -> Callable:
    return compose(lbind(extract, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Any'}

func_d = {('get_941d9a10_x6_x4', 'Callable', 'Any', 'Callable'): 'compose(lbind(extract, a1), a2)'}


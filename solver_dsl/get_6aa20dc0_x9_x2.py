def get_6aa20dc0_x9_x2(a1: Any, a2: Callable) -> Callable:
    return compose(lbind(occurrences, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Any'}

func_d = {('get_6aa20dc0_x9_x2', 'Callable', 'Any', 'Callable'): 'compose(lbind(occurrences, a1), a2)'}


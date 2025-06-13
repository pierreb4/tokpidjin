def get_36d67576_x13_x12(a1: Any, a2: Callable) -> Callable:
    return chain(lbind(occurrences, a1), a2, normalize)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Any'}

func_d = {('get_36d67576_x13_x12', 'Callable', 'Any', 'Callable'): 'chain(lbind(occurrences, a1), a2, normalize)'}


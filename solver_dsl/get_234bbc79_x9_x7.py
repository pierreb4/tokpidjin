def get_234bbc79_x9_x7(a1: Any, a2: Callable) -> Callable:
    return compose(lbind(matcher, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Any'}

func_d = {('get_234bbc79_x9_x7', 'Callable', 'Any', 'Callable'): 'compose(lbind(matcher, a1), a2)'}


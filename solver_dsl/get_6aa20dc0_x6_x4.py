def get_6aa20dc0_x6_x4(a1: Any, a2: Callable) -> Callable:
    return compose(lbind(matcher, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Any'}

func_d = {('get_6aa20dc0_x6_x4', 'Callable', 'Any', 'Callable'): 'compose(lbind(matcher, a1), a2)'}


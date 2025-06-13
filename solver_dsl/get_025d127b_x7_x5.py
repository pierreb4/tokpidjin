def get_025d127b_x7_x5(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return compose(rbind(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Any'}

func_d = {('get_025d127b_x7_x5', 'Callable', 'Callable', 'Any', 'Callable'): 'compose(rbind(a1, a2), a3)'}


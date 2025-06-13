def get_025d127b_x7_x6(a1: Callable, a2: Any) -> Callable:
    return compose(a1, lbind(colorfilter, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_025d127b_x7_x6', 'Callable', 'Callable', 'Any'): 'compose(a1, lbind(colorfilter, a2))'}


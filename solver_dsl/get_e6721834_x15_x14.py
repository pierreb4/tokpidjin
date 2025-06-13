def get_e6721834_x15_x14(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return chain(a1, a2, rbind(sfilter, a3))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_e6721834_x15_x14', 'Callable', 'Callable', 'Callable', 'Any'): 'chain(a1, a2, rbind(sfilter, a3))'}

